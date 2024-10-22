class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = 0
        self.current_indent = 0

    def parse(self):
        try:
            self.current_token = self.tokens[self.index]
            while self.current_token:
                self.statement()  # Comienza por analizar una declaración
                self.next_token()
        except SyntaxError as e:
            return str(e)
        return "El analisis sintactico ha finalizado exitosamente."

    def next_token(self):
        """Avanza al siguiente token y verifica indentación."""
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
            if self.current_token[0] == 'indent':  # Detecta indentación
                indent_level = self.current_token[1]
                if indent_level > self.current_indent:
                    self.current_indent = indent_level
                elif indent_level < self.current_indent:
                    self.current_indent = indent_level
                    return False  # Indica reducción de bloque
        else:
            self.current_token = None

    def class_definition(self):
        """Verifica la estructura de una clase."""
        self.next_token()
        
        if self.current_token[0] != 'id':  # Se espera el nombre de la clase
            self.raise_syntax_error(["identificador (nombre de la clase)"])
        self.next_token()
        
        if self.current_token[0] == 'tk_par_izq':  # Verifica si hay herencia (paréntesis)
            self.validate_parentheses_content()  # Función para validar herencia en clases
            
        if self.current_token[0] != 'tk_dos_puntos':  # Se espera ':' después de la definición de la clase
            self.raise_syntax_error([":"])
        
        self.next_token()
        
        # Verificar si la siguiente línea está correctamente indentada
        if not self.is_indented(self.current_indent + 1):
            self.raise_syntax_error(["bloque indentado para la clase"])
        
        # Procesar el cuerpo de la clase: variables y funciones
        while self.current_token and self.is_indented(self.current_indent + 1):
            if self.current_token[0] == 'def':
                self.function_definition()  # Procesar métodos dentro de la clase
            elif self.current_token[0] == 'id':  # Procesar atributos de la clase
                self.variable_declaration()  # Manejar declaraciones de variables
            self.next_token()


            
    def variable_declaration(self):
        """Verifica una declaración de variable en el contexto de una clase."""
        self.next_token()  # El nombre de la variable ya está en current_token
        if self.current_token[0] != 'tk_asig' and self.current_token[0] != 'tk_dos_puntos':
            self.raise_syntax_error([":", "="])  # Se espera anotación de tipo o asignación
        self.next_token()  # Continuar con el valor o el tipo de la variable

    def validate_parentheses_content(self):
        """Verifica el contenido dentro de los paréntesis."""
        self.next_token()
        while self.current_token[0] != 'tk_par_der':  # Mientras no cierre el paréntesis
            if self.current_token[0] == 'tk_coma':  # Verifica separadores de clases
                self.next_token()
            elif self.current_token[0] == 'id':  # Identificadores como clases heredadas
                self.next_token()
            else:
                # Si se encuentra algo inesperado, como un ':' dentro de la lista de clases
                self.raise_syntax_error(["identificador o ')'"])
        # Cierra el paréntesis
        self.next_token()

    def validate_parameters(self):
        """Verifica los parámetros en una definición de función."""
        self.next_token()  # Espera que haya un identificador (nombre del parámetro)
        while self.current_token[0] != 'tk_par_der':  # Hasta que cierre el paréntesis
            if self.current_token[0] == 'id':  # Espera un nombre de parámetro
                self.next_token()
                if self.current_token[0] == 'tk_dos_puntos':  # Verifica anotaciones de tipo
                    self.next_token()  # Espera el tipo del parámetro
                    if self.current_token[0] != 'id':
                        self.raise_syntax_error(["tipo de parámetro"])
                if self.current_token[0] == 'tk_asig':  # Verifica valores por defecto
                    self.next_token()  # Espera el valor por defecto
                    if self.current_token[0] not in ['tk_entero', 'tk_cadena']:
                        self.raise_syntax_error(["valor por defecto (ej. número o cadena)"])
            if self.current_token[0] == 'tk_coma':  # Verifica separadores de parámetros
                self.next_token()
            else:
                self.raise_syntax_error([", o )"])
        self.next_token()  # Cierra el paréntesis

    def statement(self):
        """Verifica las construcciones sintácticas básicas (ej. def, if, for, etc.)."""
        if self.current_token[0] == 'class':  # Token 'class' debería ser reconocido
            self.class_definition()
        elif self.current_token[0] == 'def':
            self.function_definition()
        elif self.current_token[0] == 'if':
            self.if_statement()
        elif self.current_token[0] == 'for':
            self.for_statement()
        elif self.current_token[0] == 'while':
            self.while_statement()
        elif self.current_token[0] == 'try':
            self.try_statement()
        elif self.current_token[0] == 'return':
            self.return_statement()
        elif self.current_token[0] == 'raise':
            self.raise_statement()
        elif self.current_token[0] == 'pass':
            self.simple_statement()
        elif self.current_token[0] == 'break':
            self.simple_statement()
        elif self.current_token[0] == 'continue':
            self.simple_statement()
        elif self.current_token[0] == 'assert':
            self.assert_statement()
        elif self.current_token[0] == 'import':
            self.import_statement()
        elif self.current_token[0] == 'global':
            self.global_statement()
        elif self.current_token[0] == 'nonlocal':
            self.nonlocal_statement()
        else:
            self.raise_syntax_error(["declaración válida (class, def, if, for, while, etc.)"])

    def function_definition(self):
        """Verifica la estructura de una función."""
        self.next_token()
        
        if self.current_token[0] != 'id':  # Espera el identificador del nombre de la función
            self.raise_syntax_error(["identificador (nombre de la función)"])
        
        self.next_token()
        
        if self.current_token[0] != 'tk_par_izq':  # Se espera el paréntesis de la lista de parámetros
            self.raise_syntax_error(["("])
        
        # Validar lista de parámetros entre paréntesis
        self.validate_parameters()
        
        if self.current_token[0] != 'tk_dos_puntos':  # Se espera ':' después de los parámetros
            self.raise_syntax_error([":"])
        
        # Verificar el bloque indentado
        self.next_token()
        if not self.is_indented(self.current_indent + 1):
            self.raise_syntax_error(["bloque indentado para la función"])

    def validate_parentheses_content(self):
        """Verifica el contenido dentro de los paréntesis."""
        self.next_token()
        while self.current_token[0] != 'tk_par_der':  # Mientras no cierre el paréntesis
            if self.current_token[0] == 'tk_coma':  # Verifica separadores de clases
                self.next_token()
            elif self.current_token[0] == 'id':  # Identificadores como clases heredadas
                self.next_token()
            else:
                # Si se encuentra algo inesperado, como un ':' dentro de la lista de clases
                self.raise_syntax_error(["identificador o ')'"])
        # Cierra el paréntesis
        self.next_token()


    def try_statement(self):
        """Verifica la estructura de un bloque try-except-finally."""
        self.next_token()
        if self.current_token[0] != 'tk_dos_puntos':
            self.raise_syntax_error([":"])
        self.next_token()
        if not self.is_indented():
            self.raise_syntax_error(["bloque indentado para 'try'"])
        
        # Continuar con 'except', 'else', 'finally'
        while self.current_token[0] in ['tk_except', 'tk_else', 'tk_finally']:
            self.next_token()
            if self.current_token[0] != 'tk_dos_puntos':
                self.raise_syntax_error([":"])
            self.next_token()
            if not self.is_indented():
                self.raise_syntax_error(["bloque indentado para excepción"])

    def if_statement(self):
        """Verifica la estructura de una declaración if."""
        self.next_token()
        if self.current_token[0] != 'tk_par_izq':
            self.raise_syntax_error(["("])
        # Continuar verificando el contenido del 'if' hasta ':'
        self.next_token()
        if self.current_token[0] != 'tk_dos_puntos':
            self.raise_syntax_error([":"])
        # Verificar el bloque indentado
        self.next_token()
        if not self.is_indented(self.current_indent + 1):
            self.raise_syntax_error(["bloque indentado"])

    def for_statement(self):
        """Verifica la estructura de un bucle for."""
        self.next_token()
        if self.current_token[0] != 'id':
            self.raise_syntax_error(["identificador en el for"])
        self.next_token()
        if self.current_token[0] != 'tk_in':
            self.raise_syntax_error(["in"])
        self.next_token()
        if self.current_token[0] not in ['id', 'tk_corc_izq']:  # 'id' o lista
            self.raise_syntax_error(["identificador o lista"])
        # Esperar ':'
        self.next_token()
        if self.current_token[0] != 'tk_dos_puntos':
            self.raise_syntax_error([":"])
        # Verificar el bloque indentado
        self.next_token()
        if not self.is_indented():
            self.raise_syntax_error(["bloque indentado"])
            
    def simple_statement(self):
        """Verifica las declaraciones simples: pass, break, continue."""
        self.next_token()  # Estas declaraciones simplemente pasan al siguiente token

    def is_indented(self, expected_indent):
        """Verifica si el bloque tiene la indentación esperada."""
        if self.current_token[0] == 'indent':  # Verifica si es un token de indentación
            indent_level = self.current_token[1]
            return indent_level == expected_indent
        elif self.current_token[0] == 'id':  # Si encuentra un identificador sin indentación, error
            if self.current_indent == 0:
                return True  # Caso especial: primera línea no indentada (nivel 0)
            return False  # Se espera indentación, pero se encontró un identificador
        return False  # No se encontró un bloque indentado


    def raise_syntax_error(self, expected):
        line, col = self.current_token[1], self.current_token[2]
        found_lexeme = self.current_token[1]  # Asegúrate de que sea el lexema
        expected_tokens = ', '.join([f'"{tok}"' for tok in expected])
        raise SyntaxError(f"<{line},{col}> Error sintactico: se encontro: \"{found_lexeme}\"; se esperaba: {expected_tokens}.")


    def assert_statement(self):
        """Verifica una declaración assert."""
        self.next_token()  # Aquí podría ir la validación de una expresión
        # Esperar expresión después de assert
        if not self.current_token:
            self.raise_syntax_error(["expresión después de assert"])

    def return_statement(self):
        """Verifica una declaración return."""
        self.next_token()  # Esperar una expresión opcional después de return

    def raise_statement(self):
        """Verifica una declaración raise."""
        self.next_token()  # Esperar una excepción opcional después de raise
        
    def import_statement(self):
        """Verifica una declaración import."""
        self.next_token()
        if self.current_token[0] != 'id':
            self.raise_syntax_error(["identificador (nombre del módulo)"])

    def global_statement(self):
        """Verifica una declaración global."""
        self.next_token()
        if self.current_token[0] != 'id':
            self.raise_syntax_error(["identificador (nombre de la variable global)"])

    def nonlocal_statement(self):
        """Verifica una declaración nonlocal."""
        self.next_token()
        if self.current_token[0] != 'id':
            self.raise_syntax_error(["identificador (nombre de la variable nonlocal)"])
