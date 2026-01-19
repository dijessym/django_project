from django.urls import path
from .views import complaint_list, feedback_api

urlpatterns = [
    path("", complaint_list, name="complaint_list"),
    path("api/", feedback_api, name="feedback_api"),
]
