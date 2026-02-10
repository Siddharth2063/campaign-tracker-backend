from django.contrib import admin
from .models import Campaign


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "platform",
        "status",
        "budget",
        "currency",
        "start_date",
        "end_date",
        "created_at",
    )

    list_filter = ("platform", "status")
    search_fields = ("name",)
