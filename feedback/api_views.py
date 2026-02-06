from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Complaint
from .serializers import ComplaintSerializer

@api_view(["GET"])
def complaints_api(request):
    qs = Complaint.objects.all().order_by("-id")
    return Response(ComplaintSerializer(qs, many=True).data)

@api_view(["GET"])
def complaint_detail_api(request, pk):
    obj = get_object_or_404(Complaint, pk=pk)
    return Response(ComplaintSerializer(obj).data)
