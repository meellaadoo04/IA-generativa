import streamlit as st
import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Configurar el cliente de Azure OpenAI
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01"
)

# Función para resumir el correo
def resumir_email(email):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente útil que resume correos."},
            {"role": "user", "content": f"Resume el siguiente correo: {email}"}
        ]
    )
    return response.choices[0].message.content

# Función para generar una respuesta
def generar_respuesta(email):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "Eres un asistente útil que genera respuestas a correos."},
            {"role": "user", "content": f"Genera una respuesta para el siguiente correo: {email}"}
        ]
    )
    return response.choices[0].message.content

# Crear la interfaz de Streamlit
st.title("📧 Asistente de Email")

email_input = st.text_area("Escribe tu correo electrónico aquí:", height=300)

col1, col2 = st.columns(2)

with col1:
    if st.button("Resumir Email"):
        if email_input:
            resumen = resumir_email(email_input)
            st.subheader("Resumen del Email:")
            st.write(resumen)
        else:
            st.warning("Por favor, ingresa un correo electrónico para resumir.")

with col2:
    if st.button("Generar Respuesta"):
        if email_input:
            respuesta = generar_respuesta(email_input)
            st.subheader("Respuesta Generada:")
            st.write(respuesta)
        else:
            st.warning("Por favor, ingresa un correo electrónico para generar una respuesta.")
