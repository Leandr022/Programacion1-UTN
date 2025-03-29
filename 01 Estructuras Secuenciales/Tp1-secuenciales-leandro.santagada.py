#EJERCICIO 1
# En la siguiente linea se imprime el mensaje en la pantalla 

print("Hola Mundo!")


#EJERCICIO 2
# Pedir al usuario que ingrese su nombre y se guarda la respuesta en la variable "nombre"
nombre = input("Ingrese su nombre: ")

# Imprimir el saludo personalizado
print(f"Hola {nombre}!")

#EJERCICIO 3
# Pedir datos al usuario en cuatro variables como "nombre","apellido", "edad", "residencia" donde por separado se guarda su respuesta
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

# Imprimir la oración con los datos ingresados
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#EJERCICIO 4

# Pedir al usuario el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Ingresamos el valor de pi
pi= 3.14159

# Calcular el área y el perímetro
area = pi * radio**2  # Fórmula: π * r²
perimetro = 2 * pi * radio  # Fórmula: 2 * π * r

# Imprimir los resultados
print(f"Para un círculo de radio:{radio}")
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")


#EJERCICIO 5

# Pedir al usuario una cantidad de segundos
segundos = int(input("Ingrese la cantidad de segundos: "))

# Calcular las horas equivalentes
horas = segundos / 3600  # 1 hora = 3600 segundos

# Imprimir el resultado
print(f"{segundos} segundos equivalen a {horas} horas.")

#EJERCICIO 6

# Pedir al usuario un número entero y lo guardamos en la variable "numero"
numero= int (input("Introduzca un numero:"))

# Realizamos las multiplicaciones correspondientes
numero_por_0 = numero * 0
numero_por_1 = numero * 1
numero_por_2 = numero * 2
numero_por_3 = numero * 3
numero_por_4 = numero * 4
numero_por_5 = numero * 5
numero_por_6 = numero * 6
numero_por_7 = numero * 7
numero_por_8 = numero * 8
numero_por_9 = numero * 9
numero_por_10 = numero * 10

# Imprimimos el resultado por pantalla. En este caso hacemos una impresión de varias líneas por lo que usamos comillas triples
print(f"""
  {numero} x 0 = {numero_por_0}
  {numero} x 1 = {numero_por_1}
  {numero} x 2 = {numero_por_2}
  {numero} x 3 = {numero_por_3}
  {numero} x 4 = {numero_por_4}
  {numero} x 5 = {numero_por_5}
  {numero} x 6 = {numero_por_6}
  {numero} x 7 = {numero_por_7}
  {numero} x 8 = {numero_por_8}
  {numero} x 9 = {numero_por_9}
  {numero} x 10 = {numero_por_10}
    """)

#EJERCICIO 7

# Pedir al usuario dos números enteros distintos de 0
num1 = int(input("Ingrese el primer número entero (distinto de 0): "))
num2 = int(input("Ingrese el segundo número entero (distinto de 0): "))

#Realizamos las operaciones que almacenamos con las respuestas a las variables "num1" y "num2"
suma= num1 + num2
resta= num1 - num2
division= round(num1 / num2)
multiplicacion= num1 * num2

#Imprimimos el resultado por pantalla de cada operacion realizada
print (f""" 
      Resultado de la suma: {suma}
      Resultado de la resta: {resta}
      Resultado de la division: {division}
      Resultado de la multiplicacion: {multiplicacion} """)


#EJERCICIO 8
# Pedir al usuario su peso en kilogramos y altura en metros
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el Índice de Masa Corporal (IMC)
imc = peso / (altura ** 2, 2)

# Imprimir el resultado
print(f"Su Índice de Masa Corporal (IMC) es: {imc}")


#EJERCICIO 9

# Pedir al usuario la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Calcular la temperatura equivalente en grados Fahrenheit
fahrenheit = (9 / 5) * celsius + 32

# Imprimir el resultado
print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}°F")

#EJERCICIO 10

# Pedir al usuario 3 números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Calcular el promedio
promedio = (numero1 + numero2 + numero3) / 3

# Imprimir el resultado
print(f"El promedio de los tres números es: {promedio:.2f}")
