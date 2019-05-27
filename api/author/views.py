import socket
from datetime import date as dt
from author.models import Author
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from author.serializers import (
    AuthorSerializer,
    AuthorSerializerUpdate,
    SwaggerSerializer
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticatedOrReadOnly
)
from drf_yasg.utils import swagger_auto_schema
import requests as rq


class AddNewAuthor(generics.CreateAPIView):

    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @swagger_auto_schema(request_body=SwaggerSerializer,
                         responses={200: AuthorSerializer},
                         operation_description="Add new author.")
    def post(self, requests, *args, **kwargs):
        json = requests.data
        today = dt.today()
        date = today.strftime("%Y-%m-%d")
        data = {"username": json['username'],
                "email": json['email'],
                "password": json['password'],
                "data_joined": date
                }
        host = socket.gethostbyname('authentication_django')
        obj = rq.post("http://"+host+":8090/user/api/v0/create/",
                      data=data)
        if obj.status_code != 201 and obj.status_code != 200:
            message = obj.reason
            response = JsonResponse({'status': 'false', 'message': message},
                                    status=obj.status_code)
            return response
        return self.create(requests, *args, **kwargs)


class UpdateAuthor(generics.UpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'username'

    @swagger_auto_schema(request_body=AuthorSerializerUpdate,
                         responses={200: AuthorSerializerUpdate},
                         operation_description="Update Author")
    def put(self, requests, *args, **kwargs):
        author = Author.objects.get(username=requests.username)
        serializer = AuthorSerializerUpdate(author, data=requests.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AuthorSerializerUpdate,
                         responses={200: AuthorSerializerUpdate},
                         operation_description="Update Author")
    def patch(self, requests, *args, **kwargs):
        author = Author.objects.get(username=requests.username)
        serializer = AuthorSerializerUpdate(author, data=requests.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class DestroyAuthor(generics.DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AuthorSerializer
    lookup_field = 'username'

    def get_queryset(self):
        username = self.kwargs.get('username', None)
        queryset = Author.objects.filter(username=username)
        return queryset

    @swagger_auto_schema(request_body=AuthorSerializer,
                         responses={200: "Delete is ok"},
                         operation_description="Delete one author")
    def perform_destroy(self, instance):
        serializer = AuthorSerializer(data=self.get_queryset())
        serializer.is_valid()
        myToken = 'Token {}'.format(self.kwargs.get('token', None))
        auth = {'Authorization': myToken}
        host = socket.gethostbyname('authentication_django')
        response = rq.delete("http://"+host +
                             ":8090/user/api/v0/destroy/"
                             + instance.username + "/",
                             headers=auth)
        if response.status_code <= 200 and response.status_code >= 300:
            message = response.reason
            resp = JsonResponse({'status': 'false', 'message': message},
                                status=response.status_code)
            return resp

        return instance.delete()
