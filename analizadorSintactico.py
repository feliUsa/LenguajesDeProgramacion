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


def analyze_syntax(lines, syntax_output_file, matcher):
    """
    Función para realizar el análisis sintáctico básico y escribir los resultados en el archivo.
    Además, detecta errores de indentación y errores estructurales.
    """
    current_indent_level = 0  # Nivel actual de indentación
    indent_stack = []  # Pila para controlar los niveles de indentación
    control_structure_stack = []  # Pila para controlar las estructuras de control

    with open(syntax_output_file, 'w') as syntax_file:
        for line_num, line in enumerate(lines, start=1):
            stripped_line = line.lstrip()

            # Ignorar líneas vacías o que sean comentarios
            if not stripped_line or stripped_line.startswith('#'):
                continue

            # Determinar nivel de indentación (contar espacios al inicio)
            indent_level = len(line) - len(stripped_line)

            # Verificar si la indentación es múltiplo de 4
            if indent_level % 4 != 0:
                syntax_file.write(f"<{line_num},1> Error sintáctico: Indentación incorrecta, debe ser múltiplo de 4.\n")

            # Detectar el token inicial de la línea
            first_token = matcher.match(stripped_line, 0)
            
            if first_token:
                token_type = first_token[0]

                # Verificar si el token es una estructura de control o una definición
                if token_type in ['if', 'for', 'while', 'def', 'class', 'elif', 'else', 'try', 'except', 'finally']:
                    # Validar que la siguiente línea esté indentada correctamente
                    if indent_level <= current_indent_level:
                        syntax_file.write(f"<{line_num},1> Error sintáctico: Se esperaba un bloque indentado después de '{token_type}'.\n")
                    
                    # Apilar la estructura de control
                    control_structure_stack.append(token_type)
                    indent_stack.append(current_indent_level)
                    current_indent_level = indent_level

                elif indent_level < current_indent_level:
                    # Si la indentación es menor, estamos saliendo de un bloque
                    while indent_stack and indent_level < indent_stack[-1]:
                        indent_stack.pop()
                        control_structure_stack.pop()

                    if indent_level != (indent_stack[-1] if indent_stack else 0):
                        syntax_file.write(f"<{line_num},1> Error sintáctico: Indentación inesperada.\n")

                    current_indent_level = indent_level

            # Verificar si hay paréntesis sin cerrar
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
    matcher = Matcher()  # Instancia de Matcher para tokenización y análisis sintáctico

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
        analyze_syntax(lines, syntax_output_file, matcher)  # Pasar también el matcher

    except FileNotFoundError:
        print(f"Error: El archivo '{input_file}' no fue encontrado.")
        sys.exit(1)

if __name__ == "__main__":
    main()
