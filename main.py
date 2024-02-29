import logging
import sched
import time
from datetime import datetime, timedelta
from config_reader import ConfigReader
from email_sender import EmailSender


def send_daily_reports(scheduler, parameters, emails):
    # Get the current datetime
    current_datetime = datetime.now()
    tomorrow_with_time = current_datetime + timedelta(hours=24)

    # Schedule for the next day
    tomorrow = 24 * 3600 # seconds
    scheduler.enter(tomorrow, 1, send_daily_reports, (scheduler, parameters, emails))
    logging.info(f'New schedule for tomorrow: {tomorrow_with_time}')
    
    # Initiate email sending
    emails.send_email()

def main():
    # Logger
    logging.basicConfig(filename='email_logger.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Program started')

    # Read Configuration
    parameters = ConfigReader()
    parameters.read_config_file()

    # Do not schedule or run if there are configuration issues
    if parameters.parameters:
        emails = EmailSender(parameters.parameters)
        login_success = emails.test_login()
        
        # Avoid scheduling or executing tasks if login is not possible
        if login_success:
            # Run and Schedule
            scheduler = sched.scheduler(time.time, time.sleep)
            scheduled_time = time.mktime(time.strptime(parameters.parameters['schedule'], "%Y-%m-%d %H:%M:%S"))
            
            logging.info(f'New schedule: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(scheduled_time))}')    
            scheduler.enterabs(scheduled_time, 1, send_daily_reports, (scheduler, parameters, emails))

            scheduler.run()
        else:
            print('Authentication issues detected in config.ini. See email_logger.log for details.')
    else:
        print('Configuration issues detected in config.ini. See email_logger.log for details.')

    logging.info('Program Ended')

if __name__ == '__main__':
    main()
