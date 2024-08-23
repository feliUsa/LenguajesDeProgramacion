# Uso de BISON para Ejecutar una Calculadora

---

**Integrantes**

* Andres Vasquez
* Daniel Oviedo

---

## ¿Como correr el código?

1. Descargar el proyecto
2. Descomprimir el archivo.zip
3. En la terminal
    a. Ingresar a la carpeta Example_Bison
    b. bison -d p1.y
    c. flex p1.l
    d. gcc p1.tab.c lex.yy.c -o nombreEjecutable -lfl
    ./nombreEjecutable
4. Realizar las pruebas funcionales de la calculadora

---

## Explicación

### 1. **Tokenización**: Describa cómo el lexer divide la expresión de entrada en tokens y cómo se utilizan estos tokens en el proceso de análisis.

En primer lugar, se definen los toquens de entrada y estos se asocian con un patron especifico (expresión regular).
Estos tokens se definen en el archivo ***p1.l*** en donde se definen las reglas de tokenización, es decir, se comentan que digitos se van a reconocer. Esta tokenización la realiza flex.

Por otra parte, en el archivo ***p1.y***, se define la gramática y como los tokens se van a organizr para formar expresiones aceptadas. En primer lugar se declaran los tokens que van a ser usados, para luego definir las reglas de como se van a combinar esos tokens para formar las expresiones.

Para el funcionamiento de la calculadora, cada vez que bison necesita un token, se llama a la funcion ***yylex***, flex analiza la entrada y devuelve a bison un token basado en los patrones definidos anteriormente. Por parte de bison, el recibe estos tokens y los usa segun la gramatica definida para construir las expresiones validas

### 2. **Análisis**: Explique el proceso de análisis de los tokens para crear un árbol de sintaxis y cómo se usa el árbol de sintaxis para evaluar la expresión.

Partiendo de lo comentado anteriormente, bison recive los tokens generados por flex, para posteriormente, construir un arbol de sintaxis. El arbol de sintaxis representa jerarquicamente la estructura de las expresiones matematicas segun las reglas definidas previamente en el archivo ***p1.y***. 

En este caso, si bison recibe un *expression* seguido de alguna expresion matematica ('+', '-', '\ast', '/') seguido de otro *expression*, se considerará que se ha encontrado una expresion matematica.

Para la construcción del arbol de sintaxis, la estructura de las reglas de produccion y el uso de '$$', '$1', '$2', etc., define la jerarquia de la expresion.

Cuando ya se aplicaron las reglas para toda la entrada, se obtiene el valor final, el cual es el resultado de evaluar la expresion segun el arbol de sintaxis implicito. Obteniendo de esta manera, la respuesta.


### 3. **Evaluación**: Discuta cómo se evalúa la expresión utilizando el árbol de sintaxis y cómo la calculadora produce el resultado final.

La evaluación de la expresion en la calculadora, se realiza al tiempo mientras que se construye el arbol de sintaxis, es decir, a medida que se aplican las reglas de produccion de bison, se crea el arbol.

La reglas de produccion en bison, no solo se agrupan los tokens, sino que tambien se espeficican como se combinan sus valores para dar un resultado. 

En el archivo ***p1.y***, las reglas de produccion, contienen condigo en **C**, el cual, espeficia como se combinan los valores de los tokens para dar un resultado.

En primer lugar, se descompone la expresion hasta llegar a sus partes mas pequeñas segun las reglas de produccion, para posteriormente, volver a combinar los valores de acuerdo con las operaciones aritmeticas definidas en las reglas. Una vez que se reduce la operacion a un solo valor, este resultado se convierte en el resultado que nos da la calculadora, valor el cual, es devuelto por la funcion main de bison (yyparse()).