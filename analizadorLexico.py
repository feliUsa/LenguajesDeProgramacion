import sys
from matcher import Matcher

def tokenize_line(line, line_num, matcher):
    """
    Tokeniza una línea de texto utilizando la instancia de `Matcher`.

    Args:
        line (str): La línea de código a tokenizar.
        line_num (int): El número de línea actual.
        matcher (Matcher): Instancia de la clase Matcher utilizada para encontrar los tokens.

    Returns:
        list: Una lista de tuplas representando los tokens encontrados o errores léxicos.
    """
    tokens = []
    pos = 0

    while pos < len(line):
        # Ignorar espacios en blanco
        if line[pos].isspace():
            pos += 1
            continue

        match = matcher.match(line, pos)
        if match:
            token_type, text, new_pos = match
            # Si es un comentario, no agregar a la lista de tokens
            if token_type == 'tk_comment':
                break  # Ignoramos el resto de la línea si es un comentario
            # Verificar si es una palabra reservada
            elif token_type in matcher.reserved_words:
                tokens.append((token_type, line_num, pos + 1))
            else:
                tokens.append((token_type, text, line_num, pos + 1))
            pos = new_pos
        else:
            # Si no se encuentra un token válido, reportar un error léxico
            tokens.append(('Error léxico', line_num, pos + 1))
            break  # Detener la tokenización de esta línea y proceder con la siguiente

    return tokens

def main():
    """
    Función principal para leer un archivo de entrada, analizarlo léxicamente, y escribir los resultados en un archivo de salida.
    """
    # Verificar los argumentos de entrada
    if len(sys.argv) != 3:
        print("Uso: python analizadorLexico.py <archivo_entrada.py> <archivo_salida.txt>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    matcher = Matcher()

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            line_num = 1
            for line in infile:
                tokens = tokenize_line(line, line_num, matcher)
                for token in tokens:
                    if token[0] == 'Error léxico':
                        # Formato de error léxico
                        outfile.write(f"Error léxico(linea:{token[1]},posicion:{token[2]})\n")
                    elif len(token) == 3:  # Formato para palabras reservadas
                        outfile.write(f"<{token[0]},{token[1]},{token[2]}>\n")
                    else:  # Formato para otros tokens
                        outfile.write(f"<{token[0]},{token[1]},{token[2]},{token[3]}>\n")
                line_num += 1
    except FileNotFoundError:
        print(f"Error: El archivo '{input_file}' no fue encontrado.")
        sys.exit(1)

if __name__ == "__main__":
    main()