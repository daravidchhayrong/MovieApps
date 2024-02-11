from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .movieAPI_ import MovieAPI
from .actorAPI_ import ActorAPI
router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("public/movie", MovieAPI.as_view()),
    path("public/actor", ActorAPI.as_view()),
]