from django.urls import path
from . import views

urlpatterns = [
    path("especialidades/", views.EspecialidadListCreateView.as_view(), name="especialidad-list-create"),
    path("especialidades/<int:pk>/", views.EspecialidadRetrieveUpdateDestroyView.as_view(), name="especialidad-retrieve-update-destroy"),

    path("doctores/", views.DoctorListCreateView.as_view(), name="doctor-list-create"),
    path("doctores/<int:pk>/", views.DoctorRetrieveUpdateDestroyView.as_view(), name="doctor-retrieve-update-destroy"),

    path("pacientes/", views.PacienteListCreateView.as_view(), name="paciente-list-create"),
    path("pacientes/<int:pk>/", views.PacienteRetrieveUpdateDestroyView.as_view(), name="paciente-retrieve-update-destroy"),

    path("citas/", views.CitaListCreateView.as_view(), name="cita-list-create"),
    path("citas/<int:pk>/", views.CitaRetrieveUpdateDestroyView.as_view(), name="cita-retrieve-update-destroy"),

    path("doctorespecialidades/", views.DoctorEspecialidadListCreateView.as_view(), name="doctorespecialidad-list-create"),
    path("doctorespecialidades/<int:pk>/", views.DoctorEspecialidadRetrieveUpdateDestroyView.as_view(), name="doctorespecialidad-retrieve-update-destroy"),
]