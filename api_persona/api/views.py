from rest_framework import viewsets

from api.models import Persona, Docentes, Estudiantes
from api.serializers import PersonaSerializer, DocentesSerializer, EstudiantesSerializer

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
import requests
 
class DocentesViewSet (viewsets.ModelViewSet):
    serializer_class = DocentesSerializer
    queryset = Docentes.objects.all()
    
class EstudiantesViewSet (viewsets.ModelViewSet):
    serializer_class = EstudiantesSerializer
    queryset = Estudiantes.objects.all()
    
class PersonaViewSet (viewsets.ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()
    
    @action(detail=True, methods=['patch'])
    def completardatos(self, request: Request, *args, **kwargs):
        #extrae el id del cliente enviado en la url
        id = kwargs['pk']  
        #extrae el id del cliente enviado en la url
        #consulta de base de datos el id solicitado
        persona = Persona.objects.get(pk=id)
        #consulta de la api extrerna datos segun el identificados proporcionado
        response = requests.get("https://jsonplaceholder.typicode.com/users/"+id)
        #en caso de una respuesta satisfactoria de la api externa, se produce a completar datos
        #en base de datos y se retorna la respuesta al cliente
        if response.status_code ==200:
            data = response.json()
            persona.email = data['email']
            persona.phone = data['phone']
            persona.save()
            #prepara un serializador para mapear la entidad a JSON
            serializer = PersonaSerializer(persona)
            #regresa una respuesta http con la nueva data del cliente
            return Response(serializer.data, content_type="application/json")
        else:
            #si hubo un error en la consulta, devolver un mensaje de error
            return Response("Error en la consulta a la API externa", status=500) 