# Definir las reglas de la gramática
grammar_1 = {
    'S': [['A', 'uno', 'B', 'C'], ['S', 'dos']],
    'A': [['B', 'C', 'D'], ['A', 'tres'], ['ε']],
    'B': [['D', 'cuatro', 'C', 'tres'], ['ε']],
    'C': [['cinco', 'D', 'B'], ['ε']],
    'D': [['seis'], ['ε']]
}

grammar_2 = {
    'S': [['A', 'B', 'uno']],
    'A': [['dos', 'B'], ['ε']],
    'B': [['C', 'D'], ['tres'], ['ε']],
    'C': [['cuatro', 'A', 'B'], ['cinco']],
    'D': [['seis'], ['ε']]
}

# Paso 1: Calcular el conjunto PRIMERO
def calcular_primeros(grammar):
    primeros = {non_terminal: set() for non_terminal in grammar.keys()}
    cambios = True
    
    while cambios:
        cambios = False
        for non_terminal, producciones in grammar.items():
            for produccion in producciones:
                if produccion[0] in grammar:  # Si es un no terminal
                    for symbol in produccion:
                        if symbol in grammar:  # Solo continuar con no terminales
                            if not primeros[non_terminal].issuperset(primeros[symbol]):
                                primeros[non_terminal].update(primeros[symbol])
                                cambios = True
                        else:  # Es un terminal
                            if symbol not in primeros[non_terminal]:
                                primeros[non_terminal].add(symbol)
                                cambios = True
                            break  # Detenemos al encontrar un terminal
                else:
                    primeros[non_terminal].add(produccion[0])  # Añadir terminal directamente
                
    return {nt: list(primeros[nt]) for nt in primeros}

# Paso 2: Calcular el conjunto SIGUIENTE
def calcular_siguientes(grammar, primeros):
    siguientes = {non_terminal: set() for non_terminal in grammar.keys()}
    siguientes['S'].add('#')  # Fin de la cadena

    cambios = True
    
    while cambios:
        cambios = False
        for non_terminal, producciones in grammar.items():
            for produccion in producciones:
                for i, symbol in enumerate(produccion):
                    if symbol in grammar:  # Si es un no terminal
                        # Obtener lo que sigue en la producción
                        if i + 1 < len(produccion):
                            siguiente_symbol = produccion[i + 1]
                            if siguiente_symbol in grammar:  # No terminal
                                for terminal in primeros[siguiente_symbol]:
                                    if terminal not in siguientes[symbol]:
                                        siguientes[symbol].add(terminal)
                                        cambios = True
                            else:  # Es un terminal
                                if siguiente_symbol not in siguientes[symbol]:
                                    siguientes[symbol].add(siguiente_symbol)
                                    cambios = True
                        else:  # Si está al final
                            if non_terminal in siguientes[symbol]:
                                for terminal in siguientes[non_terminal]:
                                    if terminal not in siguientes[symbol]:
                                        siguientes[symbol].add(terminal)
                                        cambios = True

    return {nt: list(siguientes[nt]) for nt in siguientes}

# Paso 3: Calcular el conjunto de PREDICCIÓN
def calcular_prediccion(grammar, primeros, siguientes):
    prediccion = {}
    
    for non_terminal, producciones in grammar.items():
        prediccion[non_terminal] = set()
        for produccion in producciones:
            if produccion[0] in primeros:  # Si el primer símbolo es un no terminal
                prediccion[non_terminal].update(primeros[produccion[0]])
            elif produccion[0] == 'ε':  # Si es epsilon
                prediccion[non_terminal].update(siguientes[non_terminal])
    
    return {nt: list(prediccion[nt]) for nt in prediccion}

# Calcular PRIMERO, SIGUIENTE y PREDICCIÓN
primeros = calcular_primeros(grammar_1)
siguientes = calcular_siguientes(grammar_1, primeros)
prediccion = calcular_prediccion(grammar_1, primeros, siguientes)

primeros_2 = calcular_primeros(grammar_2)
siguientes_2 = calcular_siguientes(grammar_2, primeros_2)
prediccion_2 = calcular_prediccion(grammar_2, primeros_2, siguientes_2)

print("\nGramatica 1:")
print("S → A uno B C")
print("S → S dos")
print("A → B C D")
print("A → A tres")
print("A → ε")
print("B → D cuatro C tres")
print("B → ε")
print("C → cinco D B")
print("C → ε")
print("D → seis")
print("D → ε")

# Imprimir resultados
print("Conjunto PRIMERO:")
for nt, conjunto in primeros.items():
    print(f"PRIMERO({nt}) = {{ {', '.join(conjunto)} }}")

print("\nConjunto SIGUIENTE:")
for nt, conjunto in siguientes.items():
    print(f"SIGUIENTE({nt}) = {{ {', '.join(conjunto)} }}")

print("\nConjunto de PREDICCIÓN:")
for nt, conjunto in prediccion.items():
    print(f"PREDICCIÓN({nt}) = {{ {', '.join(conjunto)} }}")

print("\n\n\n  SSSSS  EEEEE  GGGGG  U   U  N   N  DDDD   AAAAA")
print(" SS      E      G      U   U  NN  N  D   D  A   A")
print("  SSSSS  EEEE   G  GG  U   U  N N N  D   D  AAAAA")
print("      SS E      G   G  U   U  N  NN  D   D  A   A")
print("  SSSSS  EEEEE  GGGGG   UUU   N   N  DDDD   A   A\n")

# Imprimir "GRAMÁTICA" en letras grandes
print(" GGGGG  RRRR   AAAAA  M   M  ÁÁÁÁÁ  TTTTT  I   CCCC  AAAAA")
print(" G      R   R  A   A  MM MM  Á   Á    T    I   C     A   A")
print(" G  GG  RRRR   AAAAA  M M M  ÁÁÁÁÁ    T    I   C     AAAAA")
print(" G   G  R R    A   A  M   M  Á   Á    T    I   C     A   A")
print(" GGGGG  R  R   A   A  M   M  Á   Á    T    I   CCCC  A   A\n\n\n")

print("\nGramatica 2:")
print("S → A B uno")
print("A → dos B")
print("A → ε")
print("B → C D")
print("B → tres")
print("B → ε")
print("C → cuatro A B")
print("C → cinco")
print("D → seis")
print("D → ε")

# Imprimir resultados para la segunda gramática
print("Conjunto PRIMERO para la gramática 2:")
for nt, conjunto in primeros_2.items():
    print(f"PRIMERO({nt}) = {{ {', '.join(conjunto)} }}")

print("\nConjunto SIGUIENTE para la gramática 2:")
for nt, conjunto in siguientes_2.items():
    print(f"SIGUIENTE({nt}) = {{ {', '.join(conjunto)} }}")

print("\nConjunto de PREDICCIÓN para la gramática 2:")
for nt, conjunto in prediccion_2.items():
    print(f"PREDICCIÓN({nt}) = {{ {', '.join(conjunto)} }}")