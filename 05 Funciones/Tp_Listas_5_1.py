#EJERCICIO 1

# Crear la lista de múltiplos de 4 entre 1 y 100
multiplos_de_4 = list(range(4, 101, 4))

# Mostrar la lista
print(multiplos_de_4)

#EJERCICIO 2

# Crear la lista con cinco elementos
cosas_que_me_gustan = ["hamburguesa", "videojuegos", "música", "padel", "café"]

# Mostrar el penúltimo elemento usando indexing negativo
penultimo = cosas_que_me_gustan[-2]

# Imprimir el penúltimo elemento
print("El penúltimo elemento es:", penultimo)


#EJERCICIO 3

# Crear una lista vacía
lista_vacia = []

# Agregar tres palabras usando append
lista_vacia.append("Python")
lista_vacia.append("Aprender")
lista_vacia.append("Programacion1")

# Imprimir la lista resultante
print("Lista resultante:", lista_vacia)

#EJERCICIO 4

# Lista original
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazar el segundo valor (índice 1) por "loro"
animales[1] = "loro"

# Reemplazar el último valor (índice -1) por "oso"
animales[-1] = "oso"

# Imprimir la lista modificada
print("Lista actualizada:", animales)


#EJERCICIO 5 

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# Este ejercicio lo que nos plantea es que con la variable numeros, 
# presenta una lista con 5 elementos, luego con la funcion .remove
# busca dentro de la lista el numero más alto y lo elimina
# para volver a imprimir la lista sin ese numero anteriormente sacado de la lista


#EJERCICIO 6

# Crear la lista con saltos de 5
numeros = list(range(10, 31, 5))

# Mostrar los dos primeros elementos
print("Los dos primeros números son:", numeros[:2])


#EJERCICIO 7

# Lista original
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazo de los dos valores centrales
autos[1:3] = ["mustang", "camaro"]

# Imprimir lista modificada
print("Lista actualizada:", autos)


#EJERCICIO 8

# Crear lista vacía
dobles = []

# Agregar el doble de los valores usando append directamente
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Imprimir la lista resultante
print("Lista de dobles:", dobles)


#EJERCICIO 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines"
compras[1][1] = "tallarines"

# c) Eliminar "pan" del primer cliente
compras[0].remove("pan")

# d) Imprimir resultado
print("Lista de compras actualizada:", compras)


#EJERCICIO 10

# Crear la lista anidada
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

# Imprimir la lista
print("Lista anidada:", lista_anidada)


