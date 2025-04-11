#EJERCICIO 1

#En la funcion range incluimos el 101 ya que nos va a incluir hasta el 100 porque el superior no se cuenta
for numero in range(101):
    print(numero)

# EJERCICIO 2

# Solicitar un número entero al usuario
numero = input("Ingresa un número entero positivo: ")

# Asegurarnos de que el número ingresado sea un número entero positivo
if numero.isdigit():
    # Contar la cantidad de dígitos
    cantidad_digitos = len(numero)
    print(f"El número tiene {cantidad_digitos} dígitos.")
else:
    print("Por favor ingresa un número entero válido.")

# EJERCICIO 3

# Solicitar los dos valores al usuario
valor1 = int(input("Ingresa el primer valor: "))
valor2 = int(input("Ingresa el segundo valor: "))

# Asegurarse de que valor1 sea menor que valor2 para que la suma sea correcta
if valor1 < valor2:
    inicio = valor1 + 1
    fin = valor2
else:
    inicio = valor2 + 1
    fin = valor1

# Calcular la suma usando un bucle
suma = 0
for numero in range(inicio, fin):
    suma += numero
suma = sum(range(inicio, fin))

print(f"La suma de los números entre {valor1} y {valor2}, excluyéndolos, es: {suma}")


#EJERCICIO 4

# Inicializamos la suma acumulada
suma_total = 0

# Inicializamos el número con un valor distinto de 0 para entrar al bucle
numero = -1

while numero != 0:
    numero = int(input("Ingresa un número entero (0 para terminar): "))
    if numero != 0:
        suma_total += numero

print(f"La suma total es: {suma_total}")


#EJERCICIO 5

import random

# Generar un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)

# Inicializar contador de intentos
intentos = 0

# Inicializar la adivinanza del usuario
adivinanza = -1

# Bucle de juego
while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1

    if adivinanza < numero_secreto:
        print("El número secreto es más alto.")
    elif adivinanza > numero_secreto:
        print("El número secreto es más bajo.")


print(f"¡Correcto! El número era {numero_secreto}. Lo lograste en {intentos} intento(s).")

#EJERCICIO 6

# Imprimir números pares del 100 al 0 en orden decreciente
print("Números pares del 100 al 0:")

for numero in range(100, -1, -2):
    print(numero)


#EJERCICIO 7

# Solicitar al usuario un número entero positivo
num = int(input("Ingresa un número entero positivo: "))

# Verificar que el número sea positivo
if num >= 0:
    suma = 0
    for i in range(num + 1):
        suma += i
    print(f"La suma de los números entre 0 y {num} es: {suma}")
else:
    print("Por favor, ingresa un número entero positivo.")


#EJERCICIO 8

# Cambia este valor a 100 para el ejercicio final
cantidad_numeros = 100  # Puedes probar con 10 primero

# Inicializar contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Pedir números al usuario
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))

    # Contar pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Contar positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Mostrar resultados
print("\nResumen:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

#EJERCICIO 9

cantidad_numeros = 100 

# Inicializar suma total
suma_total = 0

# Solicitar los números al usuario
for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma_total += numero

# Calcular la media
media = suma_total / cantidad_numeros

# Mostrar el resultado
print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")


#EJERCICIO 10

# Pedir un número entero positivo al usuario
numero = int(input("Ingresa un número entero positivo: "))

# Variable para guardar el número invertido
invertido = 0

# Invertir el número usando un ciclo
while numero > 0:
    digito = numero % 10         # Tomar el último dígito
    invertido = invertido * 10 + digito  # Agregar el dígito al número invertido
    numero = numero // 10        # Quitar el último dígito del número original

# Mostrar el número invertido
print("El número invertido es:", invertido)
