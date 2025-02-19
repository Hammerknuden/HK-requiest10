import streamlit
import streamlit as st
import pandas as pd
from datetime import datetime, date
from pathlib import Path
import numpy as np
from confirmation_email import (admin_email, send_danish_confirmation_email, send_german_confirmation_email)
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64

st.subheader("Velkommen til")
st.title("**HAMMERKNUDEN SOMMERPENSION**")

st.image("logo2.jpg")

sprog = st.selectbox("Vælg sprog, Select language, Wählen Sie Sprache aus", options=["dansk", "english", "Deutsch"])

if sprog == "dansk":
    st.text("Send en booking forespørgelse til Hammerknuden Sommerpension")
    st.text("En forespørgelse vil normalt bliver besvaret/bekræftet inden for 12 timer")

    st.text("Kontaktoplysninger")

    navn = st.text_input("navn  ")
    telefon = st.text_input("Telefonnummer  ")
    email_address = st.text_input("Email adresse you@domain.dk  ")

    st.subheader("Hvilke ønsker har du ??  ")
    checkin_date = st.date_input("ønsket ankomst dato: ")
    checkout_date = st.date_input("ønsket afrejse dato: ")

    enkelt = st.checkbox("ønskes enkeltværelse ( 1 person )  ")
    if enkelt:
        text_sing = "dobbeltværelse ønskes anvendt som enkeltværelse"
    else:
        text_sing = ""
    mad = st.checkbox("ønskes morgenmad under opholdet")
    if mad:
        text_bf = "Morgenmad er inkluderet"
    else:
        text_bf = "Morgenmad er ikke inkluderet"

    st.text("Der kan bo 2 personer i hvert rum ")

    num_rooms = st.number_input("antal væreser i alt:", value=1, step=1)
    num_personer = st.number_input("Antal personer ialt:", value=2, step=1)

    st.text(" Hammerknuden kan tilbyde enten dobbeltseng eller enkeltsenge efter ønske")
    seng = st.selectbox("type af seng", options=["dobbeltseng", "enkeltsenge"])
    if seng == "dobbeltseng":
        text_bed = "Der er valgt dobbetseng "
    else:
        text_bed = "Der er valgt enkeltsenge  "
    extext = st.checkbox("ekstra information eller forespørgelse")
    if extext:
        text_free = st.text_input("Skriv ønsker eller yderligere information  ")
    else:
        text_free = st.text("-")

if sprog == "english":
    st.text("Send a booking booking requiest to Hammerknuden Sommerpension")
    st.text("Your inquiry will normaly be answered within 12 hours")

    st.text("Kontaktoplysninger")

    navn = st.text_input("name  ")
    telefon = st.text_input("Telefonnummer with prefix (+45...  ")
    email_address = st.text_input("Your mail adresse you@domain.dk  ")

    st.subheader("What do you need ??  ")
    checkin_date = st.date_input("Arrival date: ")
    checkout_date = st.date_input("Departure date: ")

    enkelt = st.checkbox("Do you require a single room ( for one person )  ")
    if enkelt:
        text_sing = ("The room is used as a singleroom ")
    else:
        text_sing = ""
    mad = st.checkbox("breakfirst during you stay ")
    if mad:
        text_bf = "Breakefirst is included "
    else:
        text_bf = "Breakefirst is not included "

    st.text("There are room for two persons in each room  ")

    num_rooms = st.number_input("Number of rooms in total: ", value=1, step=1)
    num_personer = st.number_input("Number of persons in total: ", value=2, step=1)

    st.text(" Hammerknuden offers dobbeltbed og singles on demand: ")
    seng = st.selectbox("type af seng", options=["dobbeltbed", "singlebeds"])
    if seng == "dobbeltbed":
        text_bed = "Your choise is dobbetbed "
    else:
        text_bed = "Your choise is singlebeds  "
    extext = st.checkbox("Any extra information or wishes")
    if extext:
        text_free = st.text_input("just start writing  ")
    else:
        text_free = st.text("")

