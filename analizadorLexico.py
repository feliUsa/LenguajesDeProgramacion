import sys
from matcher import Matcher

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
            error_found = False  # Variable para controlar si se encontró un error léxico
            for line in infile:
                if error_found:  # Si ya se encontró un error, detenemos el análisis
                    break

                tokens = tokenize_line(line, line_num, matcher)
                for token in tokens:
                    if token[0] == 'Error léxico':
                        # Formato de error léxico
                        outfile.write(f"Error léxico(linea:{token[1]},posicion:{token[2]})\n")
                        error_found = True  # Indicar que se encontró un error léxico
                        break  # Detener la escritura de tokens y análisis

                    elif len(token) == 3:  # Formato para palabras reservadas
                        outfile.write(f"<{token[0]},{token[1]},{token[2]}>\n")

                line_num += 1
    except FileNotFoundError:
        print(f"Error: El archivo '{input_file}' no fue encontrado.")
        sys.exit(1)

if __name__ == "__main__":
    main()
