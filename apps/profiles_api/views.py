from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class Cabify(APIView):
    ''' Esta clase hace un request a cabify, ordena y filtra los valores '''

    def get(self, request, format=None):
        ''' Return the dict cabify '''

        valores_cabify = {
            'valor1':'Este es el primer valor',
            'valor2':'Este es el segundo valor',
            'valor3':'Aqui el tercer valor'
        }
        return Response({'Resultados': valores_cabify})

