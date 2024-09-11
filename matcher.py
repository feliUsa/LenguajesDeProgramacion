class Matcher:
    """
    Clase que proporciona métodos para reconocer y categorizar tokens léxicos en código fuente de Python.
    """
    def __init__(self):
        """
        Inicializa el Matcher con una lista de palabras reservadas y patrones de tokens.
        """
        self.reserved_words = {
            'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 
            'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
            'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
            'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
        }
        self.token_patterns = [
            ('tk_and_sym', '&&'),
            ('tk_or_sym', '||'),
            ('tk_par_izq', '('),
            ('tk_par_der', ')'),
            ('tk_dos_puntos', ':'),
            ('tk_asig', '='),
            ('tk_comparacion', '=='),
            ('tk_punto', '.'),
            ('tk_coma', ','),
            ('tk_sum', '+'),
            ('tk_res', '-'),
            ('tk_mult', '*'),
            ('tk_exp', '**'),
            ('tk_div', '/'),
            ('tk_divent', '//'),
            ('tk_porc', '%'),
            ('tk_distinto', '!='),
            ('tk_ejecuta', '->'),
            ('tk_menor', '>'),
            ('tk_mayor', '<'),
            ('tk_key_izq', '{'),
            ('tk_key_der', '}'),
            ('tk_corc_izq', '['),
            ('tk_corc_der', ']')
        ]

    def match(self, text, pos):
        """
        Busca coincidencias de tokens en una posición dada del texto.

        Args:
            text (str): El texto a analizar.
            pos (int): La posición actual en el texto.

        Returns:
            tuple or None: Una tupla con información del token si se encuentra, o None si no.
        """
        
        # Verificar si es un comentario
        if text[pos] == '#':
            return ('tk_comment', text[pos:], len(text))  # Reconoce como comentario

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

        # Verificar si es un número (entero o decimal)
        if text[pos].isdigit() or (text[pos] == '.' and pos + 1 < len(text) and text[pos + 1].isdigit()):
            end = pos
            decimal_found = False
            while end < len(text) and (text[end].isdigit() or (text[end] == '.' and not decimal_found)):
                if text[end] == '.':
                    decimal_found = True
                end += 1
            return ('tk_entero', text[pos:end], end)

        # Verificar si es una palabra reservada
        for word in self.reserved_words:
            if text.startswith(word, pos):
                # Asegurarse de que la palabra reservada no es parte de un identificador más largo
                if pos + len(word) == len(text) or not self.is_identifier_part(text[pos + len(word)]):
                    return (word, word, pos + len(word))

        # Verificar si es un identificador válido
        if self.is_identifier_start(text[pos]):
            end = pos
            while end < len(text) and self.is_identifier_part(text[end]):
                end += 1
            return ('id', text[pos:end], end)

        # Verificar si es un operador lógico o símbolo
        for token_type, pattern in self.token_patterns:
            if text.startswith(pattern, pos):
                return (token_type, pattern, pos + len(pattern))

        # Si no es un token válido, retornar None para indicar un error léxico
        return None

    def is_identifier_start(self, char):
        """
        Verifica si un carácter puede ser el inicio de un identificador.

        Args:
            char (str): El carácter a verificar.

        Returns:
            bool: True si el carácter es válido para iniciar un identificador, False en caso contrario.
        """
        return char.isalpha() or char == '_'

    def is_identifier_part(self, char):
        """
        Verifica si un carácter puede ser parte de un identificador.

        Args:
            char (str): El carácter a verificar.

        Returns:
            bool: True si el carácter es válido como parte de un identificador, False en caso contrario.
        """
        return char.isalnum() or char == '_'
