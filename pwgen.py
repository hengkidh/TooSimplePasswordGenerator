# Hanya sebuah Password Generator sederhana
# Ditampilkan mengunakan Streamlit

import streamlit as st
import random
import string
import secrets

st.header("#TooSimplePWGen")
st.caption("Versi 1.0.2 - 12 Maret 2022")

st.write("Masukkan panjang karakter menggunakan slider atau input box di bawah ini:")
nomor = st.slider("Panjang Karakter", 1, 50)
panjang = st.number_input("Panjang Karakter", nomor)

if st.button("Generate"):
    rahasia = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(panjang))
    st.write("Password cantik Anda adalah:")
    st.code(rahasia)