import smtplib

sender_email = "3words.api@gmail.com"
password = "3wordsapp*"

def sendEmail(destination:str , message:str ):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, destination, message)
