import sys
from matcher import Matcher

def check_delimiters_balance(lines, syntax_file):
    stack = []
    delimiter_pairs = {')': '(', ']': '[', '}': '{'}
    opening_delimiters = set(delimiter_pairs.values())

    for line_num, line in enumerate(lines, start=1):
        for col_num, char in enumerate(line, start=1):
            if char in opening_delimiters:
                stack.append((char, line_num, col_num))
            elif char in delimiter_pairs:
                if stack and stack[-1][0] == delimiter_pairs[char]:
                    stack.pop()
                else:
                    syntax_file.write(f"<{line_num},{col_num}> Error sintáctico: delimitador '{char}' sin su apertura correspondiente.\n")
                    return False

    if stack:
        char, line_num, col_num = stack.pop()
        syntax_file.write(f"<{line_num},{col_num}> Error sintáctico: delimitador '{char}' sin su cierre correspondiente.\n")
        return False

    return True

def validate_def_block(line, line_num, syntax_file):
    """Valida la estructura de una definición de función, incluyendo `__init__`."""
    if '__init__' in line:
        # Verificación estricta para `__init__` con los delimitadores `(`, `)`, y `:`
        if '(' not in line or ')' not in line or ':' not in line:
            col_start = line.find('__init__') + 1
            syntax_file.write(f"<{line_num},{col_start}> Error sintáctico en '__init__': se esperaba un identificador, seguido de '()' y ':'.\n")
            return False
    else:
        # Verificación general para otras funciones
        if '(' not in line or ')' not in line or ':' not in line:
            col_start = line.find('def') + 1
            syntax_file.write(f"<{line_num},{col_start}> Error sintáctico: se esperaba un identificador, seguido de '()' y ':'.\n")
            return False
    return True

def validate_class_block(line, line_num, syntax_file):
    """Valida la estructura de una definición de clase."""
    if ':' not in line:
        col_start = line.find('class') + 1
        syntax_file.write(f"<{line_num},{col_start}> Error sintáctico: se esperaba ':'.\n")
        return False
    return True

def validate_control_structure(line, line_num, token_type, syntax_file):
    """Valida estructuras como if, for, while, etc."""
    if ':' not in line:
        col_start = line.find(token_type) + 1
        syntax_file.write(f"<{line_num},{col_start}> Error sintáctico: se encontró '{token_type}'; se esperaba ':'.\n")
        return False
    return True

def validate_elif_else_context(control_stack, line_num, token_type, syntax_file):
    """Verifica que elif y else estén dentro de un contexto válido de if."""
    if 'if' not in control_stack:
        syntax_file.write(f"<{line_num},1> Error sintáctico: '{token_type}' fuera de contexto 'if'.\n")
        return False
    return True

def tokenize_line(line, line_num, matcher):
    tokens = []
    pos = 0

    while pos < len(line):
        if line[pos].isspace():
            pos += 1
            continue

        match = matcher.match(line, pos)
        if match:
            if match[0] == 'Error léxico':
                tokens.append(('Error léxico', line_num, pos + 1))
                break
            elif len(match) == 3:
                token_type, text, new_pos = match

                if token_type == 'tk_comment':
                    break

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
    indent_stack = [0]
    control_structure_stack = []

    with open(syntax_output_file, 'w') as syntax_file:
        if not check_delimiters_balance(lines, syntax_file):
            return

        for line_num, line in enumerate(lines, start=1):
            stripped_line = line.lstrip()

            if not stripped_line or stripped_line.startswith('#'):
                continue

            indent_level = len(line) - len(stripped_line)
            top_indent = indent_stack[-1] if indent_stack else 0

            if indent_level > top_indent:
                indent_stack.append(indent_level)
            elif indent_level < top_indent:
                while indent_stack and indent_stack[-1] > indent_level:
                    indent_stack.pop()
                if indent_level != indent_stack[-1]:
                    syntax_file.write(f"<{line_num},1> Error sintáctico: Indentación inconsistente.\n")
                    return

            first_token = matcher.match(stripped_line, 0)
            if first_token:
                token_type, token_text, col_start = first_token

                if token_type == 'def':
                    if not validate_def_block(stripped_line, line_num, syntax_file):
                        return
                    control_structure_stack.append(token_type)

                elif token_type == 'class':
                    if not validate_class_block(stripped_line, line_num, syntax_file):
                        return
                    control_structure_stack.append(token_type)

                elif token_type in ['if', 'for', 'while']:
                    if not validate_control_structure(stripped_line, line_num, token_type, syntax_file):
                        return
                    control_structure_stack.append(token_type)

                elif token_type in ['elif', 'else']:
                    if not validate_elif_else_context(control_structure_stack, line_num, token_type, syntax_file):
                        return
                    if not validate_control_structure(stripped_line, line_num, token_type, syntax_file):
                        return

            if '(' in line and ')' not in line:
                col_num = line.find('(') + 1
                syntax_file.write(f"<{line_num},{col_num}> Error sintáctico: se encontró '('; se esperaba ')'.\n")
                return

        syntax_file.write("El análisis sintáctico ha finalizado exitosamente.\n")

def main():
    if len(sys.argv) != 4:
        print("Uso: python analizador.py <archivo_entrada.py> <archivo_salida.txt> <archivo_sintaxis.txt>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    syntax_output_file = sys.argv[3]
    matcher = Matcher()

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            lines = infile.readlines()
            line_num = 1

            for line in lines:
                tokens = tokenize_line(line, line_num, matcher)
                for token in tokens:
                    if token[0] == 'Error léxico':
                        outfile.write(f"Error léxico(linea:{token[1]},posicion:{token[2]})\n")
                    elif len(token) == 3:
                        outfile.write(f"<{token[0]},{token[1]},{token[2]}>\n")
                    else:
                        outfile.write(f"<{token[0]},{token[1]},{token[2]},{token[3]}>\n")

                line_num += 1

            analyze_syntax(lines, syntax_output_file, matcher)

    except FileNotFoundError:
        print(f"Error: El archivo '{input_file}' no fue encontrado.")
        sys.exit(1)

if __name__ == "__main__":
    main()
