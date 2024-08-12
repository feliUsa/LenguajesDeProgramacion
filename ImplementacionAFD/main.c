#include <stdio.h>
#include <string.h>
#include "dfa.h"

int main() {
    DFA dfa;  // Configuracion del automata
    char filename[tamString];
    char inputString[tamString];


    printf("Ingrese el nombre del archivo de configuración: ");
    scanf("%s", filename);

    cargarConfiguracion(&dfa, filename);

    printConfig(&dfa);

    while (1) {
        printf("Ingrese la cadena de entrada (o escriba 'salir' para terminar): ");
        scanf("%s", inputString);

        if (strcmp(inputString, "salir") == 0) {
            printf("Terminando el programa.\n");
            break;
        }

        if (validarAlfabeto(&dfa, inputString)) {
            if (procesarCadena(&dfa, inputString)) {
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
