import streamlit as st
import os

# ==========================
# CONFIGURACIÓN GENERAL
# ==========================
st.set_page_config(
    page_title="Portal de Recursos – Proyecto GENTE",
    page_icon="🌱",
    layout="wide"
)

# Carpetas locales
PDF_DIR = "docs"
IMG_DIR = "img"

# Lista de documentos (ajuste títulos, descripciones y nombres de archivo)
docs = [
    {
        "titulo": "Índice del Curso 1",
        "descripcion": "Curso Energia solar FV.",
        "archivo": "curso1.pdf",       # debe existir en docs/
        "imagen": "curso1.png"         # debe existir en img/
    },
    {
        "titulo": "Índice del Curso 2",
        "descripcion": "Curso Energia Eólica",
        "archivo": "curso2.pdf",
        "imagen": "curso2.png"
    },
    {
        "titulo": "Índice del Curso 3",
        "descripcion": "Curso Hidrógeno",
        "archivo": "curso3.pdf",
        "imagen": "curso3.png"
    },
    {
        "titulo": "Índice del Curso 4",
        "descripcion": "Curso Geotermia",
        "archivo": "curso4.pdf",
        "imagen": "curso4.png"
    },
]

# URL del Padlet (use la URL de embed o la normal)
PADLET_URL = "https://padlet.com/jatabordag/gente-en-formaci-n-gobernanza-energ-tica-territorio-en-forma-8wnz374bedf7tk2g"


# ==========================
# SIDEBAR (NAVEGACIÓN)
# ==========================
st.sidebar.title("Proyecto GENTE")
st.sidebar.markdown("Portal interno de recursos")

seccion = st.sidebar.radio(
    "Navegación",
    ["Inicio", "Cursos y documentos (PDF)", "Tablero Padlet"]
)


# ==========================
# SECCIÓN: INICIO
# ==========================
if seccion == "Inicio":
    st.title("Portal de recursos del proyecto GENTE")

    st.markdown(
        """
        Bienvenido al portal del proyecto **GENTE – Gobernanza Energética y Territorio**.

        Este espacio reúne en un solo lugar los materiales clave producidos por el equipo:

        - Índices y documentos base de los cursos en formato PDF  
        - Portadas gráficas de cada documento  
        - Acceso directo al tablero colaborativo en Padlet  

        El objetivo es facilitar el acceso ágil y unificado a la información que el equipo debe revisar.
        """
    )


# ==========================
# SECCIÓN: CURSOS Y DOCUMENTOS
# ==========================
elif seccion == "Cursos y documentos (PDF)":
    st.title("Cursos y documentos base (PDF)")
    st.markdown("Seleccione un documento para visualizar su portada y descargar el PDF correspondiente.")
    st.write("")

    for doc in docs:
        ruta_pdf = os.path.join(PDF_DIR, doc["archivo"])
        ruta_img = os.path.join(IMG_DIR, doc["imagen"])

        col1, col2 = st.columns([1, 2])

        with col1:
            if os.path.exists(ruta_img):
                st.image(
                    ruta_img,
                    caption=doc["titulo"],
                    use_column_width=True
                )
            else:
                st.warning(f"No se encontró la imagen: {doc['imagen']}")

        with col2:
            st.subheader(doc["titulo"])
            st.write(doc["descripcion"])

            if os.path.exists(ruta_pdf):
                with open(ruta_pdf, "rb") as f:
                    pdf_bytes = f.read()

                st.download_button(
                    label="📥 Descargar PDF",
                    data=pdf_bytes,
                    file_name=doc["archivo"],
                    mime="application/pdf"
                )
            else:
                st.error(f"No se encontró el PDF: {doc['archivo']}")

        st.markdown("---")


# ==========================
# SECCIÓN: PADLET
# ==========================
elif seccion == "Tablero Padlet":
    st.title("Tablero colaborativo – Padlet")
    st.markdown(
        """
        Espacio de trabajo colaborativo del equipo **GENTE** para registrar notas, insumos,
        reflexiones y acuerdos.
        """
    )

    if PADLET_URL and PADLET_URL != "URL_DEL_PADLET_AQUI":
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

        st.markdown(f"[Abrir Padlet en una pestaña nueva]({PADLET_URL})")
    else:
        st.warning("Configure la variable PADLET_URL con la dirección de su tablero Padlet.")

