import requests
import socket

def doxxear_ip():
    ip = input("Ingrese la dirección IP a doxxear: ")
    respuesta = requests.get(f"https://ipinfo.io/{ip}")
    if respuesta.status_code == 200:
        data = respuesta.json()
        print("Información sobre la IP:")
        print(f"País: {data['country']}")
        print(f"Región: {data['region']}")
        print(f"Ciudad: {data['city']}")
        print(f"Organización: {data['org']}")
    else:
        print("Error al obtener información de la IP.")

def ver_informacion_ip():
    ip = socket.gethostbyname(socket.gethostname())
    respuesta = requests.get(f"https://ipinfo.io/{ip}")
    if respuesta.status_code == 200:
        data = respuesta.json()
        print("Información sobre tu IP:")
        print(f"País: {data['country']}")
        print(f"Región: {data['region']}")
        print(f"Ciudad: {data['city']}")
        print(f"Organización: {data['org']}")
    else:
        print("Error al obtener información de tu IP.")

while True:
    print("Elegir una opción:")
    print("1. Doxxear una IP")
    print("2. Ver información de tu IP")
    print("3. Salir")
    opcion = input("Ingrese el número de la opción: ")
    if opcion == "1":
        doxxear_ip()
    elif opcion == "2":
        ver_informacion_ip()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
