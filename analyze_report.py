import xml.etree.ElementTree as ET
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# tree = ET.parse('./error_report.xml')
tree = ET.parse('./report.xml')
root = tree.getroot()

sender_email = "support@chainsecurity.asia"
receiver_email = "patrickwu8894@gmail.com"
subject = "API Error"
# body = "API Response is not valid!"

smtp_server = "email-smtp.us-west-2.amazonaws.com"
smtp_port = 587
email_username = "AKIAS7ZPBOAL3NP6M47X"
email_password = "BJE4alkKMjQeebGhz4RQlXOlGofZfPiygmlIlvRM3Tco"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
# message.attach(MIMEText(body, "plain"))

testsuites = root.findall('.//testsuite')

for testsuite in testsuites:

    testcases = testsuite.findall('.//testcase')
    
    for testcase in testcases:
        failures = testcase.findall('failure')
        
        if failures:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(email_username, email_password)
                body = f"Testsuite: {testsuite.get('name')}, Testcase: {testcase.get('name')} has failures."
                message.attach(MIMEText(body, "plain"))
                server.sendmail(sender_email, receiver_email, message.as_string())

            print(f"Testsuite: {testsuite.get('name')}, Testcase: {testcase.get('name')} has failures.")
            
            for failure in failures:
                print(f"Failure message: {failure.get('message')}")
            
            print("---")