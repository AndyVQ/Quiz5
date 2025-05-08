from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Doctor(models.Model):
    nombre = models.CharField(max_length=150)
    años_experiencia = models.IntegerField()
    especialidades = models.ManyToManyField(Especialidad, through="DoctorEspecialidad")

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=150)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class DoctorEspecialidad(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("doctor", "especialidad")

    def __str__(self):
        return f"{self.doctor.nombre} - {self.especialidad.nombre}"

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"Cita de {self.paciente.nombre} con {self.doctor.nombre} el {self.fecha} a las {self.hora}"
