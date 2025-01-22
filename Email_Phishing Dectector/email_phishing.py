import re
import sys
from email import message_from_file
from email.header import decode_header
from email.utils import parseaddr
from quopri import decodestring

def get_body(payload):
    if isinstance(payload, list):
        return ''.join(get_body(part.get_payload()) for part in payload)
    return payload

def decode_email_header(header):
    decoded_bytes, charset = decode_header(header)[0]
    if charset:
        decoded_header = decoded_bytes.decode(charset)
    else:
        decoded_header = decoded_bytes
    return decoded_header

def analyze_email(file_path):
    with open(file_path, 'r') as f:
        msg = message_from_file(f)

    headers = msg.items()
    headers = dict(headers)

    #Check for suspicious email headers
    suspicious_headers = ['X-Mailer', 'X-Priority', 'X-MSMail-Priority', 'X-Unsent', 'X-Originating-IP']
    for header in suspicious_headers:
        if header in headers:
            print('Suspicious header found: {}'.format(header))

    #check for suspicious email address in the From field and Reply-To-field {original}
    from_email = headers.get('From', '')
    reply_to = headers.get('Reply-To', '')
    if not re.match(r'.*@example\.com', from_email) or not re.match(r'.*@example\.com', reply_to):
        print('Suspicious email address found: {}'.format(from_email))

    #check for suspicious email address in the From field and Reply-To-field {decoded_one}
    from_email_d = decode_email_header(headers.get('From', ''))
    reply_to_d = decode_email_header(headers.get('Reply-To', ''))
    if not re.match(r'.*@example\.com', from_email_d) or not re.match(r'.*@example\.com', reply_to_d):
        print('Suspicious email address found: {}'.format(from_email_d))

    #Check for suspicious URLs in the body of the email
    body = get_body(msg.get_payload())
    try:
        body = decodestring(body).decode('utf-8')
    except UnicodeDecodeError:
        body = decodestring(body).decode('latin1')
    urls = re.findall(r'(https?://\S+)', body)
    for url in urls:
        if not re.match(r'.*example\.com.*', url):
            print(f"Suspicious URL found: {url}")

    # Check for suspicious attachments
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        filename = part.get_filename()
        if filename and not re.match(r'.*\.(jpg|jpeg|png|gif|doc|docx|xls|xlsx|pdf|zip|rar|7z|tar|gz)$', filename):
            print(f"Suspicious attachment found: {filename}")

    # Check for suspicious words in the subject line
    subject = decode_email_header(headers.get('Subject', ''))
    suspicious_words = ['urgent', 'account', 'password', 'security', 'confirm', 'verify', 'update', 'suspicious', 'phishing']
    for word in suspicious_words:
        if word in subject.lower():
            print(f"Suspicious word found in subject: {word}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python email_phishing.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    analyze_email(file_path)