import smtplib

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "tesouros.e.reliquiasrpg@gmail.com"
MY_PASSWORD = "rpgrpgrpg"


class NotificationManager:
    def send_emails(self, emails, message, flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{flight_link}".encode('utf-8')
                )
                print("got it")