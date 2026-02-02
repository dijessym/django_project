from django.shortcuts import render, get_object_or_404, redirect
from .models import Complaint
from .forms import ComplaintForm

def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(request, "feedback/complaint_list.html", {"complaints": complaints})

def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    return render(request, "feedback/complaint_detail.html", {"complaint": complaint})

def complaint_create(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("complaint_list")
    else:
        form = ComplaintForm()
    return render(request, "feedback/complaint_create.html", {"form": form})

