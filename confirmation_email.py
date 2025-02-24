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


def send_email(confirmation_password, email):
    context = ssl.create_default_context()
    # Send the message via local SMTP server.
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(admin_email, confirmation_password)
        server.send_message(email)


def danish_email_html_template(logo_cid, navn, num_rooms, num_personer, checkin_date, checkout_date,
                               text_sing, text_bf, text_bed, text_free, pris_tot, text_price, email_address, telefon):

    return f"""<html>        <html style="display: table; margin: auto;">
        <head>
            <meta charset="UTF-8" />
            <title>Reservationsformular</title>
            <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
        </head>

        <body style="display: table-cell; vertical-align: left;">
            <hr>
            <h1> **************************** </h1> 
            <h1>   Reservations forespørgelse</h1> 
            <h1> **************************** </h1>

            <img src ="cid:{logo_cid}" alt=logo width="300"/>
            </p>
            <p>
            Tak for din interesse i at bo hos os på Hammerknuden <BR> Vi har noteret dine ønsker for 
            <b>{navn}</b> 
            </p>
            <p>Der ønskes {num_rooms} Dobbelt værelse med bad, kitchenette og terrasse til ialt 
            {num_personer} personer. </p>
                  
            <hr>
            <p>Indcheck er den<span style="padding-left:3em"><b> {checkin_date}</b></span></p>
            <p>Udcheck den<span style="padding-left:4em"><b> {checkout_date}</b></span></p>
            <hr>
            <p>Indcheck er efter kl. 14:30 på indcheckningsdagen og udcheck før kl. 10:00, ellers efter aftale</p>
            <hr>
            <table>
                <tr>
                    <p>{text_sing}</p>
                    <p>{text_bf}</p>
                    <p> {text_bed} </p>
                    <p>{text_free} </p>
                    <td><span style=float:right> -- </style></td>
                </tr>
            <hr>          
                
                <p> Opholdet er foreløbigt beregnet til {pris_tot:.2f}kr inklusiv 5% onlinerabat.
            <hr>
                <p> kontaktoplysninger: <BR>
                Mail {email_address} <BR>
                Telefon {telefon}
            </p>
            <p align="center"><strong>HAMMERKNUDEN SOMMERPENSION</strong><br>
            Hammershusvej 74 - 3770 Allinge<br>
            mail@hammerknuden.dk - +45 56481750  (call only)<br>
            Mobil pay - 133565 or Danske Bank reg 4720 kt 4720758679</align></p></p>
        </body>
        </html>
    """


def send_danish_confirmation_email(to_addr, confirmation_password, navn, num_rooms, num_personer,
                                   checkin_date, checkout_date, text_sing, text_bf, text_bed,
                                   text_free, pris_tot, text_price, email_address, telefon):
    logo_cid = make_msgid()
    html_content = danish_email_html_template(logo_cid[1:-1], navn, num_rooms, num_personer, checkin_date,
                                              checkout_date, text_sing, text_bf, text_bed, text_free, pris_tot,
                                              text_price, email_address, telefon)
# construct email
    email = EmailMessage()

    email['Subject'] = Subject
    email['From'] = sender_email
    email['To'] = to_addr
    email.set_content("Email client does not support html content")
    email.add_alternative(html_content, subtype='html')

    with open(logo_path, 'rb') as img:
        email.get_payload()[0].add_related(img.read(), 'image', 'jpeg', cid=logo_cid)

    send_email(confirmation_password, email)


def english_email_html_template(logo_cid, navn, num_rooms, num_personer, checkin_date, checkout_date,
                                text_sing, text_bf, text_bed, text_free, pris_tot, text_price, email_address, telefon):
    return f"""<html>        <html style="display: table; margin: auto;">
        <head>
            <meta charset="UTF-8" />
            <title>Reservationsformular</title>
            <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
        </head>

        <body style="display: table-cell; vertical-align: left;">
            <hr>
            <h1> **************************** </h1> 
            <h1>   Reservation request</h1> 
            <h1> **************************** </h1>

            <img src ="cid:{logo_cid}" alt=logo width="300"/>
            </p>
            <p>
            Thank you for you interest in staying af Hammerknuden, we have recieved the following request for 
            <b>{navn}</b> 
            </p>
            <p>The total nummer of rooms {num_rooms} Dobbelt værelse med bath, kitchenette and terrasse for  
            {num_personer} personer. </p>

            <hr>
            <p>Inncheck on the<span style="padding-left:3em"><b> {checkin_date}</b></span></p>
            <p>Checkout on the<span style="padding-left:4em"><b> {checkout_date}</b></span></p>
            <hr>
            <p>Indcheck is from kl. 14:30 on date of arrivel og Checkout before kl. 10:00, other after agreement</p>
            <hr>
            <table>
                <tr>
                    <p>{text_sing}</p>
                    <p>{text_bf}</p>
                    <p> {text_bed} </p>
                    <p>{text_free} </p<
                    <td><span style=float:right> -- </style></td>
                </tr>
            <hr>          

                <p> Estimated price is calculated to {pris_tot:.2f}kr inclusiv 5% online-discount.
            <hr>
                <p> Your Contact information:<BR>
                Email : {email_address} <BR>
                Telephone  {telefon}
            </p>
            <p align="center"><strong>HAMMERKNUDEN SOMMERPENSION</strong><br>
            Hammershusvej 74 - 3770 Allinge<br>
            mail@hammerknuden.dk - +45 56481750  (call & SMS)<br>
            Mobil pay - 133565 or Danske Bank reg 4720 kt 4720758679</align></p></p>
        </body>
        </html>
    """


