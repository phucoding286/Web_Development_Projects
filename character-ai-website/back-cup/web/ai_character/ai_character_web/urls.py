from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home),
    path("to_page/", views.to_page),
    path("llm_response/", views.llm_response),
]