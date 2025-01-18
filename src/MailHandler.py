from os import environ
from smtplib import SMTP


from dotenv import load_dotenv

class Message:
    def __init__(self, subject:str , content: str):
        self.message = f"Subject:{subject}\n\n{content}"


def send_cafe_request_email(smtp_server: str, email_address: str,
                            sender_auth: str, message: str):
    with SMTP(smtp_server) as connection:
        connection.starttls()
        connection.login(email_address, sender_auth)
        connection.sendmail(from_addr=email_address, to_addrs=email_address,
                            msg=message)

if __name__ == "__main__":
    load_dotenv(".env")

    PW = environ["PW"]
    EMAIL = environ["EMAIL"]
    SERVER = environ["SERVER"]
    test_message = Message("Hello world", "Please add my cafe to your website").message
    send_cafe_request_email(smtp_server=SERVER,
                            email_address=EMAIL,
                            sender_auth=PW,
                            message=test_message
                            )




