from antlr_generated.MLanguajeVisitor import MLanguajeVisitor
from custom_library import read_csv_custom, read_txt_custom
from custom_library import linear_regression_fit, linear_regression_predict, mlp_fit, mlp_predict, calculate_metrics, generate_random_values
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

variables = {}  # Diccionario global para almacenar variables


class MLanguajeVisitorImplementation(MLanguajeVisitor):

    def visitProgram(self, ctx):
        #print("[DEBUG] Visitando programa")
        for statement in ctx.statement():
            self.visit(statement)

    def visitVariableDeclaration(self, ctx):
        name = ctx.ID().getText()  # Nombre de la variable
        #print(f"[DEBUG] Declarando variable: {name}")
        try:
            value = self.visit(ctx.expression())  # Evaluar la expresión asignada
            #print(f"[DEBUG] Valor evaluado para '{name}': {value}")
            if value is None:
                raise ValueError(f"[ERROR] Error al evaluar la expresión para la variable '{name}'.")
            variables[name] = value  # Almacenar la variable en el diccionario
            #print(f"[DEBUG] Variable '{name}' almacenada con valor: {variables[name]}")
        except Exception as e:
            print(f"[ERROR] Excepción al evaluar la variable '{name}': {e}")
            raise


    def visitPrintStatement(self, ctx):
        if ctx.STRING():
            #print(f"[DEBUG] Imprimiendo cadena: {ctx.STRING().getText().strip('\"')}")
            print(ctx.STRING().getText().strip('\"'))
        else:
            value = self.visit(ctx.expression())
            #print(f"[DEBUG] Imprimiendo expresión evaluada: {value}")
            print(value)



    def visitExpression(self, ctx):
        #print(f"[DEBUG] Evaluando expresión: {ctx.getText()}")
        #print(f"[DEBUG] random: ctx.getChildCount() = {ctx.getChildCount()}")
        #for i in range(ctx.getChildCount()):
            #print(f"[DEBUG] Hijo {i}: {ctx.getChild(i).getText()}")

        if ctx.getChildCount() == 3:  # Operadores binarios
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            operator = ctx.getChild(1).getText()
            #print(f"[DEBUG] Operador: {operator}, Izquierda: {left}, Derecha: {right}")
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
            elif operator == '/':
                return left / right
            elif operator == '**':
                return left ** right
            
            
        elif ctx.getChildCount() == 4:  # Función unaria
            func = ctx.getChild(0).getText()
            value = self.visit(ctx.expression(0))
            #print(f"[DEBUG] Función unaria: {func}, Valor: {value}")
            if func == 'sin':
                return math.sin(value)
            elif func == 'cos':
                return math.cos(value)
            elif func == 'sqrt':
                return math.sqrt(value)
            
        elif ctx.getChildCount() == 8 and ctx.getChild(0).getText() == 'random':  # Función random
            #print("[DEBUG] Detectada función random")
            left = self.visit(ctx.expression(0))  # Primer argumento
            right = self.visit(ctx.expression(1))  # Segundo argumento
            size = self.visit(ctx.expression(2))  # Tercer argumento
            #print(f"[DEBUG] Argumentos random - left: {left}, right: {right}, size: {size}")

            # Validación de argumentos
            #if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
                #raise ValueError(f"[ERROR] Los límites de 'random' deben ser números. Recibido: left={left}, right={right}")
            #if not isinstance(size, int) or size <= 0:
                #raise ValueError(f"[ERROR] El tamaño de 'random' debe ser un entero positivo. Recibido: size={size}")
            
            # Generar valores aleatorios
            result = generate_random_values(left, right, size)
            #print(f"[DEBUG] Resultado de random: {result}")
            return result
        
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '-':  # Números negativos
            value = self.visit(ctx.expression(0))
            #print(f"[DEBUG] Evaluando número negativo: -{value}")
            return -value
        
        
        elif ctx.list_():  # Si es una lista
            result = [self.visit(expr) for expr in ctx.list_().expression()]
            #print(f"[DEBUG] Lista evaluada: {result}")
            return result

        elif ctx.rangeExpr():
            result = self.visitRangeExpr(ctx.rangeExpr())
            #print(f"[DEBUG] Rango evaluado: {list(result)}")
            return result

        elif ctx.fileOperation():  # Operaciones de archivo
            #print(f"[DEBUG] Evaluando operación de archivo: {ctx.getText()}")
            result = self.visitFileOperation(ctx.fileOperation())
            #print(f"[DEBUG] Resultado de operación de archivo: {result}")
            return result

        elif ctx.matrixOperation():  # Operaciones de matriz
            #print(f"[DEBUG] Evaluando operación de matriz como expresión: {ctx.getText()}")
            result = self.visitMatrixOperation(ctx.matrixOperation())
            #print(f"[DEBUG] Resultado de operación de matriz: {result}")
            return result
        
        elif ctx.INT():
            value = int(ctx.INT().getText())
            #print(f"[DEBUG] Valor INT: {value}")
            return value

        elif ctx.FLOAT():
            value = float(ctx.FLOAT().getText())
            #print(f"[DEBUG] Valor FLOAT: {value}")
            return value
        
        elif ctx.STRING():
            value = ctx.STRING().getText().strip('"')
            #print(f"[DEBUG] Valor STRING: {value}")
            return value

        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name not in variables:
                raise ValueError(f"[ERROR] Variable '{var_name}' no está definida.")
            #print(f"[DEBUG] Variable referenciada: {var_name}, Valor: {variables[var_name]}")
            return variables[var_name]

        print("[ERROR] La expresión no es válida.")
        return None





    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.condition())
        if condition:
            for statement in ctx.statement()[:ctx.getChildCount() - 3]:  # Antes del 'else' si existe
                self.visit(statement)
        else:
            if ctx.getChildCount() > 6:  # Procesar bloque else
                else_statements = ctx.statement()[len(ctx.statement()) // 2:]
                for statement in else_statements:
                    self.visit(statement)

    def visitWhileLoop(self, ctx):
        while self.visit(ctx.condition()):
            for statement in ctx.statement():
                self.visit(statement)

    def visitForLoop(self, ctx):
        var_name = ctx.ID().getText()
        iterable = self.visit(ctx.expression())

        if not isinstance(iterable, (list, range)):
            raise ValueError(f"La expresión en el bucle for debe ser una lista o un rango, no {type(iterable).__name__}.")

        # Iterar sobre el iterable
        for val in iterable:
            #print(f"[DEBUG] Iteración: Asignando {val} a {var_name}")
            variables[var_name] = val
            for statement in ctx.statement():
                self.visit(statement)



    def visitRangeExpr(self, ctx):
        if ctx.INT(0) and ctx.INT(1):  # Rango con inicio y fin
            start = int(ctx.INT(0).getText())
            end = int(ctx.INT(1).getText())
            return range(start, end)
        elif ctx.INT(0):  # Rango con solo fin
            end = int(ctx.INT(0).getText())
            return range(end)
        else:
            raise ValueError("Rango no válido en bucle for.")


    def visitList_(self, ctx):
        return [self.visit(expr) for expr in ctx.expression()]


    def visitMatrixOperation(self, ctx):
        operation = ctx.getChild(0).getText()
        #print(f"[DEBUG] Operación de matriz: {operation}")
        try:
            if operation == "addMatrix":
                matrix1 = self.visit(ctx.expression(0))
                matrix2 = self.visit(ctx.expression(1))
                #print(f"[DEBUG] Matriz1: {matrix1}, Matriz2: {matrix2}")
                if isinstance(matrix1, list) and isinstance(matrix2, list):
                    result = np.add(matrix1, matrix2).tolist()
                    #print(f"[DEBUG] Resultado de addMatrix: {result}")
                    return result
                else:
                    raise ValueError(f"Los argumentos de {operation} deben ser matrices válidas.")
            elif operation == "multiplyMatrix":
                matrix1 = self.visit(ctx.expression(0))
                matrix2 = self.visit(ctx.expression(1))
                #print(f"[DEBUG] Matriz1: {matrix1}, Matriz2: {matrix2}")
                if isinstance(matrix1, list) and isinstance(matrix2, list):
                    result = np.dot(matrix1, matrix2).tolist()
                    #print(f"[DEBUG] Resultado de multiplyMatrix: {result}")
                    return result
                else:
                    raise ValueError(f"Los argumentos de {operation} deben ser matrices válidas.")
            elif operation == "transposeMatrix":
                matrix = self.visit(ctx.expression(0))
                #print(f"[DEBUG] Matriz a transponer: {matrix}")
                if isinstance(matrix, list):
                    result = np.transpose(matrix).tolist()
                    #print(f"[DEBUG] Resultado de transposeMatrix: {result}")
                    return result
                else:
                    raise ValueError("El argumento de transposeMatrix debe ser una matriz.")
            elif operation == "inverseMatrix":
                matrix = self.visit(ctx.expression(0))
                #print(f"[DEBUG] Matriz a invertir: {matrix}")
                if isinstance(matrix, list):
                    result = np.linalg.inv(matrix).tolist()
                    #print(f"[DEBUG] Resultado de inverseMatrix: {result}")
                    return result
                else:
                    raise ValueError("El argumento de inverseMatrix debe ser una matriz.")   
                
            elif operation == "linearRegressionFit":
                X = self.visit(ctx.expression(0))
                y = self.visit(ctx.expression(1))
                return linear_regression_fit(X, y)
            elif operation == "linearRegressionPredict":
                X = self.visit(ctx.expression(0))
                beta = self.visit(ctx.expression(1))
                return linear_regression_predict(X, beta)
            elif operation == "mlpFit":
                X = self.visit(ctx.expression(0))
                y = self.visit(ctx.expression(1))
                hidden_neurons = self.visit(ctx.expression(2)) if ctx.expression(2) else 10
                learning_rate = self.visit(ctx.expression(3)) if ctx.expression(3) else 0.01
                return mlp_fit(X, y, hidden_neurons, learning_rate)
            elif operation == "mlpPredict":
                X = self.visit(ctx.expression(0))
                model = self.visit(ctx.expression(1))
                return mlp_predict(X, model)
            
            
            elif operation == "calculateMetrics":
                y_true = self.visit(ctx.expression(0))
                y_pred = self.visit(ctx.expression(1))
                return calculate_metrics(y_true, y_pred)
            
        except Exception as e:
            print(f"[ERROR] Error al realizar operación de matriz '{operation}': {e}")
            raise

    def visitFileOperation(self, ctx):
        operation = ctx.getChild(0).getText()  # Obtener la operación (por ejemplo, loadCSV)
        if operation == "loadCSV":
            filename = ctx.STRING(0).getText().strip('"')  # Accede al primer STRING
            #print(f"Cargando archivo CSV: {filename}")
            try:
                data = read_csv_custom(filename)
                #print(f"Archivo CSV cargado: {data}")
                return data
            except Exception as e:
                print(f"[ERROR] Error al cargar archivo CSV '{filename}': {e}")
                raise
        elif operation == "readFile":
            filename = ctx.STRING(0).getText().strip('"')  # Accede al primer STRING
            #print(f"Leyendo archivo TXT: {filename}")
            try:
                data = read_txt_custom(filename)
                #print(f"Archivo TXT cargado: {data}")
                return data
            except Exception as e:
                print(f"[ERROR] Error al cargar archivo TXT '{filename}': {e}")
                raise
        else:
            raise ValueError(f"[ERROR] Operación de archivo desconocida: {operation}")


    def visitVisualization(self, ctx):
        if ctx.plotLine():
            #print("[DEBUG] Procesando plotLine")
            x = self.visit(ctx.plotLine().expression(0))
            y = self.visit(ctx.plotLine().expression(1))
            plt.plot(x, y)
            plt.show()
        elif ctx.plotBar():
            #print("[DEBUG] Procesando plotBar")
            categories = self.visit(ctx.plotBar().expression(0))
            values = self.visit(ctx.plotBar().expression(1))
            plt.bar(categories, values)
            plt.show()
        elif ctx.plotHistogram():
            #print("[DEBUG] Procesando plotHistogram")
            data = self.visit(ctx.plotHistogram().expression(0))
            plt.hist(data)
            plt.show()
        elif ctx.plotScatter3D():
            #print("[DEBUG] Procesando plotScatter3D")
            x = self.visit(ctx.plotScatter3D().expression(0))
            y = self.visit(ctx.plotScatter3D().expression(1))
            z = self.visit(ctx.plotScatter3D().expression(2))
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(x, y, z)
            plt.show()
        else:
            raise ValueError("[ERROR] Tipo de visualización desconocido.")


    def visitCondition(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = ctx.getChild(1).getText()
        if operator == '>':
            return left > right
        elif operator == '<':
            return left < right
        elif operator == '==':
            return left == right
        elif operator == '!=':
            return left != right