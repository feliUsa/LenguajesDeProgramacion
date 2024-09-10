class Matcher:
    def __init__(self):
        self.token_patterns = [
            ('class', 'class'),
            ('def', 'def'),
            ('if', 'if'),
            ('return', 'return'),
            ('True', 'True'),
            ('False', 'False'),
            ('None', 'None'),
            ('object', 'object'),
            ('bool', 'bool'),
            ('str', 'str'),
            ('tk_par_izq', '('),
            ('tk_par_der', ')'),
            ('tk_dos_puntos', ':'),
            ('tk_asig', '='),
            ('tk_punto', '.'),
            ('tk_ejecuta', '->'),
            ('tk_lambda', 'lambda'),
            ('tk_and', 'and'),
            ('tk_or', 'or'),
            ('tk_not', 'not'),
            ('tk_and_sym', '&&'),
            ('tk_or_sym', '||'),
        ]

    def match(self, text, pos):
        # Verificar si es un comentario
        if text[pos] == '#':
            end = len(text)
            return ('id', text[pos:end].strip(), end)

        # Verificar si es un docstring (triple comillas dobles)
        if text.startswith('"""', pos):
            end = pos + 3
            while end < len(text) and not text.startswith('"""', end):
                end += 1
            end += 3  # Incluir el cierre de triple comillas dobles
            return ('tk_docstring', text[pos:end], end)

        # Verificar si es una cadena con comillas dobles
        if text[pos] == '"':
            end = pos + 1
            while end < len(text) and text[end] != '"':
                end += 1
            end += 1  # Incluir la comilla de cierre
            return ('tk_cadena', text[pos:end], end)

        # Verificar si es una cadena con comillas simples
        if text[pos] == "'":
            end = pos + 1
            while end < len(text) and text[end] != "'":
                end += 1
            end += 1  # Incluir la comilla de cierre
            return ('tk_cadena', text[pos:end], end)

        # Verificar si es un operador lógico o simbólico
        for token_type, pattern in self.token_patterns:
            if text.startswith(pattern, pos):
                return (token_type, pattern, pos + len(pattern))

        # Verificar si es un identificador
        if self.is_identifier_start(text[pos]):
            end = pos
            while end < len(text) and self.is_identifier_part(text[end]):
                end += 1
            return ('id', text[pos:end], end)

        return None

    def is_identifier_start(self, char):
        return char.isalpha() or char == '_'

    def is_identifier_part(self, char):
        return char.isalnum() or char == '_'
