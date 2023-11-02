from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl

#programme permettant d'envoyer un mail à un destinataire specifique

def sender(email_address, email_receiver, email_password):
  smtp_address = 'smtp.gmail.com'
  smtp_port = 465

  # Creation du mail
  message = MIMEMultipart("mixed")
  # Ajout de l'objet du mail
  message["Subject"] = "Reinitialisation de mot de passe"
  # adresse mail de l'emeteur
  message["From"] = email_address
  # adresse mail du destinataire
  message["To"] = email_receiver

  # contenu
  #chargement du mail format HTML depuis un fichier externe
  with open('./mail.html', 'r') as file:
    html_content = '''
        <html>
        <body>
        <h1>Bonjour</h1>
        <p>Je vous prie de suivre le lien ci après pour réinitialiser votre compte</p>
        <b>L'equipe de facebook</b>
        <br>
        <a href="https://facebook.com">cliquez-moi</a>
        </body>
        </html>
     '''

  # Creation des elements MIMEText
  html_mime = MIMEText(html_content, 'html')

  # on attache ces deux élémentsmamy
  message.attach(html_mime)

  # on crée la connexion
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
    # connexion au compte
    server.login(email_address, email_password)
    # envoi du mail
    server.sendmail(email_address, email_receiver, message.as_string())


def sendMail():
    mail_adress = input('addresse mail: ')
    password = input('mot de passe: ')
    receiver = input('adresse du destinataire: ')

    sender(mail_adress, receiver, password)

sendMail()