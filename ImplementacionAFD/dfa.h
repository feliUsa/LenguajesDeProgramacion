#ifndef DFA_H
#define DFA_H

#define MAX_STRING_LEN 100
#define MAX_STATES 100
#define MAX_TRANSITIONS 100
#define MAX_ALPHABET 26

// Estructura para representar una transición del DFA
typedef struct {
    char currentState[MAX_STRING_LEN];
    char symbol;
    char nextState[MAX_STRING_LEN];
} Transition;

// Estructura para representar un DFA
typedef struct {
    char states[MAX_STATES][MAX_STRING_LEN];
    int numStates;

    char alphabet[MAX_ALPHABET];
    int numAlphabet;

    Transition transitions[MAX_TRANSITIONS];
    int numTransitions;

    char initialState[MAX_STRING_LEN];

    char acceptingStates[MAX_STATES][MAX_STRING_LEN];
    int numAcceptingStates;
} DFA;

// Declaraciones de funciones
void loadDFAConfiguration(DFA *dfa, const char *filename);
int validateAlphabet(DFA *dfa, const char *inputString);
int processString(DFA *dfa, const char *inputString);
void printDFAConfiguration(DFA *dfa);

#endif
