from antlrEjecucion.MLanguajeVisitor import MLanguajeVisitor
from antlrEjecucion.MLanguajeParser import MLanguajeParser
import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier
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
        """Procesa cada declaración dentro del programa."""
        if ctx.varDeclaration():
            self.visit(ctx.varDeclaration())
        elif ctx.ifStatement():
            self.visit(ctx.ifStatement())
        elif ctx.whileStatement():
            self.visit(ctx.whileStatement())
        elif ctx.forStatement():
            self.visit(ctx.forStatement())
        elif ctx.methodCall():
            self.visit(ctx.methodCall())
        elif ctx.functionDecl():
            self.visit(ctx.functionDecl())
        elif ctx.plotOperation():
            self.visit(ctx.plotOperation())
        elif ctx.fileOperation():
            self.visit(ctx.fileOperation())
        elif ctx.mlFunction():
            self.visit(ctx.mlFunction())
        elif ctx.matrixOperation():
            self.visit(ctx.matrixOperation())
        elif ctx.getChild(0).getText() == 'print':
            self.visitPrintStatement(ctx)
        else:
            self.log(f"[ERROR] Nodo no manejado: {ctx.getText()}")


    def visitVarDeclaration(self, ctx):
        print("[DEBUG] Declaración de variable")
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        print(f"[DEBUG] Variable {var_name} asignada a {value}")
        return value

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
        elif ctx.list_():  # Corregido de list() a list_()
            return self.visitList(ctx.list_())
        elif ctx.matrixConstructor():
            return self.visitMatrixConstructor(ctx.matrixConstructor())
        elif ctx.getChildCount() == 3:  # Operaciones binarias
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            operator = ctx.getChild(1).getText()
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
        elif ctx.getChildCount() == 2:  # Operador unario (e.g., -x)
            value = self.visit(ctx.expression(0))
            if ctx.getChild(0).getText() == '-':
                return -value
        elif ctx.getChildCount() == 1:  # Valores directos
            return self.visit(ctx.getChild(0))

    def visitList(self, ctx):
        """Procesa una lista."""
        print("[DEBUG] Evaluando lista")
        return [self.visit(expr) for expr in ctx.expression()]

    def visitMatrixConstructor(self, ctx):
        """Procesa una construcción de matriz."""
        print("[DEBUG] Evaluando matriz")
        return np.array(self.visitList(ctx.list_()))  # Corregido de list() a list_()

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

    def visitPlotOperation(self, ctx):
        x_values = self.visit(ctx.expression(0))
        y_values = self.visit(ctx.expression(1))
        if not isinstance(x_values, list) or not isinstance(y_values, list):
            raise TypeError("Los argumentos deben ser listas.")
        if len(x_values) != len(y_values):
            raise ValueError("Las listas deben tener la misma longitud.")

        plt.plot(x_values, y_values, marker='o', label='plotLine')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Gráfica de Línea")
        plt.legend()
        plt.grid(True)
        image_name = "plot_line.png"
        plt.savefig(image_name)
        plt.close()
        self.log(f"[OUTPUT] Gráfica de línea guardada en {image_name}")



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

    def get_summary(self):
        """Devuelve un resumen acumulado de los resultados."""
        return "\n".join(self.output_log)

