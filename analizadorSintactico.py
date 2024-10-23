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

def analyze_syntax(lines, syntax_output_file):
    """
    Función para realizar el análisis sintáctico básico y escribir los resultados en el archivo.
    Actualmente solo realiza un análisis básico. Debes expandirla con las reglas de tu gramática.
    """
    with open(syntax_output_file, 'w') as syntax_file:
        for line_num, line in enumerate(lines, start=1):
            # Ejemplo básico de detección de un error de paréntesis mal cerrado
            if '(' in line and ')' not in line:
                col_num = line.find('(') + 1
                syntax_file.write(f"<{line_num},{col_num}> Error sintáctico: se encontró: '('; se esperaba: ')'.\n")
        
        syntax_file.write("El análisis sintáctico ha finalizado exitosamente.\n")

def main():
    """
    Función principal para leer un archivo de entrada, analizarlo léxicamente y sintácticamente,
    y escribir los resultados en archivos de salida.
    """
    # Verificar los argumentos de entrada
    if len(sys.argv) != 4:
        print("Uso: python analizadorLexico.py <archivo_entrada.py> <archivo_salida.txt> <archivo_sintaxis.txt>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    syntax_output_file = sys.argv[3]
    matcher = Matcher()

    try:
        # Leer el archivo de entrada y analizarlo léxicamente
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            line_num = 1
            lines = infile.readlines()  # Leer todas las líneas para luego usar en el análisis sintáctico
            error_found = False  # Variable para controlar si se encontró un error léxico
            for line in lines:
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
                    else:  # Formato para otros tokens
                        outfile.write(f"<{token[0]},{token[1]},{token[2]},{token[3]}>\n")

                line_num += 1
        
        # Realizar el análisis sintáctico
        analyze_syntax(lines, syntax_output_file)

    except FileNotFoundError:
        print(f"Error: El archivo '{input_file}' no fue encontrado.")
        sys.exit(1)

if __name__ == "__main__":
    main()