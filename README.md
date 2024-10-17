# Parcial Lenguajes Corte 2

* Daniel Oviedo

---

Instalar requerimientos necesarios para el funcionamiento del codigo

* pip install requirements.txt

Instalar la ultima version de antlr (en caso de no tenerla descargada o que no se descargue junto al codigo)

* curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar

## Punto 1

En terminal


* java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor complejos.g4

* python3 calculadoraComplejos.py

Ingresar operacion a realizar

## Punto 2

En terminal

* antlr4 -Dlanguage=Python3 -visitor appFuncion.g4

* python3 funcionMapFilter.py input.txt

Ingresar una liste de numeros separados por espacio. Ej: 1 2 3 4 5

Funciones Soportadas (Modificar este valor en el archivo input.txt)

MAP:

* square: Eleva cada número al cuadrado.
* cube: Eleva cada número al cubo.
* double: Multiplica cada número por 2.
* neg: Convierte cada número en su opuesto.
* even_to_zero: Convierte números pares a cero.
* is_prime: Verifica si cada número es primo.

FILTER:

* par: Filtra los números pares.
* impar: Filtra los números impares.
* sort: Ordena los números de menor a mayor.
* reverseSort: Ordena los números de mayor a menor.

## Punto 3

En terminal

* java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor transformadas.g4

* python3 transform.py

Modificar a gusto el archivo input.txt para probar diferentes transformaciones

Casos de uso:

* fourier([3 + 4i, 1 - 2i, 0 + 1i], 3)

* inversa([1 + 0i, 0 + 0i, 2 + 0i], 3)

* pulsoRectangular(1.0)

* pulsoTriangular(1.0)

* signum()

* deltaDirac()

* cos(5.0)

* sin(5.0)