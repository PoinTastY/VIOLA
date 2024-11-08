from numpy import double

class CarreraUniversitaria:
    def __init__(self, id : int = 0, nombre: str = "", area: str = "", duracion: double = 0):
        self.id = id
        self.nombre = nombre
        self.area = area
        self.duracion = duracion

    def __str__(self):
        return f"CarreraUniversitaria(id={self.id}, nombre='{self.nombre}', area='{self.area}', duracion='{self.duracion}')"

    def __repr__(self):
        return str(self)