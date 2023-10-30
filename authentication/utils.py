from django.core.mail import EmailMessage
import threading
import base64
import json

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Util:
    @staticmethod
    def send_email(data):
        """
        Function to Send Email
        """
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        EmailThread(email).start()


class TokenDecode:
    @staticmethod
    def _do(token: str) -> dict:
        """
        Parse Google OAuth2.0 id_token payload
        """
        parts = token.split(".")
        if len(parts) != 3:
            raise Exception("Incorrect id token format")
        payload = parts[1]
        padded = payload + "=" * (4 - len(payload) % 4)
        decoded = base64.b64decode(padded)
        return json.loads(decoded)
