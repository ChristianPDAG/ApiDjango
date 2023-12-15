from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from django.http import Http404

# Create your views here.
class UserList(APIView):
    def get(self, request):
        students = User.objects.all()
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
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
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