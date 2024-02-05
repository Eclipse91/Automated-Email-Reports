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
        try:
            with smtplib.SMTP(self.parameters['email_server'], self.parameters['email_port']) as server:
                server.starttls()
                server.login(self.parameters['email_username'], self.parameters['email_password'])

        except smtplib.SMTPAuthenticationError as e:
            logging.error(f"Authentication Error {self.parameters['email_username']}: {str(e)}")
            return False
        return True
    
    def send_email(self):
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
