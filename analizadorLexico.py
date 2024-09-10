import sys
from matcher import Matcher

# Función para tokenizar una línea utilizando Matcher
def tokenize_line(line, line_num, matcher):
    tokens = []
    pos = 0

    while pos < len(line):
        match = matcher.match(line, pos)
        if match:
            token_type, text, new_pos = match
            tokens.append((token_type, text, line_num, pos + 1))
            pos = new_pos
        else:
            pos += 1

    return tokens

# Leer archivo .py y procesar línea por línea
def main():
    if len(sys.argv) != 2:
        print("Uso: python analizadorLexico.py <archivo_entrada.py>")
        sys.exit(1)
    
    filename = sys.argv[1]
    matcher = Matcher()

    try:
        with open(filename, 'r') as file:
            line_num = 1
            for line in file:
                tokens = tokenize_line(line, line_num, matcher)
                for token in tokens:
                    print(f"<{token[0]},{token[1]},{token[2]},{token[3]}>")
                line_num += 1
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no fue encontrado.")
        sys.exit(1)

if __name__ == "__main__":
    main()
