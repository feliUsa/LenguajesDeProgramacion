from antlrEjecucion.MLanguajeVisitor import MLanguajeVisitor
import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans


class MLanguajeInterpreter(MLanguajeVisitor):
    def __init__(self):
        self.variables = {}

    # Función para manejar declaraciones de variables
    def visitVarDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        return value

    # Función para manejar expresiones aditivas (suma y resta)
    def visitAdditiveExpression(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    # Función para manejar expresiones multiplicativas (*, /, %)
    def visitMultiplicativeExpression(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.text == '*':
            return left * right
        elif ctx.op.text == '/':
            return left / right
        elif ctx.op.text == '%':
            return left % right

    # Función para manejar expresiones de potencia (x^y)
    def visitPowerExpression(self, ctx):
        base = self.visit(ctx.expression(0))
        exponent = self.visit(ctx.expression(1))
        return math.pow(base, exponent)

    # Función para manejar expresiones trigonométricas (sin, cos, tan)
    def visitTrigonometricExpression(self, ctx):
        angle = self.visit(ctx.expression())
        if ctx.op.text == 'sin':
            return math.sin(angle)
        elif ctx.op.text == 'cos':
            return math.cos(angle)
        elif ctx.op.text == 'tan':
            return math.tan(angle)

    # Función para manejar condiciones if-else
    def visitIfStatement(self, ctx):
        condition = self.visit(ctx.expression())
        if condition:
            return self.visit(ctx.program(0))
        elif ctx.elseProgram:
            return self.visit(ctx.elseProgram)

    # Función para manejar bucles for
    def visitForStatement(self, ctx):
        self.visit(ctx.varDeclaration())
        while self.visit(ctx.expression(1)):
            self.visit(ctx.program())
            self.visit(ctx.expression(2))

    # Función para generar gráficos (linea, barras)
    def visitPlotOperation(self, ctx):
        values = [self.visit(arg) for arg in ctx.argumentList().expression()]
        if ctx.op.text == 'plotLine':
            plt.plot(values)
        elif ctx.op.text == 'plotBar':
            plt.bar(range(len(values)), values)
        plt.show()

    # Función para manejo de archivos (lectura, escritura)
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

    # Función de regresión lineal
    def linear_regression(self, x_values, y_values, plot=False):
        x = np.array(x_values)
        y = np.array(y_values)
        A = np.vstack([x, np.ones(len(x))]).T
        m, c = np.linalg.lstsq(A, y, rcond=None)[0]
        self.variables['linear_regression_result'] = (m, c)
        if plot:
            plt.scatter(x, y, color='blue', label='Data points')
            plt.plot(x, m*x + c, color='red', label=f'y={m:.2f}x + {c:.2f}')
            plt.legend()
            plt.show()
        return m, c

    # Función de regresión polinomial
    def polynomial_regression(self, x_values, y_values, degree=2, plot=False):
        x = np.array(x_values)
        y = np.array(y_values)
        coeffs = np.polyfit(x, y, degree)
        poly_func = np.poly1d(coeffs)
        self.variables['polynomial_regression_result'] = coeffs
        if plot:
            x_fit = np.linspace(x.min(), x.max(), 100)
            y_fit = poly_func(x_fit)
            plt.scatter(x, y, color='blue', label='Data points')
            plt.plot(x_fit, y_fit, color='green', label=f'Polynomial regression (degree={degree})')
            plt.legend()
            plt.show()
        return coeffs

    # Función para clasificador con perceptrón multicapa
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

    # Función de agrupamiento con K-means
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

    def visitMatrixOperation(self, ctx):
        matrix_expr = self.visit(ctx.expression(0))
        operation = ctx.operation.getText()
        other_matrix_expr = self.visit(ctx.expression(1)) if ctx.expression(1) else None
        
        if operation == 'add':
            return np.add(matrix_expr, other_matrix_expr)
        elif operation == 'subtract':
            return np.subtract(matrix_expr, other_matrix_expr)
        elif operation == 'multiply':
            return np.dot(matrix_expr, other_matrix_expr)
        elif operation == 'transpose':
            return np.transpose(matrix_expr)
        elif operation == 'inverse':
            return np.linalg.inv(matrix_expr)
        else:
            raise ValueError(f"Operación de matriz desconocida: {operation}")
