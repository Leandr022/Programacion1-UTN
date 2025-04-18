#EJERCICIO 1

# Definición de la función
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Llamada a la función desde el programa principal
imprimir_hola_mundo()


#EJERCICIO 2

# Definición de la función
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
nombre_usuario = input("¿Cuál es tu nombre? ")  # Solicitar nombre al usuario
saludo = saludar_usuario(nombre_usuario)  # Llamar a la función con el nombre ingresado
print(saludo)  # Mostrar el saludo personalizado


#EJERCICIO 3

# Definición de la función
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nombre_usuario = input("¿Cuál es tu nombre? ")
apellido_usuario = input("¿Cuál es tu apellido? ")
edad_usuario = input("¿Cuántos años tienes? ")
residencia_usuario = input("¿Dónde vives? ")

# Llamada a la función con los datos ingresados
informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)


#EJERCICIO 4

PI= 3.14

# Función para calcular el área del círculo
def calcular_area_circulo(radio):
    return PI * radio**2

# Función para calcular el perímetro del círculo
def calcular_perimetro_circulo(radio):
    return 2 * PI * radio

# Programa principal
radio_usuario = float(input("¿Cuál es el radio del círculo? "))

# Llamar a ambas funciones con el radio ingresado
area = calcular_area_circulo(radio_usuario)
perimetro = calcular_perimetro_circulo(radio_usuario)

# Mostrar los resultados
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")


#EJERCICIO 5

# Función para convertir segundos a horas
def segundos_a_horas(segundos):
    horas = segundos // 3600  # 1 hora = 3600 segundos
    return horas

# Programa principal
segundos_usuario = int(input("¿Cuántos segundos quieres convertir a horas? "))

# Llamar a la función con los segundos ingresados
horas = segundos_a_horas(segundos_usuario)

# Mostrar el resultado
print(f"{segundos_usuario} segundos equivalen a {horas} horas.")

#EJERCICIO 6

# Función para imprimir la tabla de multiplicar de un número
def tabla_multiplicar(numero):
    for i in range(1, 11):  # Itera desde 1 hasta 10
        print(f"{numero} x {i} = {numero * i}")

# Programa principal y lamar a la función con el número ingresado
numero_usuario = int(input("¿De qué número quieres la tabla de multiplicar? "))
tabla_multiplicar(numero_usuario)


#EJERCICIO 7

# Función para realizar las operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # Comprobamos si el segundo número es 0 antes de dividir para evitar error de división por cero
    if b != 0:
        division = a / b
    else:
        division = "Error: División por cero"
    
    return (suma, resta, multiplicacion, division)

# Programa principal
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

# Llamar a la función con los números ingresados
suma,resta,multiplicacion,division = operaciones_basicas(a, b)

# Mostrar los resultados de manera clara
print(f"\nResultados de las operaciones con {a} y {b}:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


#EJERCICIO 8

# Función para calcular el IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)  # Fórmula del IMC
    return imc

# Programa principal
peso_usuario = float(input("¿Cuál es tu peso en kilogramos? "))
altura_usuario = float(input("¿Cuál es tu altura en metros? "))

# Llamar a la función con los datos ingresados
imc = calcular_imc(peso_usuario, altura_usuario)

# Mostrar el resultado con dos decimales
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")


#EJERCICIO 9

# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32  # Fórmula de conversión
    return fahrenheit

# Programa principal
celsius_usuario = float(input("¿Cuál es la temperatura en grados Celsius? "))

# Llamar a la función con la temperatura ingresada
fahrenheit = celsius_a_fahrenheit(celsius_usuario)

# Mostrar el resultado
print(f"{celsius_usuario} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")


#EJERCICIO 10

# Función para calcular el promedio de tres números
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3  # Fórmula para calcular el promedio
    return promedio

# Programa principal
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

# Llamar a la función con los tres números ingresados
promedio = calcular_promedio(a, b, c)

# Mostrar el resultado con dos decimales
print(f"El promedio de los tres números es: {promedio:.2f}")
