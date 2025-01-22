# Email Phishing Detector

This script analyzes email messages for potential phishing indicators.

>Download the email message.

## Usage

1. Install the required dependencies: `pip install email quopri`
2. Save the script to a file named `email_phishing.py`.
3. Run the script with the path to the email message as an argument: `python email_phishing.py path_to_email_message.eml`

## Description

The script takes an email message file as input and analyzes it for potential phishing indicators. It checks for suspicious email headers, suspicious email addresses in the 'From' and 'Reply-To' fields, suspicious URLs in the email body, suspicious attachments, and suspicious words in the subject line.

The script uses the `email` module to parse and analyze email messages, and the `quopri` module for decoding MIME encoded strings. It also uses regular expressions for pattern matching.

## Note

This script is a basic example and may require further refinement and testing for a production environment. It's important to use caution when analyzing email messages, as phishing attempts can be sophisticated and may evade detection.

> Make sure to replace path_to_email_message.eml with the actual file path of the email message you want to analyze.

> Remember to run the script in a Python environment where the required dependencies (email and quopri) are installed.
