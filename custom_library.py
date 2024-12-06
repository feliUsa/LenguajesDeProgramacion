#custom_library.py

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def addMatrix(a, b):
    return np.add(a, b)

def multiplyMatrix(a, b):
    return np.dot(a, b)

def transposeMatrix(a):
    return np.transpose(a)

def inverseMatrix(a):
    return np.linalg.inv(a)

def plotLine(x, y):
    plt.plot(x, y)
    plt.show()

def plotBar(categories, values):
    plt.bar(categories, values)
    plt.show()

def plotHistogram(data):
    plt.hist(data)
    plt.show()

def plotScatter3D(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    plt.show()

def read_csv_custom(file_path):
    """
    Lee un archivo CSV y lo devuelve como una lista de listas.
    """
    try:
        data = pd.read_csv(file_path, header=None).values.tolist()
        return data
    except Exception as e:
        raise ValueError(f"Error al leer el archivo CSV '{file_path}': {e}")

def read_csv_custom_big(file_path):
    """
    Lee un archivo CSV y lo devuelve como una lista de listas.
    """
    try:
        data = pd.read_csv(file_path, skiprows=1)
        data.columns = [f"Columna_{i}" for i in range(len(data.columns))]
        #print(f"[DEBUG] Columnas renombradas: {data.columns.tolist()}")
        return data
    except Exception as e:
        raise ValueError(f"Error al leer el archivo CSV '{file_path}': {e}")

def read_txt_custom(file_path):
    """
    Lee un archivo TXT y devuelve una lista de líneas.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except Exception as e:
        raise ValueError(f"Error al leer el archivo TXT '{file_path}': {e}")



def linear_regression_fit(X, y):
    """
    Ajusta una regresión lineal simple y devuelve los coeficientes m y b (pendiente e intersección).
    """
    # Convertir a arrays 1D para simplificar cálculos
    X = np.array(X).flatten()
    y = np.array(y)

    # Cálculo de medias
    mean_x = np.mean(X)
    mean_y = np.mean(y)

    # Cálculo de la pendiente (m)
    numerator = np.sum((X - mean_x) * (y - mean_y))
    denominator = np.sum((X - mean_x) ** 2)
    m = numerator / denominator

    # Cálculo de la intersección (b)
    b = mean_y - m * mean_x

    return m, b  # Retorna como tupla


    

def linear_regression_predict(X, m, b, decimals=4):
    X = np.array(X).flatten()
    predictions = m * X + b
    return [float(round(pred, decimals)) for pred in predictions]


def initialize_weights(input_neurons, hidden_neurons, output_neurons):
    """
    Inicializa los pesos y sesgos para el MLP.
    """
    np.random.seed(42)  # Para reproducibilidad
    W1 = np.random.randn(input_neurons, hidden_neurons) * 0.01
    b1 = np.zeros((1, hidden_neurons))
    W2 = np.random.randn(hidden_neurons, output_neurons) * 0.01
    b2 = np.zeros((1, output_neurons))
    return W1, b1, W2, b2


# Gradiente descendiente
# Derivadas parciales con rspecto a los pesos (w1, w2) y segos (b1, b2)
# predicciones
def forward_pass(X, W1, b1, W2, b2):
    """
    Realiza el paso hacia adelante (forward pass).
    """
    Z1 = X @ W1 + b1  # Capa oculta
    A1 = np.tanh(Z1)  # Activación (tanh)
    Z2 = A1 @ W2 + b2  # Capa de salida
    A2 = 1 / (1 + np.exp(-Z2))  # Activación (sigmoide)
    return Z1, A1, Z2, A2

# gradientes
def backward_pass(X, y, Z1, A1, A2, W2):
    """
    Calcula los gradientes para el paso hacia atrás (backward pass).
    """
    m = X.shape[0]  # Número de ejemplos
    dZ2 = A2 - y  # Error en la salida
    dW2 = A1.T @ dZ2 / m
    db2 = np.sum(dZ2, axis=0, keepdims=True) / m
    dZ1 = (dZ2 @ W2.T) * (1 - np.power(A1, 2))  # Derivada de tanh
    dW1 = X.T @ dZ1 / m
    db1 = np.sum(dZ1, axis=0, keepdims=True) / m
    return dW1, db1, dW2, db2


# Actualizar pesos
def update_weights(W1, b1, W2, b2, dW1, db1, dW2, db2, learning_rate):
    """
    Actualiza los pesos y sesgos usando gradiente descendente.
    """
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    return W1, b1, W2, b2


def mlp_fit(X, y, hidden_neurons=10, learning_rate=0.01, epochs=1000):
    """
    Entrena un perceptrón multicapa (MLP) con una capa oculta.
    """
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)
    input_neurons = X.shape[1]
    output_neurons = y.shape[1]

    # Inicialización de pesos
    W1, b1, W2, b2 = initialize_weights(input_neurons, hidden_neurons, output_neurons)

    # Entrenamiento
    for epoch in range(epochs):
        # Paso hacia adelante
        Z1, A1, Z2, A2 = forward_pass(X, W1, b1, W2, b2)

        # Paso hacia atrás
        dW1, db1, dW2, db2 = backward_pass(X, y, Z1, A1, A2, W2)

        # Actualización de pesos
        W1, b1, W2, b2 = update_weights(W1, b1, W2, b2, dW1, db1, dW2, db2, learning_rate)

        # Imprimir error cada 100 épocas
        if (epoch + 1) % 100 == 0:
            loss = np.mean((y - A2) ** 2)  # Error cuadrático medio
            print(f"Época {epoch + 1}/{epochs}, Error: {loss:.4f}")

    return {"W1": W1, "b1": b1, "W2": W2, "b2": b2}


def mlp_predict(X, model):
    """
    Realiza predicciones con un modelo de MLP entrenado.
    """
    X = np.array(X)
    W1, b1, W2, b2 = model["W1"], model["b1"], model["W2"], model["b2"]
    _, _, _, A2 = forward_pass(X, W1, b1, W2, b2)
    return A2.tolist()



def generate_random_values(start, end, size=1):
    """
    Genera valores aleatorios en un rango dado.
    :param start: Límite inferior.
    :param end: Límite superior.
    :param size: Número de valores a generar.
    :return: Lista de valores aleatorios.
    """
    return np.random.uniform(start, end, size).tolist()


def calculate_metrics(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    mse = np.mean((y_true - y_pred) ** 2)
    mae = np.mean(np.abs(y_true - y_pred))
    r2 = 1 - (np.sum((y_true - y_pred) ** 2) / np.sum((y_true - np.mean(y_true)) ** 2))
    return {"mse": round(mse, 4), "mae": round(mae, 4), "r2": round(r2, 4)}


def length_custom(obj):
    """
    Devuelve la longitud de un objeto compatible.
    """
    if isinstance(obj, (list, str, np.ndarray)):
        return len(obj)
    elif isinstance(obj, pd.DataFrame):
        return obj.shape[0]  # Filas en un DataFrame
    else:
        raise ValueError(f"El objeto de tipo {type(obj).__name__} no soporta la operación de longitud.")


def plot_regression(X_train, y_train, X_test, y_test, beta):
    X_all = np.vstack((X_train, X_test))
    y_pred = np.array([sum([b * x for b, x in zip(beta, [1] + list(row))]) for row in X_all])
    
    plt.scatter(X_train, y_train, label="Datos de entrenamiento", marker="o")
    plt.scatter(X_test, y_test, label="Predicciones", marker="x")
    plt.plot(X_all, y_pred, label="Línea ajustada", linestyle="--")
    plt.legend()
    plt.show()


def plot_dataframe(df, x_column, y_column, kind="line"):
    """
    Genera un gráfico a partir de un DataFrame.
    :param df: DataFrame a graficar.
    :param x_column: Nombre de la columna para el eje X.
    :param y_column: Nombre de la columna para el eje Y.
    :param kind: Tipo de gráfico ('line', 'bar', 'scatter', etc.).
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("El objeto proporcionado no es un DataFrame.")

    if x_column not in df.columns or y_column not in df.columns:
        raise ValueError(f"Las columnas '{x_column}' o '{y_column}' no existen en el DataFrame.")

    if kind == "line":
        df.plot(x=x_column, y=y_column, kind="line")
    elif kind == "bar":
        df.plot(x=x_column, y=y_column, kind="bar")
    elif kind == "scatter":
        df.plot(x=x_column, y=y_column, kind="scatter")
    else:
        raise ValueError(f"Tipo de gráfico no soportado: {kind}")

    plt.show()


def plotMLPPredictions(X_train, y_train, X_test, y_pred, title="MLP Predictions"):
    """
    Grafica los datos de entrenamiento, prueba y las predicciones realizadas por el MLP.
    :param X_train: Datos de entrada de entrenamiento (2D list or array).
    :param y_train: Etiquetas de entrenamiento (1D list or array).
    :param X_test: Datos de entrada de prueba (2D list or array).
    :param y_pred: Predicciones del modelo (1D list or array).
    :param title: Título opcional para el gráfico.
    """
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)
    y_pred = np.array(y_pred)

    # Verificar dimensiones
    if X_train.shape[1] != 2 or X_test.shape[1] != 2:
        raise ValueError("[ERROR] Solo se soportan gráficos para entradas de dimensión 2.")

    # Graficar datos de entrenamiento
    plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap="viridis", label="Entrenamiento")

    # Graficar predicciones
    plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap="coolwarm", label="Predicciones", marker='x')

    plt.title(title)
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.legend()
    plt.colorbar(label="Valor Predicho")
    plt.show()
