from django.urls import path
from restapi import views

urlpatterns = [path("", views.RestAPIHome, name="restapi__graphql")]
