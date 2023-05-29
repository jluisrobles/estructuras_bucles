#Reto 1
print("------------ RETO 1 ------------")
"""
• Construye un sistema que nos muestra por pantalla todos los números del 1 al 10.
• Después que muestre solo los números pares
• Ahora se desea que se muestre solamente los números impares y que sean divisibles
por 3.
• Constrúyelo de las 2 maneras vista en el día.
• Utilizar los bloques try-except-else-finally para tratar las posibles excepciones que
ocurran.
"""
print ("---------PRIMERA MANERA---------")
try:
    print("Números del 1 al 10:")
    for i in range(1, 11):
        print(i)

    print("Números pares:")
    for i in range(2, 11, 2):
        print(i)

    print("Números impares divisibles por 3:")
    for i in range(1, 11, 2):
        if i % 3 == 0:
            print(i)

except Exception as e:
    print("Se produjo una excepción:", str(e))

else:
    print("El código se ejecutó sin errores.")

finally:
    print("Fin del programa.")

print ("---------SEGUNDA MANERA---------")
try:
    print("Números del 1 al 10:")
    i = 1
    while i <= 10:
        print(i)
        i += 1

    print("Números pares:")
    i = 2
    while i <= 10:
        print(i)
        i += 2

    print("Números impares divisibles por 3:")
    i = 1
    while i <= 10:
        try:
            if i % 2 != 0 and i % 3 == 0:
                print(i)
        except ZeroDivisionError as zde:
            print("Error de división por cero:", str(zde))
        finally:
            i += 1

except Exception:
    print("Se produjo una excepción:")

else:
    print("El código se ejecutó sin errores.")

finally:
    print("Fin del programa.")

#Reto 2
print("------------ RETO 2 ------------")
"""
• Teniendo la siguiente estructura de diccionario siguiente:
persona =
{
"nombre" : string,
"apellido" : string,
"anyoNacimiento" : number,
"aficiones": array of string,
"dni": { "anyoExpedicion" : number,
"lugarNacimento": string},
"colorPelo" : string
}
• Crear una lista denominada personas con 4 diccionarios de tipo persona."""

#la lista de personas
persona1 = {
    "nombre": "José Luis",
    "apellido": "García",
    "anyoNacimiento": 1999,
    "aficiones": ["fútbol", "música", "viajar"],
    "dni": {
        "anyoExpedicion": 2000,
        "lugarNacimiento": "Madrid"
    },
    "colorPelo": "castaño"
}

persona2 = {
    "nombre": "Ana",
    "apellido": "López",
    "anyoNacimiento": 1989,
    "aficiones": ["leer", "cocinar", "caminar"],
    "dni": {
        "anyoExpedicion": 1999,
        "lugarNacimiento": "Tenerife"
    },
    "colorPelo": "castaño"
}

persona3 = {
    "nombre": "Luis",
    "apellido": "Martínez",
    "anyoNacimiento": 1989,
    "aficiones": ["senderismo", "cine", "buceo"],
    "dni": {
        "anyoExpedicion": 2002,
        "lugarNacimiento": "Valencia"
    },
    "colorPelo": "Calvo"
}

persona4 = {
    "nombre": "Laura",
    "apellido": "González",
    "anyoNacimiento": 1987,
    "aficiones": ["yoga", "guitarra", "jardinería"],
    "dni": {
        "anyoExpedicion": 2006,
        "lugarNacimiento": "Sevilla"
    },
    "colorPelo": "pelirrojo"
}


personas = [persona1, persona2, persona3, persona4]

# Mostrar todos los elementos de la lista personas con un bucle for
print("Mostrando personas con bucle for:")
for persona in personas:
    print(persona)

# Mostrar todos los elementos de la lista personas con un bucle while
print("Mostrando personas con bucle while:")
i = 0
while i < len(personas):
    print(personas[i])
    i += 1

# Mostrar los elementos del array persona que cumplan que su año de nacimiento esté entre 1978 y 2000 con un bucle for
print("Personas cuyo año de nacimiento está entre 1978 y 2000 (con bucle for):")
for persona in personas:
    if 1978 <= persona["anyoNacimiento"] <= 2000:
        print(persona)

print("\n")

