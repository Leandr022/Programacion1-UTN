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
    # Sumar los números entre valor1 y valor2, excluyendo ambos
    suma = sum(range(valor1 + 1, valor2))  # Usamos valor1 + 1 para excluir valor1 y valor2 para excluir valor2
    print(f"La suma de los números entre {valor1} y {valor2} es: {suma}")
else:
    print("El primer valor debe ser menor que el segundo valor.")


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
