from apps.adopcion.models import Persona
from rest_framework import serializers


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellidos', 'edad', 'email')