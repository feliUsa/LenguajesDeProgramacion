import networkx as nx
import matplotlib.pyplot as plt

def leer_gramatica(archivo):
    reglas = {}
    with open(archivo, 'r') as f:
        for linea in f:
            if '->' in linea:
                izquierda, derecha = linea.strip().split('->')
                izquierda = izquierda.strip()
                alternativas = [x.strip() for x in derecha.split('|')]
                reglas[izquierda] = alternativas
    return reglas

def construir_arbol(reglas, inicio='S'):
    G = nx.DiGraph()

    def agregar_nodos_y_aristas(estado, padre=None):
        if padre:
            G.add_edge(padre, estado)
        if estado in reglas:
            for alternativa in reglas[estado]:
                for simbolo in alternativa.split():
                    if simbolo != '|':
                        G.add_node(simbolo)
                        agregar_nodos_y_aristas(simbolo, estado)

    G.add_node(inicio)
    agregar_nodos_y_aristas(inicio)
    return G

def visualizar_arbol(G, archivo_salida='arbol.png'):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
    plt.savefig(archivo_salida)
    plt.close()

# Ejemplo de uso
if __name__ == "__main__":
    reglas = leer_gramatica('gramatica.txt')
    arbol = construir_arbol(reglas)
    visualizar_arbol(arbol)
