# Uso de BISON para Ejecutar una Calculadora

---

**Integrantes**

* Andres Vasquez
* Daniel Oviedo
* Sara Villanueva

---

## ¿Como correr el código?

1. Descargar el proyecto
2. Descomprimir el archivo.zip
3. En la terminal (Dependiendo de la gramatica a probar)
   
    a. Ingresar a la carpeta Example_Bison


    1. Gramatica normal

        a. bison -d gramaticaNormal.y

        b. flex gramaticaNormal.l

        c. gcc gramaticaNormal.tab.c lex.yy.c -o calculadoraNormal -lm

        d. ./calculadoraNormal


    2. Gramatica Inversa

        a. bison -d gramaticaInversa.y

        b. flex gramaticaInversa.l

        c. gcc gramaticaInversa.tab.c lex.yy.c -o calculadoraInversa -lm

        d. ./calculadoraInversa


    3. Menor precedencia los paréntesis

        a. bison -d gramaticaParentesis.y

        b. flex gramaticaParentesis.l
        
        c. gcc gramaticaParentesis.tab.c lex.yy.c -o calculadoraParentesis -lm

        d. ./calculadoraParentesis


 4. Realizar las pruebas funcionales de la calculadora