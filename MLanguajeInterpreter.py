from antlrEjecucion.MLanguajeVisitor import MLanguajeVisitor
from antlrEjecucion import MLanguajeParser
import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans

class MLanguajeInterpreter(MLanguajeVisitor):
    def __init__(self):
        self.variables = {}

    # Manejo de declaraciones de variables
    def visitVarDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        
        # Validar listas y matrices
        if isinstance(value, list):
            value = list(value)
        elif isinstance(value, np.ndarray):
            value = np.array(value)

        self.variables[var_name] = value
        return value

    # Operaciones aditivas
    def visitAdditiveExpression(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left + right if ctx.op.text == '+' else left - right

    # Operaciones multiplicativas
    def visitMultiplicativeExpression(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.text == '*':
            return left * right
        elif ctx.op.text == '/':
            if right == 0:
                raise ZeroDivisionError("No se puede dividir entre cero.")
            return left / right
        elif ctx.op.text == '%':
            return left % right

    # Potencias
    def visitPowerExpression(self, ctx):
        base = self.visit(ctx.expression(0))
        exponent = self.visit(ctx.expression(1))
        return math.pow(base, exponent)

    # Funciones trigonométricas
    def visitTrigonometricExpression(self, ctx):
        angle = self.visit(ctx.expression())
        if ctx.op.text == 'sin':
            return math.sin(angle)
        elif ctx.op.text == 'cos':
            return math.cos(angle)
        elif ctx.op.text == 'tan':
            return math.tan(angle)

    # Condicionales if-else
    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.expression())
        if condition:
            statements = ctx.statement(0)
        else:
            statements = ctx.statement(1) if ctx.statement(1) else []
        self._executeStatements(statements)

    # Ciclos while
    def visitWhileStatement(self, ctx):
        while self.visit(ctx.expression()):  # Evaluar la condición
            for stmt in ctx.statement():  # Ejecutar las declaraciones en el cuerpo
                self.visit(stmt)


    # Ciclos for
    def visitForStatement(self, ctx):
        # Inicialización de la variable
        self.visit(ctx.varDeclaration())
        while self.visit(ctx.expression(0)):
            self._executeStatements(ctx.statement())
            # Actualización del bucle
            update_expr = ctx.expression(1)
            if update_expr:
                self.visit(update_expr)

    # Graficación
    def visitPlotOperation(self, ctx):
        if isinstance(ctx, MLanguajeParser.PlotLineContext):
            x_values = self.visit(ctx.expression(0))
            y_values = self.visit(ctx.expression(1))

            if not isinstance(x_values, list) or not isinstance(y_values, list):
                raise TypeError("Los argumentos de plotLine deben ser listas.")

            if len(x_values) != len(y_values):
                raise ValueError("Las listas x e y deben tener la misma longitud.")

            plt.plot(x_values, y_values, marker='o', label="plotLine")
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Gráfica de Línea')
            plt.legend()
            plt.grid(True)
            plt.show()
        elif isinstance(ctx, MLanguajeParser.PlotBarContext):
            x_values = self.visit(ctx.expression(0))
            y_values = self.visit(ctx.expression(1))

            if not isinstance(x_values, list) or not isinstance(y_values, list):
                raise TypeError("Los argumentos de plotBar deben ser listas.")

            if len(x_values) != len(y_values):
                raise ValueError("Las listas x e y deben tener la misma longitud.")

            plt.bar(x_values, y_values, color='blue', label="plotBar")
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Gráfica de Barras')
            plt.legend()
            plt.grid(True)
            plt.show()


    # Manejo de archivos
    def visitFileOperation(self, ctx):
        filename = ctx.STRING().getText().strip('"')
        if ctx.op.text == 'readFile':
            with open(filename, 'r') as file:
                return file.read()
        elif ctx.op.text == 'writeFile':
            data = self.visit(ctx.expression())
            with open(filename, 'w') as file:
                file.write(data)
        return None

    # Operaciones de matrices
    def visitMatrixOperation(self, ctx):
        matrix = self.visit(ctx.expression(0))
        if not isinstance(matrix, np.ndarray):
            raise ValueError(f"Se esperaba una matriz, pero se obtuvo: {type(matrix)}")
        
        operation = ctx.operation.getText()
        if operation == 'add':
            other = self.visit(ctx.expression(1))
            return np.add(matrix, other)
        elif operation == 'subtract':
            other = self.visit(ctx.expression(1))
            return np.subtract(matrix, other)
        elif operation == 'multiply':
            other = self.visit(ctx.expression(1))
            return np.dot(matrix, other)
        elif operation == 'transpose':
            return np.transpose(matrix)
        elif operation == 'inverse':
            return np.linalg.inv(matrix)
        else:
            raise ValueError(f"Operación desconocida: {operation}")

    # Regresión lineal
    def linear_regression(self, x_values, y_values, plot=False):
        x = np.array(x_values)
        y = np.array(y_values)
        A = np.vstack([x, np.ones(len(x))]).T
        m, c = np.linalg.lstsq(A, y, rcond=None)[0]
        self.variables['linear_regression_result'] = (m, c)
        if plot:
            plt.scatter(x, y, color='blue', label='Data points')
            plt.plot(x, m * x + c, color='red', label=f'y={m:.2f}x + {c:.2f}')
            plt.legend()
            plt.show()
        return m, c

    # Clasificador MLP
    def multilayer_perceptron(self, x_train, y_train, x_test=None, y_test=None, hidden_layer_sizes=(10,), max_iter=1000):
        mlp = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, max_iter=max_iter)
        mlp.fit(x_train, y_train)
        self.variables['mlp_model'] = mlp
        if x_test is not None and y_test is not None:
            predictions = mlp.predict(x_test)
            accuracy = accuracy_score(y_test, predictions)
            print(f"Accuracy: {accuracy:.2f}")
            return accuracy
        return mlp

    # Agrupamiento K-means
    def kmeans_clustering(self, data, num_clusters=3, plot=False):
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(data)
        labels = kmeans.labels_
        self.variables['kmeans_model'] = kmeans
        self.variables['kmeans_labels'] = labels
        if plot and data.shape[1] == 2:
            plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
            plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Centroids')
            plt.legend()
            plt.show()
        return labels

    # Método auxiliar para ejecutar listas de declaraciones
    def _executeStatements(self, statements):
        if isinstance(statements, list):
            for stmt in statements:
                self.visit(stmt)
        else:
            self.visit(statements)

    # Manejo de matrices: transponer
    def visitMatrixTranspose(self, ctx):
        matrix = self.variables[ctx.ID().getText()]
        if not isinstance(matrix, np.ndarray):
            raise ValueError(f"Se esperaba una matriz, pero se obtuvo: {type(matrix)}")
        return np.transpose(matrix)

    # Manejo de matrices: inversa
    def visitMatrixInverse(self, ctx):
        matrix = self.variables[ctx.ID().getText()]
        if not isinstance(matrix, np.ndarray):
            raise ValueError(f"Se esperaba una matriz, pero se obtuvo: {type(matrix)}")
        return np.linalg.inv(matrix)
