from autor.models import Autor
from rest_framework import generics
from autor.serializers import AutorSerializer
from rest_framework.permissions import AllowAny
import requests as rq


class AddNewAutor(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def post(self, requests, *args, **kwargs):
        json = requests.data
        data = {"username": json['username'],
                "email": json['email'],
                "password": json['password'],
                }
        obj = rq.post("http://192.168.0.8:8090/user/api/v0/create/",
                      data=data)
        if obj.status_code != 201:
            raise "Erro"
        return self.create(requests, *args, **kwargs)
