import smtplib
from email.mime.text import MIMEText
tx = open('msg.txt', 'rb')
mensaje = MIMEText(tx.read())
tx.close()
mensaje['Subject'] = 'Prueba desde python' #tema
mensaje['From'] = 'user@mail.com'#es es un mensaje
smtpserver = "smtp.gmail.com"
smtpuser = "usermail@gmail.com"#tu usr smtp, tu usuario gmail
smtppassword = "your-password"#tu pass smtp
SENDER = "user@mail.com"
RECIPIENTS = "user@mail-destin.com" #email del destinatario
session = smtplib.SMTP(smtpserver, 587)
session.ehlo()
session.starttls()
session.ehlo()
session.login(smtpuser, smtppassword)
session.sendmail(SENDER, RECIPIENTS, mensaje.as_string())
session.quit()
