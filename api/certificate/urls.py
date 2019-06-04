from django.conf.urls import url
from certificate.views import (AddCertificateView, ListCertificateView)

urlpatterns = [
    # language
    url(r"^api/v0/create/certificate/$", AddCertificateView.as_view(),
        name="create_certificate"),
    url(r"^api/v0/list/certificate/$", ListCertificateView.as_view(),
        name="create_certificate"),
]