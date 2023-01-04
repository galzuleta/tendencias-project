from rest_framework import serializers
from api.models import Persona, Docentes, Estudiantes

class PersonaSerializer (serializers.ModelSerializer):
    class Meta:
        model= Persona
        fields = '__all__'
        
        
class DocentesSerializer (serializers.ModelSerializer):
    class Meta:
        model= Docentes
        fields = '__all__'

class EstudiantesSerializer (serializers.ModelSerializer):
    class Meta:
        model= Estudiantes
        fields = '__all__'