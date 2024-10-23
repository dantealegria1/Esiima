
from django.db import models

class Estudiante(models.Model):
    """
    Modelo que representa a un estudiante.
    """
    nombre: str = models.CharField(max_length=100)
    matricula: str = models.CharField(max_length=10, unique=True)
    carrera: str = models.CharField(max_length=100)
    fecha_nacimiento: str = models.DateField()

    def __str__(self) -> str:
        return self.nombre


class Materia(models.Model):
    """
    Modelo que representa una materia.
    """
    nombre_materia: str = models.CharField(max_length=100)
    clave_materia: str = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.nombre_materia


class Calificacion(models.Model):
    """
    Modelo que representa la calificación de un estudiante en una materia.
    """
    estudiante: Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia: Materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    calificacion: float = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.estudiante} - {self.materia}'