def send_english_confirmation_email(to_addr, confirmation_password, navn, num_rooms, num_personer,
                                    checkin_date, checkout_date, text_sing, text_bf, text_bed, text_free, pris_tot,
                                    text_price, email_address, telefon):
    logo_cid = make_msgid()
    html_content = danish_email_html_template(logo_cid[1:-1], navn, num_rooms, num_personer, checkin_date,
                                              checkout_date, text_sing, text_bf, text_bed, text_free, pris_tot,
                                              text_price, email_address, telefon)
    # construct email
    email = EmailMessage()

    email['Subject'] = Subject
    email['From'] = sender_email
    email['To'] = to_addr
    email.set_content("Email client does not support html content")
    email.add_alternative(html_content, subtype='html')

    with open(logo_path, 'rb') as img:
        email.get_payload()[0].add_related(img.read(), 'image', 'jpeg', cid=logo_cid)

    send_email(confirmation_password, email)


def german_email_html_template(logo_cid, navn, num_rooms, num_personer, checkin_date, checkout_date,
                               text_sing, text_bf, text_bed, text_free, pris_tot, text_price, email_address, telefon):
    return f"""<html>        <html style="display: table; margin: auto;">
        <head>
            <meta charset="UTF-8" />
            <title>Reservationsformular</title>
            <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
        </head>

        <body style="display: table-cell; vertical-align: left;">
            <hr>
            <h1> **************************** </h1> 
            <h1>   Reservierungsanfrage</h1> 
            <h1> **************************** </h1>

            <img src ="cid:{logo_cid}" alt=logo width="300"/>
            </p>
            <p>
            Vielen Dank für Ihr Interesse an einem Urlaub in Hammerknuden, Folgende Wünsche haben wir notiert 
            <b>{navn}</b> 
            </p>
            <p>Der ønskes {num_rooms} Doppelzimmer, Ed bad, kochnische und Terrasse für  
            {num_personer} Gäste. </p>

            <hr>
            <p>Reservierung ist von<span style="padding-left:3em"><b> {checkin_date}</b></span></p>
            <p>Bis <span style="padding-left:4em"><b> {checkout_date}</b></span></p>
            <hr>
            <p>Der Check-in erfolgt später kl. 14:30 Uhr am des tag des check-in und check-out vorher kl. 10:00 Uhr 
            ansonsten Vereinbarung</p>
            <hr>
            <table>
                <tr>
                    <p>{text_bf}</p>
                    <p> {text_bed} </p>
                    <p>{text_free} </p<
                    <td><span style=float:right> -- </style></td>
                </tr>
            <hr>          

                <p> Vorläufig berechneter Preis für den Aufenthalt inklusive 5 % Online-Rabatt {pris_tot:.2f}kr.
            <hr>
                <p> Ihren kontakt information: <BR>
                Email : {email_address} <BR>
                Telefon : {telefon}
            </p>
            <p align="center"><strong>HAMMERKNUDEN SOMMERPENSION</strong><br>
            Hammershusvej 74 - 3770 Allinge<br>
            mail@hammerknuden.dk - +45 56481750  (call & SMS)<br>
            Mobil pay - 133565 or Danske Bank reg 4720 kt 4720758679</align></p></p>
        </body>
        </html>
    """


def send_german_confirmation_email(to_addr, confirmation_password, navn, num_rooms, num_personer,
                                   checkin_date, checkout_date, text_sing, text_bf, text_bed,
                                   text_free, pris_tot, text_price, email_address, telefon):
    logo_cid = make_msgid()
    html_content = german_email_html_template(logo_cid[1:-1], navn, num_rooms, num_personer, checkin_date,
                                              checkout_date, text_sing, text_bf, text_bed, text_free, pris_tot,
                                              text_price, email_address, telefon)
    # construct email
    email = EmailMessage()

    email['Subject'] = Subject
    email['From'] = sender_email
    email['To'] = 'to_addr'
    email.set_content("Email client does not support html content")
    email.add_alternative(html_content, subtype='html')

    with open(logo_path, 'rb') as img:
        email.get_payload()[0].add_related(img.read(), 'image', 'jpeg', cid=logo_cid)

    send_email(confirmation_password, email)
