import os
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


class EmailSender:
    '''
    A class for sending emails with attachments to a list of clients.

    Attributes:
        parameters (dict): A dictionary containing email configuration parameters.
    '''
    def __init__(self, parameters):
        self.parameters = parameters

    def test_login(self):
        '''
        Test the validity of the username and password.
        '''
        try:
            if self.add_server_configuration(self.parameters['email_username']):
                with smtplib.SMTP(self.parameters['email_server'], self.parameters['email_port']) as server:
                    server.starttls()
                    server.login(self.parameters['email_username'], self.parameters['email_password'])
                logging.info('Parameters in .env file are correct')
            else:
                return False
        except smtplib.SMTPAuthenticationError as e:
            logging.error(f"Authentication Error {self.parameters['email_username']}: {str(e)}")
            return False
        return True
    
    def add_server_configuration(self, email):
        '''
        Add server configuration based on the email domain.
        '''
        domain = self.extract_domain(email)

        if domain == 'gmail':
            self.parameters['email_server'] = 'smtp.gmail.com'
            self.parameters['email_port'] = 587
        elif domain == 'yahoo':
            self.parameters['email_server'] = 'smtp.mail.yahoo.com'
            self.parameters['email_port'] = 587
        elif domain == 'outlook':
            self.parameters['email_server'] = 'smtp.office365.com'
            self.parameters['email_port'] = 587
        else:
            logging.error(f"Domain '{domain}' of your email is not supported")
            return False

        return True
    
    def extract_domain(self, email):
        '''
        Extract the domain from an email address.
        '''
        at_index = email.find('@')
        dot_index = email.find('.', at_index)

        if at_index != -1 and dot_index != -1:
            domain = email[at_index + 1:dot_index]
            return domain
        else:
            return None
        
    def send_email(self):
        '''
        Send emails to all the clients
        '''
        for client in self.parameters['clients_email']:
            try:
                # Set up the email
                msg = MIMEMultipart()
                msg['From'] = self.parameters['email_username']
                msg['To'] = client
                msg['Subject'] = self.parameters['email_subject']

                # Attach the body of the email
                msg.attach(MIMEText(self.parameters['email_body'], 'plain'))

                # Attach the reports
                for report in self.parameters['report_file_path']:
                    with open(report, 'rb') as file:
                        attachment = MIMEApplication(file.read(), report.rfind('.'))
                        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(report))
                        msg.attach(attachment)

                # Connect to the email server and send the email
                with smtplib.SMTP(self.parameters['email_server'], self.parameters['email_port']) as server:
                    server.starttls()
                    server.login(self.parameters['email_username'], self.parameters['email_password'])
                    server.sendmail(self.parameters['email_username'], client, msg.as_string())

                logging.info(f"Email sent successfully to {client}")

            except Exception as e:
                logging.error(f"Error sending email to {client}: {str(e)}")
