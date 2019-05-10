from author.models import Author
from rest_framework import generics
from author.serializers import AuthorSerializer
from rest_framework.permissions import AllowAny
import requests as rq


class AddNewAuthor(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def post(self, requests, *args, **kwargs):
        json = requests.data
        data = {"username": json['username'],
                "email": json['email'],
                "password": json['password'],
                }
        obj = rq.post("http://192.168.0.15:8090/user/api/v0/create/",
                      data=data)
        if obj.status_code != 201:
            raise "Erro"
        return self.create(requests, *args, **kwargs)
