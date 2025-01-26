import smtplib
from email.message import EmailMessage
import ssl
from email.utils import make_msgid
from pathlib import Path
from datetime import datetime


port = 587 #587
smtp_server = 'send.one.com'  #'asmtp.yousee.dk'
Subject = "Hammerknuden Reservation"
sender_email = 'reservation@hammerknuden.dk' #'Hkreservation@mail.dk'
admin_email = 'reservation@hammerknuden.dk' #'Hkreservation@mail.dk'  #'reservation@hammerknuden.dk'
logo_path = Path("logo2.jpg")
