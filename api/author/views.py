import os
from datetime import date as dt
from author.models import Author
from django.http import JsonResponse
from rest_framework import generics
from author.serializers import (
    AuthorSerializer,
    AuthorSerializerUpdate
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticatedOrReadOnly
)
import requests as rq


class AddNewAuthor(generics.CreateAPIView):
    """
    create:
        create new author.
    """
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

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
    """
    update:
        update author.

    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializerUpdate
    lookup_field = 'username'
