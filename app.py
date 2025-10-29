import streamlit as st
st.title("Ejemplo para usar sesion_state")

if "count" not in st.session_state:
  st.sesion_state["count"]= 0

st.write(st.sesion_state)
