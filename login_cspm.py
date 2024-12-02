import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Carga las variables de entorno desde el archivo .env

def authenticate_prisma_cloud():
    # Carga las credenciales desde variables de entorno
    ACCESS_KEY_ID = os.getenv('PRISMA_CLOUD_ACCESS_KEY_ID')
    SECRET_KEY = os.getenv('PRISMA_CLOUD_SECRET_KEY')
    API_URL = os.getenv('PRISMA_CLOUD_API_URL', 'https://api.prismacloud.io')  # URL predeterminada

    if not ACCESS_KEY_ID or not SECRET_KEY:
        raise EnvironmentError("Faltan las variables de entorno 'PRISMA_CLOUD_ACCESS_KEY_ID' o 'PRISMA_CLOUD_SECRET_KEY'.")

    # Endpoint de inicio de sesión
    LOGIN_ENDPOINT = f'{API_URL}/login'

    # Datos de autenticación
    auth_data = {
        'username': ACCESS_KEY_ID,
        'password': SECRET_KEY
    }

    # Realiza la solicitud POST para obtener el token JWT
    response = requests.post(LOGIN_ENDPOINT, json=auth_data)
    response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx

    # Extrae y devuelve el token JWT
    jwt_token = response.json().get('token')
    if jwt_token:
        return jwt_token
    else:
        raise ValueError('No se pudo obtener el token JWT. Verifica tus credenciales.')
