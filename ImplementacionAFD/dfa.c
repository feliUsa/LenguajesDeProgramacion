#include "dfa.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void cargarConfiguracion(DFA *dfa, const char *filename) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf("No se pudo abrir el archivo de configuración.\n");
        exit(1);
    }

    fgets(dfa->states[0], tamString, file);
    dfa->numStates = 0;  // Contador estados
    char *token = strtok(dfa->states[0], ",\n");  // Divide la línea en tokens separados por comas y saltos de línea
    while (token) {
        // Copia cada estado en el arreglo de estados y aumenta el contador
        strcpy(dfa->states[dfa->numStates++], token);
        token = strtok(NULL, ",\n");
    }

    // Alfabeto
    fgets(dfa->alphabet, tamString, file);
    dfa->numAlphabet = strlen(dfa->alphabet) - 1;  // Numero de simbolos en el alfabeto

    // Estado inicial
    fgets(dfa->initialState, tamString, file);
    dfa->initialState[strcspn(dfa->initialState, "\n")] = '\0'; // Elimina el salto de linea al final del estado inicial

    // Estados aceptacion
    fgets(dfa->estadoAceptacion[0], tamString, file);
    dfa->numEstadosAceptacion = 0;
    token = strtok(dfa->estadoAceptacion[0], ",\n");  // Divide la línea en tokens separados por comas y saltos de línea
    while (token) {
        // Copia cada estado de aceptación en el arreglo y aumenta el contador
        strcpy(dfa->estadoAceptacion[dfa->numEstadosAceptacion++], token);
        token = strtok(NULL, ",\n");  // Obtiene el siguiente token
    }

    // Transiciones Automata
    dfa->numTransitions = 0;
    while (fgets(dfa->transitions[dfa->numTransitions].estadoActual, tamString, file)) {
        
        token = strtok(dfa->transitions[dfa->numTransitions].estadoActual, ",\n");  // Divide la línea en tokens separados por comas y saltos de línea
        strcpy(dfa->transitions[dfa->numTransitions].estadoActual, token);  // Estado actual

        token = strtok(NULL, ",\n");
        dfa->transitions[dfa->numTransitions].entrySymbol = token[0];  // Símbolo de entrada

        token = strtok(NULL, ",\n");
        strcpy(dfa->transitions[dfa->numTransitions].nextState, token);  // Estado siguiente

        dfa->numTransitions++;
    }

    fclose(file);
}


int validarAlfabeto(DFA *dfa, const char *inputString) {

// Caracter valido = 1
// Caracter no valido = 0

    for (int i = 0; inputString[i] != '\0'; i++) {
        int valid = 0;
        for (int j = 0; j < dfa->numAlphabet; j++) {
            if (inputString[i] == dfa->alphabet[j]) {
                valid = 1;
                break;
            }
        }
        if (!valid) {
            return 0;
        }
    }
    return 1;
}

int procesarCadena(DFA *dfa, const char *inputString) {
    char estadoActual[tamString];
    strcpy(estadoActual, dfa->initialState);

    printf("\n--- Procesando la cadena '%s' ---\n", inputString);
    printf("Estado inicial: %s\n", estadoActual);

    for (int i = 0; inputString[i] != '\0'; i++) {
        char currentChar = inputString[i];
        int transitionFound = 0;

        printf("Procesando carácter '%c'\n", currentChar);

        // Recorre todas las transiciones para encontrar una que coincida con el estado actual y el símbolo de entrada
        for (int j = 0; j < dfa->numTransitions; j++) {
            if (strcmp(dfa->transitions[j].estadoActual, estadoActual) == 0 &&
                dfa->transitions[j].entrySymbol == currentChar) {
                // Mostramos transicion por transicion
                printf("Transición: %s --%c--> %s\n", estadoActual, currentChar, dfa->transitions[j].nextState);
                strcpy(estadoActual, dfa->transitions[j].nextState);
                transitionFound = 1;
                break;
            }
        }

        if (!transitionFound) {
            printf("No se encontró una transición válida. La cadena fue rechazada.\n");
            return 0;
        }
    }

    // Verifica si el estado final es uno de los estados de aceptación
    for (int i = 0; i < dfa->numEstadosAceptacion; i++) {
        if (strcmp(dfa->estadoAceptacion[i], estadoActual) == 0) {
            printf("Estado final: %s (aceptado)\n", estadoActual);
            printf("------------------------------\n");
            return 1;
        }
    }

    printf("Estado final: %s (no aceptado)\n", estadoActual);
    printf("------------------------------\n");
    return 0;
}

void printConfig(DFA *dfa) {
    printf("\n--- Configuración del DFA ---\n");

    // Lista de estados presentes en la configuracion subida
    printf("Estados: ");
    for (int i = 0; i < dfa->numStates; i++) {
        printf("%s", dfa->states[i]);
        if (i < dfa->numStates - 1) {
            printf(", "); 
        }
    }
    printf("\n");

    // Mostrar el alfabeto
    printf("Alfabeto: ");
    for (int i = 0; i < dfa->numAlphabet; i++) {
        printf("%c", dfa->alphabet[i]);
        if (i < dfa->numAlphabet - 1) {
            printf(", ");
        }
    }
    printf("\n");

    printf("Estado inicial: %s\n", dfa->initialState);


    printf("Estados de aceptación: ");
    for (int i = 0; i < dfa->numEstadosAceptacion; i++) {
        printf("%s", dfa->estadoAceptacion[i]);
        if (i < dfa->numEstadosAceptacion - 1) {
            printf(", ");
        }
    }
    printf("\n");

    printf("Transiciones:\n");
    for (int i = 0; i < dfa->numTransitions; i++) {
        printf("  %s --%c--> %s\n", dfa->transitions[i].estadoActual, dfa->transitions[i].entrySymbol, dfa->transitions[i].nextState);
    }
    printf("------------------------------\n");
}
