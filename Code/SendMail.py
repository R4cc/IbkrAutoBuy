import smtplib, ssl
from datetime import datetime

def SendMail(Ticker, Log):
    dt = (datetime.now()).strftime("%d.%m.%Y %H:%M:%S")

    sender_email = "sendermail@example.com" # SMTP mail
    receiver_email = "yourmail@example.com"
    
    SUBJECT = f"IBKR API - BUY {Ticker} AT {dt}"
    TEXT =f"BUY: {Ticker} \nAT {dt}\nON IBKR\n\n{Log}"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)


    port = 465  # For SSL
    password = "PASSWORD" # SMTP Password

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(
        "smtp.gmail.com", # THIS IS YOUR SMPTSERVER (In this case gmail)
        port, 
        context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

