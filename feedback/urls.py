from django.urls import path
from . import views
from .api_views import complaints_api, complaint_detail_api

urlpatterns = [
    path("", views.complaint_list, name="complaint_list"),
    path("complaints/create/", views.complaint_create, name="complaint_create"),
    path("complaints/<int:pk>/", views.complaint_detail, name="complaint_detail"),

    path("api/complaints/", complaints_api, name="api_complaints"),
    path("api/complaints/<int:pk>/", complaint_detail_api, name="api_complaint_detail"),
]

