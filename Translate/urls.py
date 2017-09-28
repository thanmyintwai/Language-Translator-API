from django.conf.urls import url,include

from rest_framework.routers import SimpleRouter
from .views import TranslateView


urlpatterns=[

    url(r'^', TranslateView.as_view(), name="transltor")

]
