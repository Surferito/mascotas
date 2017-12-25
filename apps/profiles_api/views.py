from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers, models, permissions
from rest_framework import status

class Cabify(APIView):
    ''' Esta clase hace un request a cabify, ordena y filtra los valores '''

    serializer_class = serializers.CabifySerializer

    def get(self, request, format=None):
        ''' Return the dict cabify '''

        valores_cabify = {
            'valor1':'Este es el primer valor',
            'valor2':'Este es el segundo valor',
            'valor3':'Aqui el tercer valor'
        }
        return Response({'Resultados': valores_cabify})

    def post(self, request):
        ''' Create a message with the variable that receives '''

        print('imprimimos request.data: ', request.data)

        serializer = serializers.CabifySerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            surname = serializer.data.get('surname')
            print('variable name: ', name, 'variable surname: ', surname)

            message = 'Devolviendo el nombre recibido: {}, apellido: {}'.format(name, surname)
            return Response({'mensaje': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        ''' Handles updating an object '''

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        ''' Only updates fields provided in the request '''

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        ''' Deletes an object '''

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.CabifySerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.CabifySerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            surname = serializer.data.get('surname')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)