#ifndef DFA_H
#define DFA_H

#define tamString 100      // Longitud máxima para nombres de estados, alfabeto, etc.
#define maxStates 100
#define maxTransitions 100
#define maxAlphabet 26

// Estructura para representar una transición en el DFA
typedef struct {
    char estadoActual[tamString];  // Estado actual de la transicion
    char entrySymbol;                        // Símbolo de entrada que causa la transición
    char nextState[tamString];     // Estado despues de la transicion
} Transition;


typedef struct {
    char states[maxStates][tamString];
    int numStates;
    char alphabet[maxAlphabet];
    int numAlphabet;
    Transition transitions[maxTransitions];
    int numTransitions;
    char initialState[tamString];
    char estadoAceptacion[maxStates][tamString];
    int numEstadosAceptacion;
} DFA;

// Carga la configuración del DFA desde un archivo
// El archivo debe contener los estados, alfabeto, estado inicial, estados de aceptación y transiciones
void cargarConfiguracion(DFA *dfa, const char *filename);

// Valida que todos los caracteres de la cadena de entrada pertenezcan al alfabeto del DFA
// Retorna 1 si es valida, 0 si no es valida
int validarAlfabeto(DFA *dfa, const char *inputString);

// Procesa una cadena de entrada en el DFA y determina si es aceptada o rechazada
// Muestra las transiciones realizadas durante el procesamiento
// Retorna 1 si es aceptada, 0 si no es aceptada
int procesarCadena(DFA *dfa, const char *inputString);

// Imprime la configuración del DFA, incluyendo estados, alfabeto, estado inicial,
// estados de aceptación y transiciones
void printConfig(DFA *dfa);

#endif
