#include <stdio.h>
#include <string.h>
#include "dfa.h"

int main() {
    DFA dfa;
    char filename[MAX_STRING_LEN];
    char inputString[MAX_STRING_LEN];

    printf("Ingrese el nombre del archivo de configuración: ");
    scanf("%s", filename);

    // Cargar la configuración del DFA desde el archivo
    loadDFAConfiguration(&dfa, filename);

    // Mostrar la configuración del DFA
    printDFAConfiguration(&dfa);

    // Bucle para procesar múltiples cadenas
    while (1) {
        printf("Ingrese la cadena de entrada (o escriba 'salir' para terminar): ");
        scanf("%s", inputString);

        // Verificar si el usuario quiere salir
        if (strcmp(inputString, "salir") == 0) {
            printf("Terminando el programa.\n");
            break;
        }

        // Validar el alfabeto y procesar la cadena
        if (validateAlphabet(&dfa, inputString)) {
            if (processString(&dfa, inputString)) {
                printf("Resultado: La cadena fue aceptada.\n");
            } else {
                printf("Resultado: La cadena fue rechazada (No termina en un estado de aceptación).\n");
            }
        } else {
            printf("Resultado: La cadena fue rechazada (Hay letras que no forman parte del alfabeto).\n");
        }
    }

    return 0;
}
