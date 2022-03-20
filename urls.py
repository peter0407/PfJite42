from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("peter", views.peter, name="peter"),
    path("birthday", views.greet, name="greet")

]
