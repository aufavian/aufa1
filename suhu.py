import streamlit as st

x = st.number_input("masukkan suhu")
sx = st.text_input ("satuan", "C")
st.write("menginput suhu", x," dengan satuan ", sx)
st.write("kuadratnya", x*x)
