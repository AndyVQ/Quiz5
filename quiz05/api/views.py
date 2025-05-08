from rest_framework import generics
from .models import Paciente, Doctor, Especialidad, Cita, DoctorEspecialidad
from .serializer import PacienteSerializer, DoctorSerializer, EspecialidadSerializer, CitaSerializer, DoctorEspecialidadSerializer

class EspecialidadListCreateView(generics.ListCreateAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class EspecialidadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PacienteListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class CitaListCreateView(generics.ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class CitaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class DoctorEspecialidadListCreateView(generics.ListCreateAPIView):
    queryset = DoctorEspecialidad.objects.all()
    serializer_class = DoctorEspecialidadSerializer

class DoctorEspecialidadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorEspecialidad.objects.all()
    serializer_class = DoctorEspecialidadSerializer