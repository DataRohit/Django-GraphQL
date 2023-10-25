from django.urls import path
from restapi import views

urlpatterns = [path("", views.RestAPIHome.as_view(), name="restapi__home")]
