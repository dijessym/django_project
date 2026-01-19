from django.contrib import admin
from .models import Category, Complaint


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "status", "created_at")
    list_filter = ("status", "category", "created_at")
    search_fields = ("title", "description")
    ordering = ("-created_at",)


