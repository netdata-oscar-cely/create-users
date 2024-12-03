
# Crear Usuarios en Prisma Cloud mediante API

Este proyecto permite crear usuarios de manera masiva en Prisma Cloud utilizando su API. Los datos de los usuarios se leen desde un archivo Excel y el script utiliza Python para automatizar el proceso.

## Estructura del proyecto

```
.
├── main.py                 # Archivo principal para ejecutar el proceso
├── create_users.py         # Módulo para crear usuarios
├── login_cspm.py           # Módulo para autenticación con Prisma Cloud
├── usuarios.xlsx           # Archivo Excel con los datos de los usuarios
├── .env                    # Variables de entorno para la configuración
└── README.md               # Documentación del proyecto
```

## Requisitos previos

- **Python 3.11 o superior**: Asegúrate de tener Python instalado en tu sistema.
- **Credenciales de Prisma Cloud**:
  - `ACCESS_KEY_ID` y `SECRET_KEY` para la autenticación.
  - URL de la API de Prisma Cloud.



## Configuración

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

### 2. Renombrar el archivo `.env.example`

Renombra el archivo `.env.example` a `.env` y ajusta con las siguientes variables de entorno:

```
PRISMA_CLOUD_ACCESS_KEY_ID=<tu_access_key_id>
PRISMA_CLOUD_SECRET_KEY=<tu_secret_key>
PRISMA_CLOUD_API_URL=https://api.prismacloud.io
```

### 3. Instalar de dependencias

Crea el entorno virtual
```bash
python -m venv venv
```

Ubicate ahora sobre el entorno virtual
```bash
source venv/bin/activate
```

Instala las dependencias
```bash
pip install -r requireme
```

### 4. Preparar el archivo Excel

Crea un archivo `usuarios.xlsx` con las siguientes columnas:

| email               | firstName | lastName | roleIds          | defaultRoleId | timeZone     |
|---------------------|-----------|----------|------------------|---------------|--------------|
| user1@example.com   | John      | Doe      | 123456,789012    | 123456        | UTC          |
| user2@example.com   | Jane      | Smith    | 234567           | 234567        | America/Bogota |

- **`roleIds`**: Lista de IDs de roles, separados por comas. Puedes obtener los roles disponibles usando el endpoint `/user/role`.
- **`defaultRoleId`**: Un ID que debe estar incluido en `roleIds`.
- **`timeZone`**: Una zona horaria válida (por ejemplo, `UTC` o `America/Bogota`).

### 5. Obtener roles disponibles (opcional)

Usa el script `get_roles_information.py` para obtener los roles disponibles en tu instancia de Prisma Cloud y guarda el resultado en `info_roles.json`.

## Uso

### Ejecutar el script principal

Para iniciar el proceso de creación de usuarios, ejecuta:

```bash
python main.py
```

El script leerá el archivo `usuarios.xlsx` y creará los usuarios en Prisma Cloud.

## Salida esperada

El script imprimirá el estado de cada usuario creado:

```plaintext
Datos enviados al servidor:
{'email': 'user1@example.com', 'firstName': 'John', 'lastName': 'Doe', 'roleIds': ['123456', '789012'], 'defaultRoleId': '123456', 'timeZone': 'UTC'}
Estado de la respuesta: 200
Usuario user1@example.com creado exitosamente.
```

## Archivos clave

- **`create_users.py`**: Módulo encargado de procesar el archivo Excel y enviar las solicitudes a la API.
- **`login_cspm.py`**: Módulo para autenticación con Prisma Cloud.
- **`usuarios.xlsx`**: Archivo con los datos de los usuarios.
- **`.env`**: Archivo para almacenar credenciales sensibles.

## Personalización

Si deseas agregar más campos o lógica, edita el archivo `create_users.py` según tus necesidades.

## Licencia

Este proyecto es de uso interno y no está licenciado para distribución pública.
