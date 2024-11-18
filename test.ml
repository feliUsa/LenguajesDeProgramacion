# Declaración de matrices
let matriz1 = matrix([[1, 2], [3, 4]])
let matriz2 = matrix([[5, 6], [7, 8]])

# Operaciones con matrices
let matrizSuma = matriz1 + matriz2
let matrizTranspuesta = matriz1.transpose()
print(matrizSuma)
print(matrizTranspuesta)

# Condicional
let suma = 5 + 3
if (suma > 5) {
    print("La suma es mayor que 5")
} else {
    print("La suma es 5 o menor")
}

# Ciclo
let i = 0
while (i < 3) {
    print(i)
    let i = i + 1
}


# Graficación
let x = [1, 2, 3, 4, 5]
let y = [2, 4, 6, 8, 10]
plotLine(x, y)

# Clasificación
let x_train = [[0, 0], [1, 1], [2, 2]]
let y_train = [0, 1, 1]
multilayer_perceptron(x_train, y_train)

# Agrupamiento
let datos = [[1, 2], [3, 4], [5, 6]]
kmeans_clustering(datos, 2, true)
