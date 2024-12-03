# Integrantes

* Daniel Oviedo
* Sara Villanueva
* Andres Vazquez

Construcción de DSL (Lenguaje de dominio específico para realizar procesos de Machine Learning)


1. Descargar codigo e ingresar a la carpeta en la terminal

2. Modificar archivo prueba.mlang a gusto

3. Ingresar en consola:

    * (opcion 1) antlr4 -Dlanguage=Python3 -visitor -o antlr_generated MLanguaje.g4

    * (opcion 2) java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o antlrEjecucion MLanguaje.g4

    * python3 main.py prueba.mlang


---

# Casos de Uso

1. Declaraciones de variables

let variable

2. Mostrar mensajes por consola

print("mensaje")

3. Operaciones aritméticas

let x = 10 + 5
let y = sin(x) * 2
print(y)

4. Operaciones con matrices

let A = matrix([[1, 2], [3, 4]])
let B = matrix([[5, 6], [7, 8]])
let C = A.add(B)
print(C)

5. Declaraciones condicionales

if (x > 10) {
    print("x es mayor que 10")
} else {
    print("x es 10 o menor")
}

6. Bucles

let i = 0
while (i < 5) {
    print(i)
    let i = i + 1
}

7. Grafico lineal o de barras

let x = [1, 2, 3, 4, 5]
let y = [2, 4, 6, 8, 10]
plotLine(x, y) || plotBar(x, y)

8. Operaciones con archivos

writeFile("salida.txt", "Este es un texto de ejemplo")
let data = readFile("salida.txt")
print(data)

9. Modelo de regresión

let x_train = [[1], [2], [3], [4]]
let y_train = [2, 4, 6, 8]
linear_regression(x_train, y_train)

10. Clasificador de perceptrón multicapa

let x_train = [[0, 0], [1, 1], [1, 0], [0, 1]]
let y_train = [0, 1, 1, 0]
multilayer_perceptron(x_train, y_train)

11. Agrupamiento con K-means

let data = [[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]]
kmeans_clustering(data, 2)

Basarse en el archivo ejemplo.ml para modificar test.ml