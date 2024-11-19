from antlrEjecucion.MLanguajeVisitor import MLanguajeVisitor
from antlrEjecucion.MLanguajeParser import MLanguajeParser
import math
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

class MLanguajeInterpreter(MLanguajeVisitor):
    def __init__(self):
        self.variables = {}
        self.output_log = []  # Lista para almacenar la salida de la ejecución

    def log(self, message):
        """Muestra mensajes directamente en la consola y los guarda en el log."""
        print(message)
        self.output_log.append(message)

    def visitProgram(self, ctx):
        """Procesa el programa completo."""
        print("[DEBUG] Visitando programa")
        for statement in ctx.statement():
            self.visit(statement)

    def visitStatement(self, ctx):
        if ctx.varDeclaration():
            print("[DEBUG] Visitando varDeclaration")
            self.visit(ctx.varDeclaration())
        elif ctx.ifStatement():
            print("[DEBUG] Visitando ifStatement")
            self.visit(ctx.ifStatement())
        elif ctx.whileStatement():
            print("[DEBUG] Visitando whileStatement")
            self.visit(ctx.whileStatement())
        elif ctx.forStatement():
            print("[DEBUG] Visitando forStatement")
            self.visit(ctx.forStatement())
        elif ctx.methodCall():
            print("[DEBUG] Visitando methodCall")
            self.visit(ctx.methodCall())
        elif ctx.functionDecl():
            print("[DEBUG] Visitando functionDecl")
            self.visit(ctx.functionDecl())
        elif ctx.plotOperation():
            print("[DEBUG] Visitando plotOperation")
            self.visit(ctx.plotOperation())
        elif ctx.fileOperation():
            print("[DEBUG] Visitando fileOperation")
            self.visit(ctx.fileOperation())
        elif ctx.mlFunction():
            print("[DEBUG] Visitando mlFunction")
            self.visit(ctx.mlFunction())
        elif ctx.matrixOperation():
            print("[DEBUG] Visitando matrixOperation")
            self.visit(ctx.matrixOperation())
        elif ctx.getChild(0).getText() == 'print':
            print("[DEBUG] Visitando printStatement")
            self.visitPrintStatement(ctx)
        else:
            self.log(f"[ERROR] Nodo no manejado: {ctx.getText()}")


    def visitVarDeclaration(self, ctx):
        """Maneja declaraciones de variables."""
        print("[DEBUG] Declaración de variable")
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        print(f"[DEBUG] Variable {var_name} asignada a {value}")
        return value


    def visitList(self, ctx):
        """Procesa una lista."""
        print("[DEBUG] Evaluando lista")
        return [self.visit(expr) for expr in ctx.expression()]


    def visitMatrixConstructor(self, ctx):
        """Procesa una construcción de matriz."""
        print("[DEBUG] Evaluando matriz")
        try:
            result = np.array(self.visitList(ctx.list_()))
            print(f"[DEBUG] Matriz construida: {result}")
            return result
        except Exception as e:
            self.log(f"[ERROR] Error en matrixConstructor: {e}")
            print(f"[ERROR] Detalles del error: {e}")
            return None


    def visitIfStatement(self, ctx):
        """Maneja declaraciones if."""
        try:
            print("[DEBUG] Ejecutando declaración if")
            condition = self.visit(ctx.expression())
            print(f"[DEBUG] Condición evaluada: {condition}")
            if condition:
                self._executeStatements(ctx.statement(0))
            elif ctx.statement(1):
                self._executeStatements(ctx.statement(1))
        except Exception as e:
            self.log(f"[ERROR] Error en declaración if: {e}")


    def visitWhileStatement(self, ctx):
        """Maneja bucles while."""
        print("[DEBUG] Ejecutando declaración while")
        while self.visit(ctx.expression()):
            print(f"[DEBUG] Condición while evaluada como True")
            self._executeStatements(ctx.statement())
        print("[DEBUG] Salida del while loop")
        
        
    def visitForStatement(self, ctx):
        """Maneja bucles for estilo Python."""
        print("[DEBUG] Ejecutando forStatement")
        try:
            # Obtener el nombre de la variable de iteración
            var_name = ctx.ID().getText()

            # Evaluar la expresión iterable (e.g., range(5) o una lista)
            iterable = self.visit(ctx.expression())

            if not hasattr(iterable, '__iter__'):
                raise TypeError(f"[ERROR] El objeto {iterable} no es iterable.")

            # Iterar sobre el iterable
            for value in iterable:
                # Asignar el valor actual a la variable de iteración
                self.variables[var_name] = value
                print(f"[DEBUG] Variable de iteración {var_name} = {value}")

                # Ejecutar el cuerpo del bucle
                self._executeStatements(ctx.statement())
        except Exception as e:
            self.log(f"[ERROR] Error en forStatement: {e}")
            print(f"[ERROR] Detalles del error: {e}")



    def visitPlotOperation(self, ctx):
        """Maneja las operaciones de graficado para líneas."""
        try:
            print("[DEBUG] Entrando a visitPlotOperation")
            
            # Evaluar las expresiones para X e Y
            x_values = self.visit(ctx.expression(0))
            y_values = self.visit(ctx.expression(1))
            print(f"[DEBUG] Valores de X: {x_values}, Valores de Y: {y_values}")

            # Validar que sean listas
            if not isinstance(x_values, list) or not isinstance(y_values, list):
                raise TypeError("[ERROR] Los valores X e Y deben ser listas.")
            if len(x_values) != len(y_values):
                raise ValueError(f"[ERROR] Las listas X e Y deben tener la misma longitud. Len(X): {len(x_values)}, Len(Y): {len(y_values)}")

            # Graficar
            plt.scatter(x_values, y_values, label='Datos', color='blue', s=100)  # Cambiado a scatter para consistencia
            plt.plot(x_values, y_values, marker='o', linestyle='-', color='green', label='Línea')  # Línea con marcador
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.title("Gráfica de Línea")
            plt.legend()
            plt.grid(True)

            # Guardar la gráfica
            image_name = "plot_line.png"
            print(f"[DEBUG] Guardando gráfica en {image_name}")
            plt.savefig(image_name)  # Guardar la gráfica
            plt.close()  # Cerrar la figura
            self.log(f"[OUTPUT] Gráfica de línea guardada en {image_name}")
            print(f"[DEBUG] Gráfica guardada correctamente en {image_name}")
        except Exception as e:
            self.log(f"[ERROR] Error en plotOperation: {e}")
            print(f"[ERROR] Detalles del error: {e}")



    def _executeStatements(self, statements):
        if isinstance(statements, list):
            for stmt in statements:
                self.visit(stmt)
        else:
            self.visit(statements)

    def get_summary(self):
        """Devuelve un resumen acumulado de los resultados."""
        return "\n".join(self.output_log)
    
    
    def visitPrintStatement(self, ctx):
        """Maneja declaraciones print."""
        value = self.visit(ctx.expression())
        self.log(f"[OUTPUT] {value}")
        

    def visitExpression(self, ctx):
        """Evalúa una expresión."""
        print("[DEBUG] Evaluando expresión")
        
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText()) if '.' in ctx.NUMBER().getText() else int(ctx.NUMBER().getText())
        
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')
        
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise NameError(f"Variable '{var_name}' no definida")
        
        elif ctx.list_():
            return self.visitList(ctx.list_())
        
        elif ctx.matrixConstructor():
            return self.visitMatrixConstructor(ctx.matrixConstructor())
        
        elif ctx.getChildCount() == 3:  # Operaciones binarias
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            operator = ctx.getChild(1).getText()
            if operator in ['+', '-', '*', '/', '%', '^']:
                return self._evaluateArithmetic(left, right, operator)
            elif operator in ['>', '<', '>=', '<=', '==', '!=']:
                return self._evaluateComparison(left, right, operator)
        
        elif ctx.getChildCount() == 2:  # Operador unario (e.g., -x)
            value = self.visit(ctx.expression(0))
            if ctx.getChild(0).getText() == '-':
                return -value
        
        elif ctx.getChild(0).getText() == 'range':  # Evaluación de range
            start = self.visit(ctx.expression(0))  # Primer argumento: inicio
            stop = self.visit(ctx.expression(1)) if ctx.expression(1) else None  # Segundo argumento: fin (opcional)
            step = self.visit(ctx.expression(2)) if ctx.expression(2) else 1  # Tercer argumento: paso (opcional)
            
            # Construir el rango
            if stop is None:
                return range(start)  # Solo un argumento: range(stop)
            return range(start, stop, step)  # Dos o tres argumentos: range(start, stop, step)
        
        elif ctx.getChild(0).getText() in ['sin', 'cos', 'tan']:  # Funciones trigonométricas
            value = self.visit(ctx.expression(0))
            if not isinstance(value, (int, float)):
                raise TypeError(f"El argumento de {ctx.getChild(0).getText()} debe ser numérico.")
            if ctx.getChild(0).getText() == 'sin':
                return math.sin(value)
            elif ctx.getChild(0).getText() == 'cos':
                return math.cos(value)
            elif ctx.getChild(0).getText() == 'tan':
                return math.tan(value)
        
        elif ctx.getChildCount() == 1:  # Valores directos
            return self.visit(ctx.getChild(0))



    def _evaluateArithmetic(self, left, right, operator):
        """Evalúa operaciones aritméticas."""
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            if right == 0:
                raise ZeroDivisionError("División por cero")
            return left / right
        elif operator == '%':
            return left % right
        elif operator == '^':
            return math.pow(left, right)

    def _evaluateComparison(self, left, right, operator):
        """Evalúa operaciones de comparación."""
        if operator == '>':
            return left > right
        elif operator == '<':
            return left < right
        elif operator == '>=':
            return left >= right
        elif operator == '<=':
            return left <= right
        elif operator == '==':
            return left == right
        elif operator == '!=':
            return left != right
        
        
    def visitMatrixOperation(self, ctx):
        """Maneja operaciones con matrices."""
        print("[DEBUG] Visitando matrixOperation")
        try:
            # Obtener el nombre de la matriz
            matrix_name = ctx.ID().getText()
            if matrix_name not in self.variables:
                raise NameError(f"[ERROR] Matriz '{matrix_name}' no está definida.")

            # Obtener la operación
            operation = ctx.getChild(2).getText()
            matrix = self.variables[matrix_name]
            print(f"[DEBUG] Matriz '{matrix_name}': {matrix}")
            print(f"[DEBUG] Operación: {operation}")

            # Operaciones binarias
            if operation in ['add', 'subtract', 'multiply']:
                other_matrix = self.visit(ctx.expression(0))
                print(f"[DEBUG] Otra matriz: {other_matrix}")
                if not isinstance(other_matrix, np.ndarray):
                    raise TypeError(f"[ERROR] La operación '{operation}' requiere una matriz válida.")
                if operation == 'add':
                    result = np.add(matrix, other_matrix)
                elif operation == 'subtract':
                    result = np.subtract(matrix, other_matrix)
                elif operation == 'multiply':
                    result = np.dot(matrix, other_matrix)

            # Operaciones unarias
            elif operation == 'transpose':
                result = np.transpose(matrix)
            elif operation == 'inverse':
                if len(matrix) != len(matrix[0]):
                    raise ValueError("[ERROR] Solo se puede calcular la inversa de matrices cuadradas.")
                result = np.linalg.inv(matrix)

            print(f"[DEBUG] Resultado de '{operation}': {result}")
            self.variables[f"{matrix_name}_{operation}"] = result  # Guardar resultado
            return result
        except Exception as e:
            self.log(f"[ERROR] Error en matrixOperation: {e}")
            print(f"[ERROR] Detalles del error: {e}")
            return None




        
    def visitMlFunction(self, ctx):
        if ctx.getChild(0).getText() == 'multilayer_perceptron':
            return self.visitMultilayerPerceptron(ctx)
        elif ctx.getChild(0).getText() == 'kmeans_clustering':
            return self.visitKmeansClustering(ctx)
        elif ctx.getChild(0).getText() == 'linear_regression':
            return self.visitLinearRegression(ctx)


    def visitMultilayerPerceptron(self, ctx):
        x_train = np.array(self.visit(ctx.expression(0)))
        y_train = np.array(self.visit(ctx.expression(1)))
        mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000)
        mlp.fit(x_train, y_train)
        self.log(f"[OUTPUT] Clasificador entrenado. Pesos: {mlp.coefs_}")


    def visitKmeansClustering(self, ctx):
        """Maneja K-means clustering."""
        try:
            data = np.array(self.visit(ctx.expression(0)))
            num_clusters = self.visit(ctx.expression(1))
            kmeans = KMeans(n_clusters=num_clusters)
            kmeans.fit(data)
            labels = kmeans.labels_
            self.log(f"[OUTPUT] Etiquetas de agrupamiento: {labels}")

            if len(data[0]) == 2:  # Si los datos son bidimensionales, graficamos
                plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', label="Clusters")
                plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=300, label="Centroides")
                plt.title("Agrupamiento K-Means")
                plt.legend()
                image_name = "kmeans_clustering.png"
                plt.savefig(image_name)
                plt.close()
                self.log(f"[OUTPUT] Agrupamiento K-Means guardado en {image_name}")
        except Exception as e:
            self.log(f"[ERROR] Error en K-means clustering: {e}")

    def _executeStatements(self, statements):
        """Ejecuta una lista de declaraciones."""
        if isinstance(statements, list):
            for stmt in statements:
                self.visit(stmt)
        else:
            self.visit(statements)

    def visitFileOperation(self, ctx):
        """Maneja operaciones de archivos."""
        try:
            operation = ctx.getChild(0).getText()
            if operation == 'readFile':
                file_name = ctx.STRING().getText().strip('"')
                with open(file_name, 'r') as file:
                    data = file.read()
                self.log(f"[DEBUG] Archivo leído: {file_name}")
                return data
            elif operation == 'writeFile':
                file_name = ctx.STRING(0).getText().strip('"')
                content = self.visit(ctx.expression())
                with open(file_name, 'w') as file:
                    file.write(str(content))
                self.log(f"[DEBUG] Archivo escrito: {file_name}")
            elif operation == 'readCSV':
                file_name = ctx.STRING().getText().strip('"')
                data = np.loadtxt(file_name, delimiter=',')
                self.log(f"[DEBUG] CSV leído: {file_name}")
                return data
            elif operation == 'writeCSV':
                file_name = ctx.STRING(0).getText().strip('"')
                content = np.array(self.visit(ctx.expression()))
                np.savetxt(file_name, content, delimiter=',')
                self.log(f"[DEBUG] CSV escrito: {file_name}")
        except Exception as e:
            self.log(f"[ERROR] Error en operación de archivo: {e}")
            
    def visitLinearRegression(self, ctx):
        """Maneja la regresión lineal."""
        try:
            # Extraer los datos de entrada (X e y)
            x_train = np.array(self.visit(ctx.expression(0)))  # Primer argumento: X
            y_train = np.array(self.visit(ctx.expression(1)))  # Segundo argumento: y

            # Verificar si X es una lista unidimensional; de ser así, convertirla en una matriz de una sola columna
            if x_train.ndim == 1:
                x_train = x_train.reshape(-1, 1)

            # Crear e entrenar el modelo de regresión lineal
            model = LinearRegression()
            model.fit(x_train, y_train)

            # Extraer coeficientes e intercepto
            coef = model.coef_
            intercept = model.intercept_

            self.log(f"[OUTPUT] Modelo de regresión entrenado. Coeficientes: {coef}, Intercepto: {intercept}")

            # Si el usuario pasa un tercer argumento, predecimos
            if ctx.expression(2) is not None:
                x_test = np.array(self.visit(ctx.expression(2)))
                if x_test.ndim == 1:
                    x_test = x_test.reshape(-1, 1)
                predictions = model.predict(x_test)
                self.log(f"[OUTPUT] Predicciones para {x_test}: {predictions.tolist()}")

        except Exception as e:
            self.log(f"[ERROR] Error en regresión lineal: {e}")


    def get_summary(self):
        """Devuelve un resumen acumulado de los resultados."""
        return "\n".join(self.output_log)

