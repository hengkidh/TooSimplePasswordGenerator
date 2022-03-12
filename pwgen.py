# Hanya sebuah Password Generator sederhana
# Ditampilkan mengunakan Streamlit

import streamlit as st
import random
import string
import secrets

st.title("#TooSimplePasswordGenerator")
st.caption("Versi 1.0.1")

st.text("Masukkan panjang karakter menggunakan slider atau input box di bawah ini:")
nomor = st.slider("Panjang Karakter", 1, 50)
# st.write("atau")
panjang = st.number_input("Panjang Karakter", nomor)

if st.button("Generate"):
    rahasia = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(panjang))
    st.text("Password cantik Anda adalah:")
    st.code(rahasia)