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

planta = st.selectbox("Planta:", ["Beaumont", "California", "Florida", "Illinois", "Pennsylvania"])

if planta == "California":
    maquina = st.selectbox("Maquina: ", ["SCHNELL", "TURIA", "EVG", "WD01", "WD02", "MEP", "Otros"])
    if maquina == "WD01" or maquina == "WD02" or maquina == "SCHNELL":
        producto = st.selectbox("Producto:", ["C4", "C6", "C6.5", "C8", "C10"])
    elif maquina == "TURIA":
        producto = st.selectbox("Producto:", ["C6 7x20", "C8 8x20", "C10 4x7", "C10 5x50", "C10 5x150", "C10 7x20", "C10 7x200", "C10 7.5x20", "C10 7.5x200", "C10 8x20"])
    elif maquina == "MEP":
        producto = st.selectbox("Producto:", ["C4 7x20", "C6 4/4 7x20", "C6 4/4 7.5x20", "C6 7x20", "C6 7.5x20", "C8 7x20", "C10 4x7", "C10 4x7.5", "C10 4x8 FC", "C10 42x84 Boise", "C10 42x84 FC", "C10 42x84 UFP", "C10 7x20", "C10 7.5x20"])
    elif maquina == "EVG":
        producto = st.selectbox("Producto:", ["3/3 6 x 11", "C4 4X4 7X20", "C4 4/4 7.5 x 20", "C4 4/4 8 x 20", "C4 4/4 8x13", "C4 4/4 8X15", "C4 4/4 8x17", "C4 7 x 20", "C4 8 x 20", "C6 3/3 5 x 8", "C6 3/3 6 x 11", "C6 3/3 8 x 10", "C6 3/3 8 x 11", "C6 3/3 8 x 9", "C6 4/3 8 x 10", "C6 4/3/2 5.8 x 18", "C6 4/4 4X8", "C6 4/4 5.8 x 21.8", "C6 4/4 6 x 10", "C6 4/4 68 X 260", "C6 4/4 7 x 11", "C6 4/4 7 x 20", "C6 4/4 7.5 x 20", "C6 4/4 8 x 12", "C6 4/4 8 x 13", "C6 4/4 8 x 20", "C6 4/4 8 x 9", "C6 4/4/2 5.8 x 18", "C6 5.8X18 4X3X2", "C6 6/6 7.5 x 20", "C6 7 x 20", "C6 8 x 20", "C6 8X9 3X3", "C6.5 4/4 5.8 x 17", "C6.5 4/4 6 x 17", "C6.5 4/4 6 x 19", "C6.5 4/4/2 5'8 x 17", "C6.5 4X4 5.8X17", "C8  8 x 20 PR.  50", "C8 4/4 5.8 x 17", "C8 4/4/2 5 x 16", "C8 4X4 5.8 X 21.8", "C8 6/6 5 x 14", "C8 8 x 20", "C10 42 x 84 FC", "C10 7 x 20", "C10 8 x 20"])
    else:
        producto = st.text_input("Producto:")
elif planta == "Beaumont":
    maquina = st.selectbox("Maquina: ", ["EVG1", "EVG2", "MEP E", "MEP H", "MEP R", "Otros"])
    if maquina == "EVG1":
        producto = st.selectbox("Producto:", ["C4 8 x 20", "C6 5 x 150", "C6 8 x 12.5", "C6 8 x 20", "C8 8 x 15", "C8 8 x 20", "C10 5 x 150", "C10 8 x 20"])
    elif maquina == "EVG2":
        producto = st.selectbox("Producto:", ["12 x 12 D5.0/D5.0 8 x 20", "12 x 12 D6.0/D6.0 8 x 20", "12x12 5.0/5.0 8X20", "4 x 4 D3.5/D3.5 8 x 20", "4 x 4 D5.0/D5.0 8 x 20", "4X4  D4.5/D4.5  8x20 (146.88 lbs)", "4x4 3.5/3.5 8x20", "4x4 D7.0/D7.0 8x20", "4x4 W4/W4 3'-0.5''x10'-0'' BASKET", "6 x 12 D4.0/D4.0 8 x 20", "6 x 12 D7.4/D6.3 8 x 20", "6 x 12 D7.5/D6.5 8 x 20", "6 x 6 D5.0/D5.0 8 x 20", "6 x 6 D6.0/D6.0 8 x 20", "6 x 6 D6.5/D6.5 8 x 20", "6x12 7.5/6.5 8x20", "C4 4/4 8 x 12.5", "C4 4/4 8 x 15", "C4 4/4 8 x 20", "C4 8 x 15", "C4 8 x 20", "C6 4/4 8 x 20", "C6 6/6 5.5 x 20", "C6 8 x 20", "C8 8 x 20", "C10 8 x 20"])
    elif maquina == "MEP E" or maquina == "MEP H" or maquina == "MEP R":
        producto = st.selectbox("Producto:", ["C6 3.5 8 x 20", "C6 3.5 x 20", "C6 5 x 150", "C6 5.5 x 20", "C6 6 x 200", "C10 5 x 150", "C10 5 x 200", "C10 6 x 150", "C10 8 x 20"])
    else:
        producto = st.text_input("Producto:")
