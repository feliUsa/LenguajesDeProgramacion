# Integrantes del grupo

Andres Vasquez

Daniel Oviedo

# Pasos para compilación del codigo

1. Descargar el codigo
2. Descomprimir el codigo
3. En la terminal
4. Meterse a la carpeta deseada programaLex/punto#

## Punto1

Modificar el archivo txt para poder realizar combinaciones de caracteres

1. flex contadorCaracteres.l
2. gcc lex.yy.c -o palabras -lfl
3. ./palabras

## Punto2

En el txt2 se encuentra la lista de palabras permitidas por el analizador

1. flex contadorCaracteres.l
2. gcc lex.yy.c -o palabras -lfl
3. echo "palabras a traducir" | ./traductor

## Punto3

1. flex contadorCaracteres.l
2. gcc lex.yy.c -o palabras -lfl
3. echo "operacion separada por espacios" | ./calcular

ejemplo operación: 5 + 3 * 2 ^ 4 = 53

## Punto4

En el txt4 se encuentran los tokens aceptados por el analizador

1. flex contadorCaracteres.l
2. gcc lex.yy.c -o palabras -lfl
3. echo "tokens separados por espacios" | ./tokens

## Punto5

1. flex contadorCaracteres.l
2. gcc lex.yy.c -o palabras -lfl
3. echo "operaciones con numeros complejos separados por espacios" | ./identificar