#EJERCICIO 1
# Pedimos al usuario que ingrese su edad y la convertimos a un número entero
edad = int(input("Por favor, ingresa tu edad: "))

# Verificamos si la edad es mayor o igual a 18
if edad >= 18:
    # Si es mayor de edad, mostramos un mensaje en pantalla
    print("Es mayor de edad.")

#EJERCICIO 2
# Pedimos al usuario que ingrese su nota y la convertimos a un número entero
nota = int(input("Por favor, ingresa tu nota: "))

# Verificamos si la nota es mayor o igual a 6
if nota >= 6:
    # Si la nota es 6 o más, mostramos el mensaje "Aprobado"
    print("Aprobado")
else:
    # Si la nota es menor a 6, mostramos el mensaje "Desaprobado"
    print("Desaprobado")

#EJERCICIO 3
# Pedimos al usuario que ingrese un número y lo convertimos a un entero
numero = int(input("Por favor, ingrese un número par: "))

# Verificamos si el número es par usando el operador módulo (%)
if numero % 2 == 0:
    # Si el residuo de la división por 2 es 0, significa que es un número par
    print("Ha ingresado un número par")
else:
    # Si el residuo no es 0, significa que el número es impar
    print("Por favor, ingrese un número par")

#EJERCICIO 4
# Pedimos al usuario que ingrese su edad y la convertimos a un número entero
edad = int(input("Por favor, ingresa tu edad: "))

# Verificamos a qué categoría pertenece según su edad
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#EJERCICIO 5
# Pedimos al usuario que ingrese una contraseña
contraseña = input("Por favor, ingrese una contraseña (entre 8 y 14 caracteres): ")

# Verificamos si la longitud de la contraseña está dentro del rango permitido usando len()
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#EJERCICIO 6
# Importamos el módulo random para generar números aleatorios
import random  

# Importamos las funciones estadísticas necesarias
from statistics import mode, median, mean  

# Generamos una lista con 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos la moda, la mediana y la media de la lista
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Mostramos los valores calculados
print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

# Determinamos el tipo de sesgo según los criterios dados
if media > mediana > moda:
    print("La distribución tiene sesgo positivo (a la derecha).")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo (a la izquierda).")
else:
    print("La distribución no tiene sesgo.")

#EJERCICIO 7
# Pedimos al usuario que ingrese una frase o palabra
texto = input("Ingrese una frase o palabra sin mayusculas: ")

# Definimos las vocales
vocales = "aeiou"

# Verificamos si el último carácter del texto es una vocal
if texto[-1] in vocales:

# Imprimimos el resultado
    print("Resultado:", texto)

#EJERCICIO 8
# Pedimos al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")

# Pedimos al usuario que elija una opción
print("Elija una opción:")
print("1 - Nombre en mayúsculas")
print("2 - Nombre en minúsculas")
print("3 - Nombre con la primera letra en mayúscula")
opcion = input("Ingrese el número de la opción deseada (1, 2 o 3): ")

# Aplicamos la transformación según la opción elegida
if opcion == "1":
    resultado = nombre.upper()  # Convierte el nombre a mayúsculas
elif opcion == "2":
    resultado = nombre.lower()  # Convierte el nombre a minúsculas
elif opcion == "3":
    resultado = nombre.title()  # Convierte la primera letra en mayúscula
else:
    resultado = "Opción inválida, por favor ingrese 1, 2 o 3."

# Imprimimos el resultado
print("Resultado:", resultado)

#EJERCICIO 9
# Pedimos al usuario que ingrese la magnitud del terremoto y la convertimos a un número decimal
magnitud = float(input("Ingrese la magnitud del terremoto según la escala de Richter: "))

# Clasificamos la magnitud en una categoría según la escala de Richter
if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif magnitud >= 3 and magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif magnitud >= 4 and magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif magnitud >= 5 and magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif magnitud >= 6 and magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else: 
    magnitud >= 7
    categoria = "Extremo (puede causar graves daños a gran escala)"

# Imprimimos la clasificación correspondiente
print("Clasificación del terremoto:", categoria)

#EJERCICIO 10
# Pedimos al usuario que ingrese el hemisferio en el que se encuentra
hemisferio = input("Ingrese el hemisferio en el que se encuentra (N para Norte / S para Sur): ").strip().upper()

# Pedimos al usuario que ingrese el mes y el día
mes = int(input("Ingrese el número del mes (1 para enero, 2 para febrero, ..., 12 para diciembre): "))
dia = int(input("Ingrese el día del mes: "))

# Verificamos que el mes y el día sean válidos
if mes < 1 or mes > 12 or dia < 1 or dia > 31:
    print("Fecha inválida. Por favor, ingrese un mes (1-12) y un día válido (1-31).")
else:
    # Determinamos la estación según el hemisferio y la fecha
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    else:  # (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20)
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"

    # Imprimimos la estación correspondiente al hemisferio ingresado
    if hemisferio == "N":
        print(f"En el hemisferio norte, la estación es: {estacion_norte}")
    elif hemisferio == "S":
        print(f"En el hemisferio sur, la estación es: {estacion_sur}")
    else:
        print("Hemisferio inválido. Por favor, ingrese 'N' para Norte o 'S' para Sur.")

