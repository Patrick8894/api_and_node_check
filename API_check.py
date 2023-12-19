import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

api_endpoint = 'https://api-optimistic.etherscan.io/api?module=account&action=txlist&address=0x389d85599fdebc831b8b8d3667e15a35414b3e99&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=W38SDZ5NTCYJCZQWWK69X82D1ER8PRWB5A'

sender_email = "support@chainsecurity.asia"
receiver_email = "patrickwu8894@gmail.com"
subject = "API Error"
body = "API Response is not valid!"

smtp_server = "email-smtp.us-west-2.amazonaws.com"
smtp_port = 587
email_username = "AKIAS7ZPBOAL3NP6M47X"
email_password = "BJE4alkKMjQeebGhz4RQlXOlGofZfPiygmlIlvRM3Tco"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

response = requests.get(api_endpoint)

if response.status_code == 200:
    data = response.json()
    
    if data["status"] == "1" and data["message"] == "OK" and len(data["result"]) > 0:
        print("API Response is valid.")
    else:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_username, email_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("API Response is not valid.")

else:
    print("Error:", response.status_code)
    print("Response content:", response.text)