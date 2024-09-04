# Parcial Lenguajes de Programación

* Daniel Felipe Oviedo Trujillo

---

## Para el funcionamiento del codigo

* Tener descargado **FLEX** (sudo apt-get install flex)

* Tener descargado **ANTLR4** (pip install antlr4-python3-runtime)

    * Para este proyecto se utilizo la version de python de antlr

* Descargar y descomprimir el código

* Ingresar a la carpeta deseada

## Punto 1

* Modificar a gusto el archivo token.txt

* Ejecutar en terminal:

    * ./token.awk token.txt

* Asegurarse de que el archivo .awk sea un ejecutable, en caso de que no sea un ejecutable, antes de ejecutar el paso anterior, colocar en terminal: **chmod +x token.awk**

## Punto 2

* Modificar a gusto el archivo archivo.txt

* Verificar que **FLEX** este descargado (Remitirse a numerales anteriores)

* Ejecutar en terminal:

    * flex lambda.l
    * gcc lex.yy.c -o lambda
    * /.lambda archivo.txt

## Punto 3

* Modificar a gusto el archivo key.txt

* Ejecutar en terminal

    * gcc miprograma.c -o miprograma
    * ./miprograma key.txt palabraABuscar

## Punto 4

* Para correr el codigo C

    * gcc main.c -o tiempoC
    * ./tiempoC

* Para correr el codigo python

    * python3 main.py

## Punto 5

* Modificar el archivo expr.in a gusto

* Verificar que **ANTLR4** es decargado (Remitirse a numerales anteriores)

* Ejecutar en terminal

    * antlr4 -Dlanguage=Python3 Trig.g4 -visitor
    * python3 TrigCalculator.py expr.in




