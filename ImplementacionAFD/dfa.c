#include "dfa.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Función para cargar la configuración del DFA desde un archivo
void loadDFAConfiguration(DFA *dfa, const char *filename) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf("No se pudo abrir el archivo de configuración.\n");
        exit(1);
    }

    // Leer los estados
    fgets(dfa->states[0], MAX_STRING_LEN, file);
    dfa->numStates = 0;
    char *token = strtok(dfa->states[0], ",\n");
    while (token) {
        strcpy(dfa->states[dfa->numStates++], token);
        token = strtok(NULL, ",\n");
    }

    // Leer el alfabeto
    fgets(dfa->alphabet, MAX_STRING_LEN, file);
    dfa->numAlphabet = strlen(dfa->alphabet) - 1;  // Descontar el salto de línea

    // Leer el estado inicial
    fgets(dfa->initialState, MAX_STRING_LEN, file);
    dfa->initialState[strcspn(dfa->initialState, "\n")] = '\0';  // Eliminar el salto de línea

    // Leer los estados de aceptación
    fgets(dfa->acceptingStates[0], MAX_STRING_LEN, file);
    dfa->numAcceptingStates = 0;
    token = strtok(dfa->acceptingStates[0], ",\n");
    while (token) {
        strcpy(dfa->acceptingStates[dfa->numAcceptingStates++], token);
        token = strtok(NULL, ",\n");
    }

    // Leer las transiciones
    dfa->numTransitions = 0;
    while (fgets(dfa->transitions[dfa->numTransitions].currentState, MAX_STRING_LEN, file)) {
        token = strtok(dfa->transitions[dfa->numTransitions].currentState, ",\n");
        strcpy(dfa->transitions[dfa->numTransitions].currentState, token);

        token = strtok(NULL, ",\n");
        dfa->transitions[dfa->numTransitions].symbol = token[0];

        token = strtok(NULL, ",\n");
        strcpy(dfa->transitions[dfa->numTransitions].nextState, token);

        dfa->numTransitions++;
    }

    fclose(file);
}

// Función para validar si una cadena pertenece al alfabeto del DFA
int validateAlphabet(DFA *dfa, const char *inputString) {
    for (int i = 0; inputString[i] != '\0'; i++) {
        int valid = 0;
        for (int j = 0; j < dfa->numAlphabet; j++) {
            if (inputString[i] == dfa->alphabet[j]) {
                valid = 1;
                break;
            }
        }
        if (!valid) {
            return 0;  // Carácter no válido
        }
    }
    return 1;
}

// Función para procesar una cadena en el DFA y mostrar las transiciones
int processString(DFA *dfa, const char *inputString) {
    char currentState[MAX_STRING_LEN];
    strcpy(currentState, dfa->initialState);

    printf("\n--- Procesando la cadena '%s' ---\n", inputString);
    printf("Estado inicial: %s\n", currentState);

    for (int i = 0; inputString[i] != '\0'; i++) {
        char currentChar = inputString[i];
        int transitionFound = 0;

        printf("Procesando carácter '%c'\n", currentChar);

        for (int j = 0; j < dfa->numTransitions; j++) {
            if (strcmp(dfa->transitions[j].currentState, currentState) == 0 &&
                dfa->transitions[j].symbol == currentChar) {
                printf("Transición: %s --%c--> %s\n", currentState, currentChar, dfa->transitions[j].nextState);
                strcpy(currentState, dfa->transitions[j].nextState);
                transitionFound = 1;
                break;
            }
        }

        if (!transitionFound) {
            printf("No se encontró una transición válida. La cadena fue rechazada.\n");
            return 0;
        }
    }

    for (int i = 0; i < dfa->numAcceptingStates; i++) {
        if (strcmp(dfa->acceptingStates[i], currentState) == 0) {
            printf("Estado final: %s (aceptado)\n", currentState);
            printf("------------------------------\n");
            return 1;
        }
    }

    printf("Estado final: %s (no aceptado)\n", currentState);
    printf("------------------------------\n");
    return 0;
}

// Función para mostrar la configuración del DFA
void printDFAConfiguration(DFA *dfa) {
    printf("\n--- Configuración del DFA ---\n");

    // Mostrar estados
    printf("Estados: ");
    for (int i = 0; i < dfa->numStates; i++) {
        printf("%s", dfa->states[i]);
        if (i < dfa->numStates - 1) {
            printf(", ");
        }
    }
    printf("\n");

    // Mostrar alfabeto
    printf("Alfabeto: ");
    for (int i = 0; i < dfa->numAlphabet; i++) {
        printf("%c", dfa->alphabet[i]);
        if (i < dfa->numAlphabet - 1) {
            printf(", ");
        }
    }
    printf("\n");

    // Mostrar estado inicial
    printf("Estado inicial: %s\n", dfa->initialState);

    // Mostrar estados de aceptación
    printf("Estados de aceptación: ");
    for (int i = 0; i < dfa->numAcceptingStates; i++) {
        printf("%s", dfa->acceptingStates[i]);
        if (i < dfa->numAcceptingStates - 1) {
            printf(", ");
        }
    }
    printf("\n");

    // Mostrar transiciones
    printf("Transiciones:\n");
    for (int i = 0; i < dfa->numTransitions; i++) {
        printf("  %s --%c--> %s\n", dfa->transitions[i].currentState, dfa->transitions[i].symbol, dfa->transitions[i].nextState);
    }
    printf("------------------------------\n");
}