elif planta == "Pennsylvania":
    maquina = st.selectbox("Maquina: ", ["ATT", "GD6 Rolls", "GD61", "GD62", "GRS 2", "Otros"])
    if maquina == "ATT":
        producto = st.selectbox("Producto:", ["C6 4/4 5 x 10", "C6 4/4 5 x10 (50)", "C8 4/2 56 x 10", "C8 4/4 5 x 14", "C8 4/4 5 x 16", "C8 4/4 5 x 18", "C8 4/4 56 x 15", "C8 6/6 5 x 14", "C8 6/6 5 x 16"])
    elif maquina == "GD6 Rolls":
        producto = st.selectbox("Producto:", ["4 x 8  10 GA", "4/4 3 x 10  4 GA", "4X4  D4/D4  3.04x10 (26.01 lbs)", "4X4  W4/W4  3x10 (25.84 lbs)", "4x4 W4/W4 3'-0.5''x10'-0'' BASKET", "4x4 W4/W4 3x10", "5 x 13  10 GA", "5 x 150  10 GA", "5 x 50  10 GA", "C4  4/4  3 x 10", "C4  4/4  3 x 10 PR. BASKETS", "C6 5 x 10", "C8 5 x 10", "C9 4 x 8 9 GA", "C10  5 x 10 PR.  100", "C10  5 x 150", "C10 4 x 8", "C10 5 x 10", "C10 5 x 150"])
    elif maquina == "GD61":
        producto = st.selectbox("Producto:", ["4/4 8 x 12  6 GA", "4x4 D4/D4 5'-0x10'-0", "4x4 D4/D4 8'-0x15'-0", "5 x 10  10 GA", "8 x 12.5  10 GA", "8 x 15 10 GA", "8 x 20  10 GA", "8 x 20  6 GA", "8 X 20  8 GA", "C4 4/4 5 x 10", "C4 4/4 8 x 12.5", "C4 4/4 8 x 15", "C4 4/4 8 x 20", "C4 5 x 10", "C4 8 x 12.5", "C4 8 x 15", "C4 8 x 20", "C6 4/4 5 x 10", "C6 4/4 8 x 15", "C6 4/4 8 x 20", "C6 5 x 10", "C6 5 x 12", "C6 5 x 16", "C6 8 x 12.5", "C6 8 x 15", "C6 8 x 20", "C8 5 x 10", "C8 8 x 12.5", "C8 8 x 15", "C8 8 x 20"])
    elif maquina == "GD62":
        producto = st.selectbox("Producto:", ["4/4 C8 5 x 14", "C6 4/4 5 x 10", "C8  4/4 5 x 14 (140) Half", "C8  4/4 5 x 14 (150)", "C8  4/4 5 x 15 (100) Half", "C8 4/4 5 x 14", "C8 4/4 5 x 16-S", "C8 4x2 56 x 10' (100)", "C8 5 x 10", "C8 6/6 5 x 10 (100)", "C8 6/6 5 x 14", "C8 8 x 12.5", "C8 8 x 15", "C8 8 x 20", "C10  4/4 5 x 15 (50)", "C10  4/4 5 x 16 (50)", "C10  4/4/2 56X10 (100) Half", "C10  42 x 84 FC", "C10 4/4 5 x 15", "C10 4/4 5 x 15 MMS", "C10 4/4 5 x 16", "C10 4/4 52x 15 Half", "C10 4/4/2 56 x 10", "C10 42 x 84 FC", "C10 5 x 10", "C10 5 x 13", "C10 6/6 5 x 14", "C10 6/6 5 x 15", "C10 8 x 12.5", "C10 8 x 15", "C10 8 x 20", "Flush cut-6 x 6 10 / 10 - 3.5 x 7 Sheets"])
    elif maquina == "GRS 2":
        producto = st.selectbox("Producto:", ["4x4 W4/W4 3'-0.5''x10'-0'' BASKET", "C6 4/4 5 x 10", "C6 4/4 5 x10 (50)", "C8  4/4 5 x 14 (140)", "C8  4/4 5 x 14 (140) Half", "C8  4/4 5 x 14 (150)", "C8  4/4 5 x 15 (100)", "C8  4/4 5 x 15 (100) Half", "C8  4/4 5 x 16 (25)", "C8  4/4 5 x 16 (50)", "C8  4/4 5 x 18 (100) Half", "C8  6/6 5 x 14 (100) Half", "C8  6/6 5 x 14 (50) Half", "C8 4/2 56 x 10", "C8 4/4 5 x 14", "C8 4/4 5 x 16", "C8 4/4 5 x 16-S", "C8 4/4 5 x 18", "C8 4/4 5 x 18 (100) Half", "C8 4/4 56 x 15", "C8 4/4 56 x 15 MMS", "C8 4/4 56 x 15 (100) Half", "C8 4/4/2 56 x 10", "C8 4x2 56 x 10' (100)", "C8 6/6 5 x 14", "C8 6/6 5 x 14 (100)", "C8 6/6 5 x 16 MMS", "C8.5 5 X 14", "C10  4/4 5 x 15 (50)", "C10 4/4 5 x 16", "C10 4/4 5 x 16 MMS", "C10 4/4 56x 15 Half"])
    else:
        producto = st.text_input("Producto:")
