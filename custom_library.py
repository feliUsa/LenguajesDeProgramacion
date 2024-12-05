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


def mlp_fit(X, y, hidden_neurons=10, learning_rate=0.01, epochs=1000):
    """
    Entrena un perceptrón multicapa (MLP) con una capa oculta.
    """
    np.random.seed(42)  # Para reproducibilidad
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)
    input_neurons = X.shape[1]
    output_neurons = y.shape[1]

    # Inicialización de pesos
    W1 = np.random.randn(input_neurons, hidden_neurons) * 0.01
    b1 = np.zeros((1, hidden_neurons))
    W2 = np.random.randn(hidden_neurons, output_neurons) * 0.01
    b2 = np.zeros((1, output_neurons))

    for epoch in range(epochs):
        # Forward pass
        Z1 = X @ W1 + b1
        A1 = np.tanh(Z1)
        Z2 = A1 @ W2 + b2
        A2 = 1 / (1 + np.exp(-Z2))  # Sigmoide

        # Backward pass
        dZ2 = A2 - y
        dW2 = A1.T @ dZ2
        db2 = np.sum(dZ2, axis=0, keepdims=True)
        dZ1 = (dZ2 @ W2.T) * (1 - np.power(A1, 2))
        dW1 = X.T @ dZ1
        db1 = np.sum(dZ1, axis=0, keepdims=True)

        # Actualización de pesos
        W1 -= learning_rate * dW1
        b1 -= learning_rate * db1
        W2 -= learning_rate * dW2
        b2 -= learning_rate * db2

    return {"W1": W1.tolist(), "b1": b1.tolist(), "W2": W2.tolist(), "b2": b2.tolist()}

def mlp_predict(X, model):
    """
    Realiza predicciones con un modelo de MLP entrenado.
    """
    X = np.array(X)
    Z1 = X @ np.array(model["W1"]) + np.array(model["b1"])
    A1 = np.tanh(Z1)
    Z2 = A1 @ np.array(model["W2"]) + np.array(model["b2"])
    A2 = 1 / (1 + np.exp(-Z2))  # Sigmoide
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
    return {"mse": round(mse, 4)}



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
