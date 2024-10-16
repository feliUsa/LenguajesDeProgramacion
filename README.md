# Parcial Lenguajes Corte 2

* Daniel Oviedo

---

Instalar requerimientos necesarios para el funcionamiento del codigo

* pip install requirements.txt

## Punto 1

En terminal

* antlr4 -Dlanguage=Python3 -visitor Calc.g4

* python3 calculadora.py

Ingresar operacion a realizar

## Punto 2

En terminal

* antlr4 -Dlanguage=Python3 -visitor MapFilter.g4

* python3 interpreter.py input.txt

Ingresar una liste de numeros separados por espacio. Ej: 1 2 3 4 5


Funciones Soportadas (Modificar este valor en el archivo input.txt)

MAP:

* square: Eleva cada número al cuadrado.
* cube: Eleva cada número al cubo.
* double: Multiplica cada número por 2.
* negate: Convierte cada número en su opuesto.
* even_to_zero: Convierte números pares a cero.
* is_prime: Verifica si cada número es primo.

FILTER:

* even: Filtra los números pares.
* odd: Filtra los números impares.
* asc: Ordena los números de menor a mayor.
* desc: Ordena los números de mayor a menor.

## Punto 3