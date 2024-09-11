# Comentario de ejemplo
False
None
True

def funcion_ejemplo():
    global x
    x = 0
    while x < 5:
        if x == 2:
            continue
        elif x == 4:
            break
        else:
            x += 1

try:
    import math as m
    assert m.sqrt(4) == 2
except AssertionError:
    pass
finally:
    print("Prueba finalizada")

class MiClase:
    def __init__(self):
        self.valor = lambda: 'valor de ejemplo'

    def metodo(self):
        with open('archivo.txt', 'w') as f:
            f.write('Contenido')

for i in range(3):
    print(i)

x = [1, 2, 3]
y = [n * 2 for n in x if n > 1]

def decorador(func):
    def wrapper(*args, **kwargs):
        print("Llamada decorada")
        return func(*args, **kwargs)
    return wrapper
