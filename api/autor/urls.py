from django.conf.urls import url
from autor.views import AddNewAutor

urlpatterns = [
    url(r"^api/v0/create/$", AddNewAutor.as_view(), name="create_autor")
]
