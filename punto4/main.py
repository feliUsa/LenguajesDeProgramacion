import time

N = 100000000
suma = 0

inicio = time.time()

for i in range(1, N + 1):
    suma += i

fin = time.time()
tiempo = fin - inicio

print(f"Suma en Python: {suma}")
print(f"Tiempo de ejecución en Python: {tiempo} segundos")
