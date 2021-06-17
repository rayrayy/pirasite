import smtplib

sender_email = "imperial.kvm@gmail.com"
password = "Student123?"

receiver_email = "rrz1618@ic.ac.uk"


server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(sender_email, password)

def send_message(msg):
    server.sendmail(sender_email, receiver_email, msg)


if __name__ == "__main__":
    send_message("Test!")