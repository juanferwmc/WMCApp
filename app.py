import streamlit as st
from supabase import create_client
from datetime import datetime

# -----------------------------
# BASE DE DATOS
# -----------------------------

supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

# -----------------------------
# INTERFAZ
# -----------------------------

st.title("Registro de Pruebas")

planta = st.radio("Planta:", ["BW", "PA", "FL", "CA", "IL", "CR", "TX", "AR"])

maquina = st.text_input("Máquina:").upper()

nombre = st.text_input("Operador:")

producto = st.text_input("Producto:").upper()

turno = st.selectbox(
    "Turno:",
    ["Day", "Night"]
)

peso = st.number_input(
    "Peso:",
    min_value=0.0
)


# -----------------------------
# GUARDAR
# -----------------------------

if st.button("Guardar"):

    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    supabase.table("pruebas").insert({
        "planta": planta,
        "maquina": maquina,
        "nombre": nombre,
        "producto": producto,
        "turno": turno,
        "peso": peso,
        "fecha_hora": fecha_hora
    }).execute()

    st.success("Datos guardados correctamente.")

st.dataframe(registros)
