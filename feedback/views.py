from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Complaint


def complaint_list(request):
    complaints = Complaint.objects.select_related("category").all()
    return render(
        request,
        "feedback/complaint_list.html",
        {"complaints": complaints},
    )


@csrf_exempt
def feedback_api(request):
    if request.method == "GET":
        complaints = Complaint.objects.select_related("category").all()
        data = [
            {
                "id": c.id,
                "title": c.title,
                "description": c.description,
                "category": c.category.name,
                "status": c.status,
            }
            for c in complaints
        ]
        return JsonResponse(data, safe=False)

    if request.method == "POST":
        body = json.loads(request.body)
        c = Complaint.objects.create(
            title=body["title"],
            description=body["description"],
            category_id=body["category_id"],
            status="open",
        )
        return JsonResponse({"message": "Created", "id": c.id})
