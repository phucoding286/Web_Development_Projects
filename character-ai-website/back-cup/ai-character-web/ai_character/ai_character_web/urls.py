from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home),
    # path("to_page/", views.to_page),
    path("hutao/", views.hutao_view, name="hutao_view"),
    path("keqing/", views.keqing_view, name="keqing_view"),
    path("yae/", views.yae_view, name="yae_view"),
    path("ei/", views.ei_view, name="ei_view"),
    path("ganyu/", views.ganyu_view, name="ganyu_view"),
]