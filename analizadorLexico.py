import sys
from matcher import Matcher
from Parser import Parser

def tokenize_line(line, line_num, matcher):
    tokens = []
    pos = 0

    while pos < len(line):
        # Ignorar espacios en blanco
        if line[pos].isspace():
            pos += 1
            continue

        match = matcher.match(line, pos)
        if match:
            if match[0] == 'Error léxico':  # Manejo del error léxico
                tokens.append(('Error léxico', line_num, pos + 1))
                break  # Detener la tokenización en cuanto haya un error léxico
            elif len(match) == 3:  # Caso estándar
                token_type, text, new_pos = match

                # Ignorar los comentarios en la salida
                if token_type == 'tk_comment':
                    break  # Ignorar el resto de la línea si es un comentario
                
                # Si es una palabra reservada
                if token_type in matcher.reserved_words:
                    tokens.append((token_type, line_num, pos + 1))
                else:
                    tokens.append((token_type, text, line_num, pos + 1))
                
                pos = new_pos
            else:
                tokens.append(('Error léxico', line_num, pos + 1))
                break
        else:
            tokens.append(('Error léxico', line_num, pos + 1))
            break

    return tokens


def main():
    """
    Función principal para leer un archivo de entrada, analizarlo léxicamente, y luego realizar el análisis sintáctico.
    """
    # Verificar los argumentos de entrada
    if len(sys.argv) != 3:
        print("Uso: python analizadorSintactico.py <archivo_entrada.py> <archivo_salida.txt>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    matcher = Matcher()

    tokens = []
    with open(input_file, 'r') as infile:
        line_num = 1
        for line in infile:
            tokens += tokenize_line(line, line_num, matcher)
            line_num += 1

    # Pasar los tokens al analizador sintáctico
    parser = Parser(tokens)
    result = parser.parse()

    # Guardar el resultado del análisis en el archivo de salida
    with open(output_file, 'w') as outfile:
        outfile.write(result)


if __name__ == "__main__":
    main()
