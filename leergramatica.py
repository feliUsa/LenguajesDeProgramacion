import networkx as nx
import matplotlib.pyplot as plt

def leer_gramatica(archivo):
    reglas = {}
    print("Leyendo las reglas de producción desde el archivo:")
    with open(archivo, 'r') as f:
        for linea in f:
            if '->' in linea:
                izquierda, derecha = linea.strip().split('->')
                izquierda = izquierda.strip()
                alternativas = [x.strip() for x in derecha.split('|')]
                reglas[izquierda] = alternativas
                print(f"{izquierda} -> {' | '.join(alternativas)}")
    print("\nGramática cargada correctamente.\n")
    return reglas

def es_terminal(simbolo, reglas):
    return simbolo not in reglas

def es_derivable(cadena, reglas, simbolo_inicial='S'):
    def expandir(derivacion, cadena, reglas):
        if derivacion == cadena:
            return derivacion
        if len(derivacion) > len(cadena):
            return None

        for i, simbolo in enumerate(derivacion):
            if simbolo in reglas:
                for alternativa in reglas[simbolo]:
                    nueva_derivacion = derivacion[:i] + alternativa.split() + derivacion[i+1:]
                    resultado = expandir(nueva_derivacion, cadena, reglas)
                    if resultado:
                        return resultado
        return None

    derivacion_inicial = [simbolo_inicial]
    cadena_dividida = cadena.split()
    return expandir(derivacion_inicial, cadena_dividida, reglas)

def construir_arbol(derivacion, reglas):
    G = nx.DiGraph()

    def agregar_nodos_y_aristas(estado, derivacion):
        if estado in reglas:
            for alternativa in reglas[estado]:
                simbolos = alternativa.split()
                for simbolo in simbolos:
                    G.add_node(simbolo)
                    G.add_edge(estado, simbolo)
                    agregar_nodos_y_aristas(simbolo, derivacion)

    G.add_node(derivacion[0])  # Nodo raíz
    for simbolo in derivacion[1:]:
        G.add_node(simbolo)
        G.add_edge(derivacion[0], simbolo)  # Conectar el nodo raíz con el primer símbolo
        agregar_nodos_y_aristas(simbolo, derivacion)
    return G

def visualizar_arbol(G, archivo_salida='arbol_cadena.png'):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
    plt.savefig(archivo_salida)
    plt.show()  # Mostrar la imagen
    plt.close()

# Ejemplo de uso
if __name__ == "__main__":
    archivo_gramatica = 'gramatica.txt'  # Archivo con las reglas gramaticales
    cadena = 'the dog chases a cat'  # Cadena a verificar

    # Leer la gramática desde el archivo
    reglas = leer_gramatica(archivo_gramatica)

    # Mostrar la cadena que se va a derivar
    print(f"\nIntentando derivar la cadena: '{cadena}'\n")

    # Verificar si la cadena es derivable
    derivacion = es_derivable(cadena, reglas)

    if derivacion:
        print(f"La cadena '{cadena}' es válida según la gramática.")
        print(f"Derivación obtenida: {derivacion}\n")
        # Construir el árbol a partir de la derivación
        arbol = construir_arbol(derivacion, reglas)
        # Visualizar el árbol y guardar la imagen
        visualizar_arbol(arbol)
    else:
        print(f"La cadena '{cadena}' no es válida según la gramática.")
