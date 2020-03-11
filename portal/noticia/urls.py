from django.urls import path

from .views import NoticiaView

app_name = "noticia"

urlpatterns = [
    path("noticias/", NoticiaView.as_view()),
    path("noticias/<int:pk>", NoticiaView.as_view()),
]
