import streamlit as st
import pandas as pd

st.header("velkommen til Hammerknuden Sommerpension")

st.image("logo2")

sprog = st.selectbox("sprog", options=["dansk"])

if sprog == "dansk":
    st.text("Send en forespørgelse til Hammerknuden Sommerpension")
    st.text("Kontaktoplysninger")

    navn = st.text_input("navn  ")
    telefon = st.text_input("Telefonnummer  ")
    email = st.text_input("Email adresse you@domain.dk  ")

    st.subheader("Hvilke ønsker har du ??  ")
    indcheck = st.date_input("ønsket ankomst dato: ")
    checkout = st.date_input("ønsket afrejse dato: ")

    enkelt = st.checkbox("ønskes enkeltværelse ( 1 person )  ")
    mad = st.checkbox("ønskes morgenmad under opholdet")

    st.text("Der kan bo 2 personer i hvert rum ")

    antal = st.number_input("antal væreser i alt:", value=1, step=1)
    personer = st.number_input("Antal personer ialt:", value=2, step=1)

    st.text(" Hammerknuden kan tilbyde endten dobbltseng eller enkeltsenge efter ønske")
    st.selectbox("type af seng", options=["dobbeltseng", "enkeltsenge"])










