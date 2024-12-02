from create_users import create_users_from_excel

def main():
    excel_file_path = "usuarios.xlsx"
    try:
        create_users_from_excel(excel_file_path)
    except Exception as e:
        print(f"Error al ejecutar el proceso de creación de usuarios: {e}")

if __name__ == "__main__":
    main()