if sprog == "Deutsch":
    st.text("Anfrage des reservation für Hammerknuden Sommerpension")
    st.text("Eiene anfrage wurde won 12 stunde anworted werden")

    st.text("Kontakt")

    navn = st.text_input("nahme  ")
    telefon = st.text_input("Telefonnummer  ")
    email_address = st.text_input("Email adresse you@domain.dk  ")

    st.subheader("Hvilke ønsker har du ??  ")
    checkin_date = st.date_input("ankomst dato: ")
    checkout_date = st.date_input("abrejse dato: ")

    enkelt = st.checkbox("ønskes enkeltværelse ( 1 person )  ")
    if enkelt:
        text_sing = "Das Doppelzimmer wird als Einzelzimmer genutzt "
    else:
        text_sing = ""

    mad = st.checkbox("ønskes morgenmad under opholdet")
    if mad:
        text_bf = "Früstuck sind inkluderet"
    else:
        text_bf = "Frûstuck sind nicht inkluderet"

    st.text("Der kan bo 2 personer i hvert rum ")

    num_rooms = st.number_input("antal væreser i alt:", value=1, step=1)
    num_personer = st.number_input("Antal personer ialt:", value=2, step=1)

    st.text(" Hammerknuden kan tilbyde enten dobbeltseng eller enkeltsenge efter ønske")
    seng = st.selectbox("type af seng", options=["dobbeltseng", "enkeltsenge"])
    if seng == "dobbeltseng":
        text_bed = "Der er valgt dobbetseng "
    else:
        text_bed = "Der er valgt enkeltsenge  "
    extext = st.checkbox("ekstra information eller forespørgelse")
    if extext:
        text_free = st.text_input("Skriv ønsker eller yderligere information  ")
    else:
        text_free = st.text("-")
# calculations and data
if enkelt:
    high_season_price = 950  # 2025 950
    low_season_price = 830  # 2025 830
    single_room = "Y"
else:
    high_season_price = 1050  # 2025 1050
    low_season_price = 930  # 2025 930
    single_room = "N"
print(high_season_price)
print(low_season_price)
#st.markdown(high_season_price)
#st.markdown(low_season_price)

bf_price = 100
rabat = 5 #online rabat sat til 5%

high_season_start = datetime.strptime("29-06-25", _format := "%d-%m-%y").date()
high_season_end = datetime.strptime("26-08-25", _format := "%d-%m-%y").date()

high_season_days = high_season_end - high_season_start
high_booking = (checkin_date >= high_season_start) and (checkout_date <= high_season_end)
low_booking = ((checkin_date <= high_season_start) and (checkout_date < high_season_start)) or (checkin_date >
                                                                                                    high_season_end)
mixbooking_early = (checkin_date < high_season_start) and (checkout_date > high_season_start)
mixbooking_end = (checkout_date > high_season_end) and (high_season_start < checkin_date) and (checkin_date <
                                                                                                   high_season_end)
days = checkout_date - checkin_date

high_season_days = high_season_end - high_season_start
mixearly = checkout_date - high_season_start
mixearly_b = high_season_start - checkin_date
mixend = high_season_end - checkin_date
mixend_b = checkout_date - high_season_end

if high_booking:
    pris = (high_season_price * int(days.days)) * int(num_rooms)
if low_booking:
    pris = (low_season_price * int(days.days)) * int(num_rooms)
if mixbooking_early:
    pris = (((int(mixearly.days) * high_season_price) + (int(mixearly_b.days) * low_season_price)) * int(num_rooms))
if mixbooking_end:
    pris = (high_season_price * (int(mixend.days)) + (int(mixend_b.days) * low_season_price)) * int(num_rooms)

if mad:
    bf_t = (days.days * int(bf_price) * int(num_personer))
else:
    bf_t = 0
print(bf_t)
#st.markdown(bf_t)
rabat_a = int(rabat) / 100
rabat_b = bf_t * rabat_a
rabat_r = pris * rabat_a
rabat_t = rabat_b + rabat_r
print(rabat_t)
#st.markdown(pris)
#st.markdown(rabat_t)

pris_tot = pris + bf_t - rabat_t
st.markdown(f"**Antal Dage i denne booking**, {days.days}")
st.markdown(f"**Foreløbig pris denne reservation med 5 % online rabat** {pris_tot:.2f}kr")
print(days.days)
print(pris_tot)


to_addr = [email_address, admin_email]  #'finnjorg@gmail.com'   #[admin_email]  #email'finnjorg@mail.dk'

confirmation_password = "pc0012hk"  #st.text_input("pc0012hk") #Pc2024Bonv
booking_submitted = st.button("Send forespørgelse")

if sprog == "dansk" and booking_submitted:
    send_danish_confirmation_email(to_addr, confirmation_password, navn, num_rooms, num_personer, checkin_date, checkout_date,
                                   text_bf, text_bed, text_free, pris_tot)
    st.markdown('forespørgelse er afsendt dette vindue kan lukkes')

elif sprog == "english" and booking_submitted:
    send_danish_confirmation_email(to_addr, confirmation_password, navn, num_rooms, num_personer, checkin_date, checkout_date,
                                   text_bf, text_bed, text_free, pris_tot)
    st.markdown('Your request has been send, this window can be closed')

elif sprog == "Deutsch" and booking_submitted:
    send_german_confirmation_email(to_addr, confirmation_password, navn, num_rooms, num_personer, checkin_date, checkout_date,
                                   text_bf, text_bed, text_free, pris_tot)

else:
    st.markdown('forespørgelsen ikke sendt, sendt mail direkte til mail@hammerknuden.dk')

















