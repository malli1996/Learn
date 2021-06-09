from os import name
from django.conf.urls import url
from deployment import views


urlpatterns = [
    url("login", views.log, name="log"),
    url("model_form_upload/", views.model_form_upload, name="model_form_upload"),
    url("upload_form/", views.upload_form, name="upload_form"),
]
