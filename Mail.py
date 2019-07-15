import smtplib
import datetime


class Mailer:
    MAIL = "thefirst.test.mail@gmail.com"
    MAIL_PASSWORD = "wearethefirst"
    HOST = "smtp.gmail.com"
    PORT = 465
    SUBJECT = "Заявка с посадочной страницы"
    TO = "thefirst.test.mail@gmail.com"
    FROM = "thefirst.test.mail@gmail.com"

    def send_mail(self, message):
        res_m = self.construct_message(message)
        try:
            BODY = "\r\n".join((
                "From: %s" % self.FROM,
                "To: %s" % self.TO,
                "Subject: %s" % self.SUBJECT,
                "",
                res_m
            ))

            server = smtplib.SMTP('smtp.gmail.com:25')
            #server.set_debuglevel(1)
            server.ehlo()
            server.starttls()
            server.login(self.MAIL, self.MAIL_PASSWORD)
            server.sendmail(self.FROM, self.TO, BODY.encode('utf-8'))
            server.close()
            print("Заявка отправленна: " + res_m)
        except smtplib.SMTPServerDisconnected:
            print("connection closed")

    def construct_message(self, message):
        words = message.split()
        temp = ""
        for i in range(len(words) - 1):
            temp += words[i] + " "
        res_message = "Клиент " + temp + "с посадочной страницы оставил заявку на звонок по номеру " + words[len(words) - 1] + ". Дата заявки: " + str(datetime.datetime.now())
        return res_message
