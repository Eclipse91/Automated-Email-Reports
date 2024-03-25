# Automated Email Reports Project

This project aims to automate the process of sending daily reports to clients via email. The script, `main.py`, utilizes various libraries to achieve this automation, including `smtplib`, `email`, `os`, and `schedule`. The project also includes supporting modules like `config_reader.py` for reading and validating configuration parameters and `email_sender.py` for sending emails.

## Requirements

- Python 3.x
- Required Python packages are listed in the requirements.txt file

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Eclipse91/Automated-Email-Reports.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Automated-Email-Reports
   ```
4. Install the required dependencies (creating a virtual environment is strongly recommended before this step):

   ```bash
   pip install -r requirements.txt
   ```
5. Update the config.ini and the .env file adding the parameters required, follow the steps outlined in the [Configuration](#configuration) section

6. Run the application:

   ```bash
   python3 main.py
   ```
7. Check the `email_logger.log` file for program logs and any potential issues.

## Configuration:
    - Open your .env file and set EMAIL_USERNAME = your_email and EMAIL_PASSWORD = your_password
    - Edit the config.ini file to include the necessary configuration parameters, such as the clients' email addresses, the path of the reports and a valid schedule
    - Ensure the data is formatted correctly (YYYY-MM-DD hh:mm:ss) and that it represents a timestamp occurring after the program execution time
    - Ensure the presence of valid report file paths
    - Body and subject of the mail are optional

## Usage

1. **Configuration:**
    - Update the config.ini and the .env file adding the parameters required.

2. **Execution:**
    - Run the `main.py` script to initiate the automated email report sending process.

3. **Logging:**
    - Check the `email_logger.log` file for logs and information about the execution.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.

## Notes

Feel free to contribute or report issues!
This README provides a clearer structure, concise information, and instructions for setting up and running the Automated-Email-Reports. Adjust the content as needed for your project.
