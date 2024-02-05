import logging
from datetime import datetime
import os


class ConfigReader:
    '''
    A class for reading and validating configuration parameters from a config.ini file.

    Attributes:
        parameters (dict): A dictionary to store the configuration parameters.
    '''

    def __init__(self):
        self.parameters = {}

    def read_config_file(self):
        '''
        Read the config.ini file and populate the parameters dictionary.
        '''
        try:
            with open('config.ini', 'r') as file:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        key, value = map(str.strip, line.split('='))
                        self.parameters[key] = value

        except FileNotFoundError:
            logging.error(f"Configuration file config.ini not found.")

        except Exception as e:
            logging.error(f"Error reading configuration file: {str(e)}.")

        else:
            if self.check_parameters():
                logging.info('Parameters config.ini are correct')
            else:
                logging.error("Configuration issue detected in config.ini.")
                
    def check_parameters(self):
        '''
        Check the validity of parameters.
        '''
        # Check the presence of at least one client email
        if self.parameters.get('clients_email'):
            self.parameters['clients_email'] = self.parameters['clients_email'].replace(" ", "").split(',')
        else:
            logging.error("Client email missing")
            self.parameters.clear()
            return False

        # Check the validity of the schedule
        if not self.validate_datetime_format(self.parameters.get('schedule')):
            logging.error(f"Invalid datetime {self.parameters.get('schedule')}")
            self.parameters.clear()
            return False

        # Check the existence of the report file
        if self.parameters.get('report_file_path'):
            self.parameters['report_file_path'] = self.parameters['report_file_path'].replace(" ", "").split(',')
            for report in self.parameters['report_file_path']:
                if not os.path.exists(report):
                    logging.error(f"Report file not found for {self.parameters.get('report_file_path')}")
                    self.parameters.clear()
                    return False
        else:
            logging.error('File is missing.')
            self.parameters.clear()
            return False

        # Create the configuration of the server
        if not self.add_server_configuration(self.parameters.get('email_username')):
            logging.error(f"Unknown server configuration for this email: {self.parameters.get('email_username')}")
            self.parameters.clear()
            return False

        # Check if email subject is missing
        if self.parameters.get('email_subject') == '':
            logging.warning('Email subject is missing.')

        # Check if email body is missing 
        if self.parameters.get('email_body') == '':
            logging.warning('Email body is missing.')

        return True

    def validate_datetime_format(self, datetime_str):
        '''
        Validate the format of a datetime string.
        '''
        try:
            datetime_object = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
            current_time = datetime.now()

            if datetime_object < current_time:
                return False
            
            return True

        except ValueError:
            return False

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
