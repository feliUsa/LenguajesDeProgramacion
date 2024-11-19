# Muchas expresiones (se demora mucho)

# 1. Declaraciones de variables

let variable = "hola mundo"

# 2. Mensajes por consola

print(variable)

# 3. Operaciones aritméticas
print("=== Pruebas de Operaciones Aritméticas ===")
let a = 10 + 5
let b = a * 2
let c = b / 3
let d = sin(c)
print(a)
print(b)
print(c)
print(d)

# 4. Operaciones con matrices
print("=== Pruebas de Operaciones con Matrices ===")
let A = matrix([[1, 2], [3, 4]])
let B = matrix([[5, 6], [7, 8]])
let C = A.add(B)
let D = A.multiply(B)
let E = A.transpose()
print(C)
print(D)
print(E)

# 5. Declaraciones condicionales
print("=== Pruebas de Declaraciones Condicionales ===")
let x = 15
if (x > 10) {
    print("x es mayor que 10")
} else {
    print("x es 10 o menor")
}
let y = 5
if (y > 10) {
    print("y es mayor que 10")
} else {
    print("y es 10 o menor")
}

# 6. Bucles
print("=== Pruebas de Bucles While ===")
let i = 0
while (i < 5) {
    print(i)
    let i = i + 1
}

print("=== Pruebas de Bucles For ===")
for (let j = 0; j < 5; j = j + 1) {
    print(j)
}

# 7. Visualización de datos
print("=== Pruebas de Visualización de Datos ===")
let x_vals = [1, 2, 3, 4, 5]
let y_vals = [2, 4, 6, 8, 10]
plotLine(x_vals, y_vals)

let y_vals_bar = [5, 7, 9, 11, 13]
plotBar(x_vals, y_vals_bar)

# 8. Operaciones con archivos
print("=== Pruebas de Operaciones con Archivos ===")
writeFile("test_output.txt", "Hola, este es un texto de prueba")
let file_content = readFile("test_output.txt")
print(file_content)

# 9. Modelo de regresión
print("=== Pruebas de Modelo de Regresión Lineal ===")
let x_train = [[1], [2], [3], [4]]
let y_train = [2, 4, 6, 8]
linear_regression(x_train, y_train)

# 10. Clasificador de perceptrón multicapa
print("=== Pruebas de Clasificador Perceptrón Multicapa ===")
let x_train_mlp = [[0, 0], [1, 1], [1, 0], [0, 1]]
let y_train_mlp = [0, 1, 1, 0]
multilayer_perceptron(x_train_mlp, y_train_mlp)

# 11. Agrupamiento con K-Means
print("=== Pruebas de Agrupamiento K-Means ===")
let data_kmeans = [[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]]
kmeans_clustering(data_kmeans, 2)
