import streamlit as st
st title("Ejemplo para usar sesion state")

count=0

increment=st.button("Increment")
if increment:
  count=1

st writte("Count= , count)
