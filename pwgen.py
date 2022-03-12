# Hanya sebuah Password Generator sederhana
# Ditampilkan mengunakan Streamlit

import streamlit as st
import random
import string
import secrets

st.title("Password Generator Sederhana")
st.caption("Versi 1.0.0")

panjang = st.number_input("Masukkan Panjang Karakter", 10)

if st.button("Generate"):
    rahasia = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(panjang))
    st.text("Password cantik Anda adalah:")
    st.code(rahasia)