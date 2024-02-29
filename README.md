# Automated Email Reports Project

This project aims to automate the process of sending daily reports to clients via email. The script, `main.py`, utilizes various libraries to achieve this automation, including `smtplib`, `email`, `os`, and `schedule`. The project also includes supporting modules like `config_reader.py` for reading and validating configuration parameters and `email_sender.py` for sending emails.

## Project Overview

### main.py

The main script orchestrates the entire automation process. It performs the following steps:

1. **Import Necessary Libraries:**
    - `logging`: For logging information and errors.
    - `sched`: For scheduling the script to run daily.
    - `time`: For handling time-related operations.
    - `datetime`: For working with date and time.
    - `ConfigReader`: Module for reading and validating configuration parameters.
    - `EmailSender`: Module for sending emails.

2. **Function Definitions:**
    - `send_daily_reports`: Schedules and sends daily reports to clients.
    - `main`: The main function that initializes logging, reads configuration, and schedules the daily report sending.

3. **Execution:**
    - Checks configuration parameters.
    - Initializes an `EmailSender` object.
    - Tests login credentials.
    - Schedules the daily report sending using the `schedule` library.

### config_reader.py

This module reads and validates configuration parameters from the `config.ini` file. It includes the following:

- `ConfigReader` class with methods:
    - `read_config_file`: Reads the configuration file and populates the parameters dictionary.
    - `check_parameters`: Validates the configuration parameters.
    - `validate_datetime_format`: Validates the format of a datetime string.
    - `add_server_configuration`: Adds server configuration based on the email domain.
    - `extract_domain`: Extracts the domain from an email address.

### email_sender.py

This module handles the sending of emails with attachments. It includes the following:

- `EmailSender` class with methods:
    - `test_login`: Tests the login credentials.
    - `send_email`: Sends emails with attachments to clients.

## Requirements

- Python 3.x
- Libraries: `smtplib`, `email`, `os`, `schedule`

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Eclipse91/Automated-Email-Reports.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Automated-Email-Reports
   ```

3. Explore Configuration Below
   Update the config.ini adding the parameters required
4. Run the application:

   ```bash
   python main.py
   ```
5.Check the `email_logger.log` file for program logs and any potential issues.

## Usage

1. **Configuration:**
    - Edit the config.ini file to include the necessary configuration parameters, such as your email, your password, the clients' email addresses, and a valid schedule
    - Ensure the data is formatted correctly (YYYY-MM-DD hh:mm:ss) and that it represents a timestamp occurring after the program execution time
    - Ensure the presence of valid report file paths
    - Body and subject of the mail are optional

2. **Execution:**
    - Run the `main.py` script to initiate the automated email report sending process.
    - Check the `email_logger.log` file for logs and information about the execution.

3. **Logging:**
    - The `email_logger.log` file records program execution, errors, and email sending information.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.

## Notes

Feel free to contribute or report issues!
This README provides a clearer structure, concise information, and instructions for setting up and running the Automated-Email-Reports. Adjust the content as needed for your project.
