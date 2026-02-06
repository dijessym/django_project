from django.urls import path
from .views import complaints_api, complaint_detail_api

urlpatterns = [
    path("complaints/", complaints_api),
    path("complaints/<int:pk>/", complaint_detail_api),
]



