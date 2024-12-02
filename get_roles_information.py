import os
import requests
import json
from dotenv import load_dotenv
from login_cspm import authenticate_prisma_cloud  # Asegúrate de que el módulo de autenticación esté configurado correctamente

# Cargar las variables de entorno
load_dotenv()

# URL del endpoint para obtener los roles de usuario
GET_USER_ROLES_ENDPOINT = f"{os.getenv('PRISMA_CLOUD_API_URL')}/user/role"

def test_get_user_roles():
    # Obtener el token de autenticación
    token = authenticate_prisma_cloud()

    # Configurar encabezados
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Realizar la solicitud GET
    try:
        response = requests.get(GET_USER_ROLES_ENDPOINT, headers=headers)
        print(f"Estado de la respuesta: {response.status_code}")
        if response.status_code == 200:
            roles_data = response.json()

            # Guardar en un archivo JSON
            with open("user_roles.json", "w") as json_file:
                json.dump(roles_data, json_file, indent=4)
            
            print("Los roles de usuario se han guardado en 'user_roles.json'.")
        else:
            print(f"Error al obtener los roles: {response.json()}")
    except Exception as e:
        print(f"Error al probar el endpoint: {e}")

if __name__ == "__main__":
    test_get_user_roles()
