import streamlit as st
import sqlite3
from datetime import datetime

# -----------------------------
# BASE DE DATOS
# -----------------------------

conn = sqlite3.connect("pruebas.db")
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS pruebas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        planta TEXT,
        maquina TEXT,
        nombre TEXT,
        producto TEXT,
        turno TEXT,
        peso REAL,
        fecha_hora TEXT
    )
""")

conn.commit()


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

    c.execute("""
        INSERT INTO pruebas
        (planta, maquina, nombre, producto, turno, peso, fecha_hora)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        planta,
        maquina,
        nombre,
        producto,
        turno,
        peso,
        fecha_hora
    ))

    conn.commit()

    st.success("Datos guardados correctamente.")

st.subheader("Registros guardados")

c.execute("SELECT * FROM pruebas ORDER BY id DESC")
registros = c.fetchall()

st.dataframe(registros)
