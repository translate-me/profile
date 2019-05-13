from django.conf.urls import url
from author.views import AddNewAuthor, UpdateAuthor
# from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    url(r"^api/v0/create/$", AddNewAuthor.as_view(), name="create_author"),
    url(r"^api/v0/update/(?P<username>\w+)/$", UpdateAuthor.as_view(),
        name="update_author"),
]
