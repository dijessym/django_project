from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from feedback.models import Complaint
from .serializers import ComplaintSerializer


@api_view(["GET", "POST"])
def complaints_api(request):
    print(">>> API complaints_api CALLED, method =", request.method)

    # GET: list
    if request.method == "GET":
        qs = Complaint.objects.all().order_by("-id")
        serializer = ComplaintSerializer(qs, many=True)
        return Response(serializer.data)

    # POST: create
    serializer = ComplaintSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def complaint_detail_api(request, pk):
    print(">>> API complaint_detail_api CALLED, method =", request.method, "pk =", pk)

    obj = get_object_or_404(Complaint, pk=pk)

    # GET: detail
    if request.method == "GET":
        serializer = ComplaintSerializer(obj)
        return Response(serializer.data)

    # PUT: update
    if request.method == "PUT":
        serializer = ComplaintSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: delete
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




