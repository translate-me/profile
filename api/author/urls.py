from django.conf.urls import url
from author.views import (
    AddNewAuthor,
    UpdateAuthor,
    DestroyAuthor)
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Author API",
      default_version='v0',
      description="Test description",
   ),
   public=True,
   permission_classes=(AllowAny,),
)

urlpatterns = [
    url(r"^api/v0/create/$", AddNewAuthor.as_view(), name="create_author"),
    url(r"^api/v0/update/(?P<username>\w+)/$", UpdateAuthor.as_view(),
        name="update_author"),
    url(r"api/v0/destroy/(?P<username>\w+)/(?P<token>\w+)/$",
        DestroyAuthor.as_view(),
        name="destroy_author"),
]
