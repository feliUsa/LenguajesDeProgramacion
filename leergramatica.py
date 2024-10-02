import networkx as nx
import matplotlib.pyplot as plt

# 1. Leer la gramática de un archivo
def leer_gramatica(archivo):
    reglas_produccion = {}
    terminales = set()

    with open(archivo, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if '->' in linea:
                parte_izquierda, parte_derecha = linea.split('->')
                parte_izquierda = parte_izquierda.strip()
                producciones = [p.strip() for p in parte_derecha.split('|')]
                if parte_izquierda not in reglas_produccion:
                    reglas_produccion[parte_izquierda] = []
                reglas_produccion[parte_izquierda].extend(producciones)
                for prod in producciones:
                    for simbolo in prod:
                        if simbolo.islower():
                            terminales.add(simbolo)
    return reglas_produccion, terminales

# 2. Dibujar el árbol de derivación
def dibujar_arbol(reglas_usadas, cadena):
    G = nx.DiGraph()
    nodo_id = 0

    def agregar_nodo(padre, regla, simbolo):
        nonlocal nodo_id
        nodo_actual = nodo_id
        G.add_node(nodo_actual, label=simbolo)
        if padre is not None:
            G.add_edge(padre, nodo_actual, label=regla)
        nodo_id += 1
        return nodo_actual

    nodo_raiz = agregar_nodo(None, None, 'S')
    
    for regla in reglas_usadas:
        padre, simbolo, regla_usada = regla
        nodo_actual = agregar_nodo(padre, regla_usada, simbolo)

    # Dibujar el árbol con labels
    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    edge_labels = nx.get_edge_attributes(G, 'label')

    nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000, node_color="lightblue", font_size=10, font_color="black", font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()

# 3. Verificación secuencial letra por letra
def verificar_cadena(cadena, reglas_produccion):
    n = len(cadena)
    reglas_usadas = []
    
    for i, simbolo in enumerate(cadena):
        encontrado = False
        for var in reglas_produccion:
            for regla in reglas_produccion[var]:
                if regla == simbolo:  # Si encontramos una regla que genera el símbolo
                    reglas_usadas.append((i, var, simbolo))
                    encontrado = True
                    break
            if encontrado:
                break
        
        if not encontrado:
            print(f"Cadena no aceptada por la gramática. Símbolo '{simbolo}' no encontrado en las reglas de producción.")
            return False, None

    # Si todas las letras fueron aceptadas
    return True, reglas_usadas

# 4. Función principal
def main():
    archivo_gramatica = 'gramatica.txt'
    reglas_produccion, terminales = leer_gramatica(archivo_gramatica)
    
    # Mostrar reglas de producción y terminales
    print("Reglas de producción:")
    for var in reglas_produccion:
        for regla in reglas_produccion[var]:
            print(f"{var} -> {regla}")
    
    print("\nTerminales:")
    print(", ".join(terminales))

    # Ingresar la cadena a validar
    cadena = input("\nIngresa la cadena a validar: ")

    # Verificar si la cadena es aceptada
    aceptada, reglas_usadas = verificar_cadena(cadena, reglas_produccion)

    if aceptada:
        print("Cadena aceptada por la gramática.")
        dibujar_arbol(reglas_usadas, cadena)
    else:
        print("Cadena no aceptada por la gramática.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
