from django.shortcuts import render
from .serializers import UserSerializer
from .models import Usuarios
from .forms import UserForm
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from django.http import Http404
from django.contrib.auth import get_user_model

# Create your views here. API
class UserList(APIView):
    def get(self, request):
        students = Usuarios.objects.all()
        serializer = UserSerializer(students,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self,pk):
        try:
            return Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = UserSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = UserSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        student= self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Create AppWeb
    
#navbar
def barra_navegacion(request):
    # Lógica para obtener datos necesarios para la barra de navegación
    datos_navegacion = {
        'enlace1': 'Enlace 1',
        'enlace2': 'Enlace 2',
        'enlace3': 'Enlace 3',
        # Otros datos necesarios
    }
    return render(request, 'navbar.html', {'datos_navegacion': datos_navegacion})
    
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            
            form.save()
    return render(request,'formulario_user.html',{'form' : form})