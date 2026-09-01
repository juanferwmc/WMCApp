import streamlit as st
from supabase import create_client
from datetime import datetime
from zoneinfo import ZoneInfo

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

if st.button("Guardar Registro"):

    fecha_hora = datetime.now(
        ZoneInfo("America/Chicago")
    ).strftime("%Y-%m-%d %H:%M:%S")
    
    result = supabase.table("pruebas").insert({
        "planta": planta,
        "maquina": maquina,
        "nombre": nombre,
        "producto": producto,
        "turno": turno,
        "peso": peso,
        "fecha_hora": datetime.now().isoformat()
    }).execute()

    st.success("Registros Guardados")
