from django.conf.urls import url
from author.views import AddNewAuthor

urlpatterns = [
    url(r"^api/v0/create/$", AddNewAuthor.as_view(), name="create_author")
]
