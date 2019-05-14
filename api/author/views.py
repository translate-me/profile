import os
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
        obj = rq.post(os.environ["HTTP_IP"]+":8090/user/api/v0/create/",
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
