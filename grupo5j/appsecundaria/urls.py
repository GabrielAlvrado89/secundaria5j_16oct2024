from appsecundaria import views
from django.urls import path

urlpatterns = [
    path("",views.Index_vista,name="Index_vista")
]
