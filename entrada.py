# Esto es un comentario
class Animal:
    """Clase que representa un Animal"""
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Sonido genérico"

# Crear una instancia de la clase
a = Animal('Fido')
print(a.hacer_sonido())

if a.nombre == 'Fido' and not a.nombre == '':
    print("El nombre es Fido")
