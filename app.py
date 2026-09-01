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

st.write("Supabase conectado correctamente")

if st.button("TEST SUPABASE"):

    try:
        result = supabase.table("pruebas").insert({
            "planta": "TX",
            "maquina": "TEST",
            "nombre": "PRUEBA",
            "producto": "TEST",
            "turno": "Day",
            "peso": 100,
            "fecha_hora": datetime.now().isoformat()
        }).execute()

        st.success("INSERT FUNCIONÓ")
        st.write(result.data)

    except Exception as e:
        st.error("INSERT FALLÓ")
        st.exception(e)