# Mostrar los elementos del array persona que cumplan que su año de nacimiento esté entre 1978 y 2000 con un bucle while
print("Personas cuyo año de nacimiento está entre 1978 y 2000 (con bucle while):")
i = 0
while i < len(personas):
    if 1978 <= personas[i]["anyoNacimiento"] <= 2000:
        print(personas[i])
    i += 1

# Mostrar un mensaje dependiendo de la edad de cada persona
print("Mensajes según la edad de cada persona:")
for persona in personas:
    edad = 2023 - persona["anyoNacimiento"]
    if 40 >= edad >= 20:
        print("Tu edad está entre 40 y 20 años.")
    else:
        print("Tu edad es menor de 20.")

# Agregar la afición "jugar a la play" a todos los elementos de la lista personas
try:
    for persona in personas:
        persona["aficiones"] = "jugar a la play"

except Exception:
    print("Se produjo una excepción:")

else:
    print("La afición (jugar a la play),se agregó correctamente a todas las personas.")

finally:
    print("Fin del programa.")

#Reto 3
print("------------ RETO 3 ------------")
"""
• Calcular el factorial de un numero dado, primero utilizando la sentencia for y luego con while.
• Dado una lista de números, buscar si existe algún numero de esa lista que sea múltiplo de 2
utilizando la sentencia while.
• Realizar la suma de los 100 primeros números. Utilizar el bucle que mejor se adapte al problema.
• Dado una lista de nombres mostrar el índice de la primera ocurrencia del nombre “Pepe”. Utilizar
el bucle que mejor se adapte al problema.
• Generar dos listas de 100 números aleatorios entre 0 y 20.
• Realizar la suma de los dos listas anteriores.
• Utilizar los bloques try-except-else-finally para tratar las posibles excepciones que ocurran."""
#• Calcular el factorial de un numero dado, primero utilizando la sentencia for
num = 5
factorial = 1
for i in range(1, num+1):
    factorial *= i
print("Factorial de", num, "utilizando for:", factorial)

# Calcular el factorial de un número dado utilizando la sentencia while
num = 5
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print("Factorial de", num, "utilizando while:", factorial)

print()

# Dado una lista de números, buscar si existe algún número que sea múltiplo de 2 utilizando la sentencia while
numeros = [1, 2, 3, 4, 5, 6,7, 8, 9, 10]
i = 0
while i < len(numeros):
    if numeros[i] % 2 == 0:
        print(numeros[i], "es múltiplo de 2")
    i += 1

# Realizar la suma de los 100 primeros números
suma = 0
for i in range(1, 101):
    suma += i
print("La suma de los 100 primeros números es:", suma)

print()

# Dado una lista de nombres, mostrar el índice de la primera ocurrencia del nombre "Pepe"
nombres = ["Juan", "María", "Pepe", "Carlos", "Pepe", "Ana"]
indice_pepe = -1
i = 0
while i < len(nombres):
    if nombres[i] == "Pepe":
        indice_pepe = i
    i += 1
if indice_pepe != -1:
    print("El índice de la primera ocurrencia de 'Pepe' es:", indice_pepe)
else:
    print("'Pepe' no se encuentra en la lista.")

print()

# Generar dos listas de 100 números aleatorios entre 0 y 20
lista1 = []
lista2 = []
numero = 0
contador = 0

while contador < 100:
    numero = (numero + 4) % 21
    lista1.append(numero)
    numero = (numero + 5) % 21
    lista2.append(numero)
    contador += 1
print("Lista 1:", lista1)
print("Lista 2:", lista2)

# Realizar la suma de dos listas
suma = []
lista1 = [2, 4, 6, 8, 10, 12, 14]
lista2 = [3, 5, 7, 9, 11, 13, 15]

suma = []

for i in range(len(lista1)):
    suma += [lista1[i] + lista2[i]]
print("Suma:", suma)

#Utilizar los bloques try-except-else-finally para tratar las posibles excepciones que ocurran.
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except ValueError:
    print("Error: El número no es válido.")
except ZeroDivisionError:
    print("Error: No es posible dividir entre cero.")
else:
    print("El resultado es:", resultado)
finally:
    print("Fin del programa.")