from faker import Faker

fake = Faker()

lista = {}

# Genera 15 usuarios con datos falsos y los almacena en un diccionario
for i in range(1, 16):
    lista[i] = {
        "nombre": fake.first_name(),
        "direccion": fake.address(),
        "correo": fake.email(),
        "telefono": fake.phone_number(),
    }

# Muestra los datos de cada usuario en la consola
for usuario in lista:
    print(f"Usuario {usuario}:")
    print(f"Nombre: {lista[usuario]['nombre']}")
    print(f"Dirección: {lista[usuario]['direccion']}")
    print(f"Correo: {lista[usuario]['correo']}")
    print(f"Teléfono: {lista[usuario]['telefono']}\n")

# Genera un número aleatorio entre 1 y 15, aprovechando la función random_int de Faker
numero_aleatorio = fake.random_int(min=1, max=15)

# Muestra el nombre del usuario afortunado en la consola
print(f"O usuario chamado {lista[numero_aleatorio]['nombre']} foi o afortunado!")
