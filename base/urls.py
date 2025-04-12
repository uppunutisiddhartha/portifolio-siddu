from base import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="index"),
    path("succes/",views.succes,name="succes"),
     path("contact/", views.contact_view, name="contact"),
]