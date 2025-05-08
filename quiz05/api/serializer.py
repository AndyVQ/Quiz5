from rest_framework import serializers
from .models import Paciente, Doctor, Especialidad, Cita, DoctorEspecialidad

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = "__all__"

class DoctorEspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorEspecialidad
        fields = "__all__"

class DoctorSerializer(serializers.ModelSerializer):
    especialidades = EspecialidadSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = "__all__"

    def create(self, validated_data):
        especialidades_data = validated_data.pop("especialidades", [])
        doctor = Doctor.objects.create(**validated_data)
        for especialidad_data in especialidades_data:
            especialidad, created = Especialidad.objects.get_or_create(**especialidad_data)
            DoctorEspecialidad.objects.create(doctor=doctor, especialidad=especialidad)
        return doctor

    def update(self, instance, validated_data):
        especialidades_data = validated_data.pop("especialidades", None)
        instance = super().update(instance, validated_data)

        if especialidades_data is not None:
            instance.doctorespecialidad_set.all().delete()
            for especialidad_data in especialidades_data:
                especialidad, created = Especialidad.objects.get_or_create(**especialidad_data)
                DoctorEspecialidad.objects.create(doctor=instance, especialidad=especialidad)
        return instance

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"

class CitaSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)
    paciente_id = serializers.PrimaryKeyRelatedField(queryset=Paciente.objects.all(), write_only=True)
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all(), write_only=True)

    class Meta:
        model = Cita
        fields = "__all__"
        extra_kwargs = {"paciente": {"read_only": True}, "doctor": {"read_only": True}}

    def create(self, validated_data):
        validated_data["paciente"] = validated_data.pop("paciente_id")
        validated_data["doctor"] = validated_data.pop("doctor_id")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "paciente_id" in validated_data:
            validated_data["paciente"] = validated_data.pop("paciente_id")
        if "doctor_id" in validated_data:
            validated_data["doctor"] = validated_data.pop("doctor_id")
        return super().update(instance, validated_data)