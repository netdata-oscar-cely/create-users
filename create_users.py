import os
import pandas as pd
import requests
from dotenv import load_dotenv
from login_cspm import authenticate_prisma_cloud  # Asegúrate de que el módulo de autenticación esté configurado correctamente

# Cargar variables de entorno
load_dotenv()

# URL del endpoint para agregar usuarios
ADD_USER_ENDPOINT = f"{os.getenv('PRISMA_CLOUD_API_URL')}/v3/user"

# Función para crear un solo usuario
def create_user(token, user_data):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Imprimir los datos enviados al servidor para depuración
    print("Datos de la solicitud:")
    print(user_data)

    response = requests.post(ADD_USER_ENDPOINT, headers=headers, json=user_data)
    print(f"Estado de la respuesta: {response.status_code}")

    # Manejo de respuestas
    if response.status_code in [200, 201]:
        print(f"Usuario {user_data['email']} creado exitosamente.")
    else:
        print(f"Error al crear el usuario {user_data['email']}: {response.status_code}, {response.text}")

# Función para procesar y crear usuarios desde un archivo Excel
def create_users_from_excel(file_path):
    # Obtener el token JWT
    token = authenticate_prisma_cloud()

    # Leer el archivo Excel
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return

    # Validar que el archivo tiene las columnas necesarias
    required_columns = {'email', 'firstName', 'lastName', 'roleIds', 'defaultRoleId', 'timeZone'}
    if not required_columns.issubset(df.columns):
        print(f"El archivo Excel debe contener las columnas: {required_columns}")
        return

    # Iterar sobre cada fila del Excel y crear usuarios
    for _, row in df.iterrows():
        try:
            # Validar que roleIds es una lista y defaultRoleId está en roleIds
            role_ids = [rid.strip() for rid in row['roleIds'].split(',')]

            if row['defaultRoleId'] not in role_ids:
                print(f"Error: defaultRoleId {row['defaultRoleId']} no está en roleIds {role_ids} para el usuario {row['email']}")
                continue

            user_data = {
                "email": row['email'],
                "firstName": row['firstName'],
                "lastName": row['lastName'],
                "roleIds": role_ids,
                "defaultRoleId": row['defaultRoleId'],
                "timeZone": row['timeZone']
            }

            # Crear el usuario
            create_user(token, user_data)

        except Exception as e:
            print(f"Error al procesar al usuario {row['email']}: {e}")

