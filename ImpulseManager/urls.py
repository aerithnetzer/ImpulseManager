from django.urls import path
from JobViewer import views

app_name = "JobViewer"

urlpatterns = [
    path("", views.index, name="index"),
]
