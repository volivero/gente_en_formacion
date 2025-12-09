import streamlit as st
import base64
import os

# ---------------------------
# CONFIGURACIÓN
# ---------------------------
st.set_page_config(
    page_title="Portal de Recursos – Proyecto GENTE",
    page_icon="🌱",
    layout="wide"
)

# Carpeta local donde estarán los PDFs
PDF_DIR = "docs"

# Lista de documentos
docs = [
    {
        "titulo": "Índice del Curso 1",
        "descripcion": "Contenido general del módulo 1, objetivos y estructura.",
        "archivo": "Indice_Curso_Solar_Storybooks.pdf"
    },
    {
        "titulo": "Índice del Curso 2",
        "descripcion": "Contenido general del módulo 2.",
        "archivo": "Indice_Curso_Eolico_Storybooks.pdf"
    },
    {
        "titulo": "Índice del Curso 3",
        "descripcion": "Guía metodológica del módulo 3.",
        "archivo": "Indice_Curso_Hidrógeno_Storybooks.pdf"
    },
    {
        "titulo": "Índice del Curso 4",
        "descripcion": "Material complementario del curso.",
        "archivo": "Indice_Curso_Geotermia_Storybooks.pdf"
    },
]

PADLET_URL = "https://padlet.com/jatabordag/gente-en-formaci-n-gobernanza-energ-tica-territorio-en-forma-8wnz374bedf7tk2g"


# ---------------------------
# Función para mostrar PDF local embebido
# ---------------------------
def mostrar_pdf_local(ruta_pdf):
    with open(ruta_pdf, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.title("Proyecto GENTE")
st.sidebar.markdown("Portal interno de recursos")

seccion = st.sidebar.radio(
    "Navegación",
    ["Inicio", "Cursos y documentos (PDF)", "Tablero Padlet"]
)


# ---------------------------
# SECCIONES
# ---------------------------

if seccion == "Inicio":
    st.title("Portal de recursos del proyecto GENTE")
    st.markdown("""
        Bienvenido al portal del proyecto **GENTE – Gobernanza Energética y Territorio**.
        
        Aquí encontrará:
        - Los 4 índices del curso en PDF  
        - Acceso directo al tablero colaborativo en Padlet  
    """)

elif seccion == "Cursos y documentos (PDF)":
    st.title("Cursos y documentos base (PDF)")
    st.markdown("Seleccione un documento para visualizarlo o descargarlo.")

    for doc in docs:
        st.subheader(doc["titulo"])
        st.write(doc["descripcion"])

        ruta = os.path.join(PDF_DIR, doc["archivo"])

        # Descargar archivo
        with open(ruta, "rb") as f:
            st.download_button(
                label="📥 Descargar PDF",
                data=f,
                file_name=doc["archivo"],
                mime="application/pdf"
            )

        # Mostrar embebido
        mostrar_pdf_local(ruta)

        st.markdown("---")

elif seccion == "Tablero Padlet":
    st.title("Tablero colaborativo – Padlet")
    st.markdown("Visualización del espacio colaborativo del equipo GENTE:")

    padlet_iframe = f"""
    <iframe 
        src="{PADLET_URL}" 
        width="100%" 
        height="600"
        style="border-radius: 12px;"
        frameborder="0">
    </iframe>
    """
    st.components.v1.html(padlet_iframe, height=620, scrolling=True)

    st.markdown(f"[Abrir Padlet en nueva pestaña]({PADLET_URL})")
