# prueba.ml

# Declaración de variables y operaciones aritméticas
let a = 5
let b = 3
let suma = a + b
let resta = a - b
let multiplicacion = a * b
let division = a / b
let potencia = a ^ b
let raiz = b ^ (1/2)

# Funciones trigonométricas
let seno = sin(a)
let coseno = cos(b)
let tangente = tan(a)

# Operaciones de matrices
let matriz1 = matrix([[1, 2], [3, 4]])
let matriz2 = matrix([[5, 6], [7, 8]])
let sumaMatrices = matriz1.add(matriz2)
let restaMatrices = matriz1.subtract(matriz2)
let multiplicacionMatrices = matriz1.multiply(matriz2)
let transpuesta = matriz1.transpose()
let inversa = matriz1.inverse()

# Condicionales
if (suma > 5) {
    print("La suma es mayor que 5")
} else {
    print("La suma es 5 o menos")
}

# Ciclos
let contador = 0
while (contador < 5) {
    print(contador)
    contador = contador + 1
}

# Gráficos
plotLine([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])

# Manejo de archivos
let texto = readFile("entrada.txt")
writeFile("salida.txt", texto)

# Regresión lineal
let x = [1, 2, 3, 4, 5]
let y = [2, 4, 6, 8, 10]
let regresion = linear_regression(x, y, true)

# Clasificador usando Perceptrón multicapa
let x_train = [[0, 0], [1, 1]]
let y_train = [0, 1]
let perceptron = multilayer_perceptron(x_train, y_train)

# Agrupamiento con K-means
let datos = [[1, 2], [2, 3], [3, 4], [8, 8]]
let kmeans_result = kmeans_clustering(datos, 2, true)