elif planta == "Illinois":
    maquina = st.radio("Maquina: ", ["EVG", "MEP", "Otros"])
    if maquina == "EVG":
        producto = st.radio("Producto:", ["4/4 C10 4.8 x 15", "4/4 C10 5 x 16", "4/4 C10 5 x 18", "4/4 C10 7 x 13", "4/4 C8 5 x 16", "4/4 C8 7 x 13", "4/6 C10 4.8 x 15", "C4 4/4 8 x 15", "C4 4/4 8 x 20", "C4 8 x 15", "C4 8 x 20", "C6 4/4 68 X 260-S", "C6 4/4 8 x 15", "C6 4/4 8 x 20", "C6 8 x 12.5", "C6 8 x 15","C6 8 x 20", "C6.5 4/4 5'8 x 17'", "C8  4/4 5 x 18", "C8 4/4 4.8 x 15", "C8 4/4 5 x 10", "C8 4/4 5 x 16", "C8 4/4 5 x 16-S", "C8 4/4 5 x 18", "C8 4/4 5.8 x 17", "C8 4/4 56 x 15-S", "C8 4/4 7 x 13", "C8 4/4/2 56 x 10", "C8 4x4 8 X 20", "C8 8 x 12.5", "C8 8 x 15", "C8 8 x 20", "C10  4/4 5 x 18", "C10  42 x 84 FC", "C10 4 x 8", "C10 4/4 4.8 x 15", "C10 4/4 4.8 x 15-S", "C10 4/4 5 x 16", "C10 4/4 5 x 16-S", "C10 4/4 5 x 18", "C10 4/4 5 x 18-S", "C10 4/4 52 x 15", "C10 4/4 52 x 15-S", "C10 4/4 7 x 13", "C10 4/4/2 56 x 10", "C10 4/6 4.8 x 15", "C10 4/6 4.8 x 16", "C10 4/6 5 X 14-S", "C10 4/6 56 X 15-S", "C10 42 x 84 FC", "C10 5 x 10", "C10 8 x 15", "C10 8 x 20"])
    elif maquina == "MEP":
        producto = st.radio("Producto:", ["C6 8 x 12.5", "C6 8 x 15", "C6 8 x 20", "C8 8 x 12.5", "C8 8 x 15", "C8 8 x 20", "C10  4 x 8", "C10  5 x 150", "C10  5 x 50", "C10 4 x 8", "C10 4 x 8 FC", "C10 5 x 144", "C10 5 x 150", "C10 5 x 50", "C10 8 x 12.5", "C10 8 x 15", "C10 8 x 20"])
    else:
        producto = st.text_input("Producto:")
elif planta == "Florida":
    maquina = st.radio("Maquina: ", ["KOCH", "KOCH2", "MEP1", "MEP2", "PITTINI", "PITTINI2", "TEUREMA", "TURIA", "Otros"])
    if maquina == "KOCH" or maquina == "PITTINI2":
        producto = st.radio("Producto:", ["BB Deformed Positive Wire 0.375 1018", "Bright Basic Deformed Posit 0.5000 1018", "Bright Basic_.244_ASTM A 1064 W-4.7", "Brigth Basic_.250_ASTM A 1064 W-4.9", "DeformedPositiveWire _.625_A1064 D-30.7"])
    elif maquina == "KOCH2" or maquina == "PITTINI" or maquina == "TEUREMA" or maquina == "TURIA":
        producto = st.radio("Producto:", ["C3", "C4", "C6", "C8", "C10", "C10.5"])
    elif maquina == "MEP1":
        producto = st.radio("Producto:", ["5 x 150  6 GA", "C10 5 x 150", "C10 5 x 200", "C10 5 x 50", "C10 6 x 150", "C10.5 5 x 150"])
    elif maquina == "MEP2":
        producto = st.radio("Producto:", ["4/4 8 x 15  4 GA", "4/4 8 x 20  6 GA", "5 x 10  10 GA", "5 x 10  6 GA", "6x12 D2.9/D2.1 7'10x25'", "6x12 D2.9/D2.1 7'10x31'", "6x6 D3/D3 8'4x11'10 4 GA", "8 x 15  4 GA", "C4 4/4 8 x 20", "C4 8 x 20", "C6  8 x 20", "C6 3.5 x 20", "C6 4/4 8 x 20", "C6 8 x 15", "C6 8 x 20", "C8 8 x 20", "C10 42 x 84 FC", "C10 5 x 10", "C10 8 x 12.5", "C10 8 x 15", "C10 8 x 20"])
    else:
        producto = st.text_input("Producto:")

nombre = st.text_input("Operador:")


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
