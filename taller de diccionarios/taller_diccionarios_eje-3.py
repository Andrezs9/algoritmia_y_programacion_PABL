usuarios = {
    "iperurena": {
        "nombre": "Iñaki" ,
            "apellido": "Perurena",
            "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
    }
}

for i in range(3):
    usuario = input("ingrese usuario: ")
    contraseña = input("ingrese contraseña: ")
    if usuario in usuarios and usuarios[usuario]["password"] == contraseña:
        print(f"{usuarios[usuario]["nombre"]} {usuarios[usuario]["apellido"]}")