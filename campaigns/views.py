from rest_framework import viewsets
from .models import Campaign
from .serializers import CampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all().order_by("-created_at")
    serializer_class = CampaignSerializer
    
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth


@api_view(["GET"])
def status_summary(request):
    data = (
        Campaign.objects.values("status")
        .annotate(count=Count("id"))
        .order_by("status")
    )
    return Response(data)


@api_view(["GET"])
def budget_by_platform(request):
    data = (
        Campaign.objects.values("platform")
        .annotate(total_budget=Sum("budget"))
        .order_by("platform")
    )
    return Response(data)


@api_view(["GET"])
def monthly_trends(request):
    data = (
        Campaign.objects.annotate(month=TruncMonth("created_at"))
        .values("month")
        .annotate(count=Count("id"))
        .order_by("month")
    )
    return Response(data)


import requests
from rest_framework.decorators import api_view


@api_view(["GET"])
def convert_currency(request):
    """
    Query params:
    ?amount=1000&from=INR&to=USD
    """
    amount = request.GET.get("amount")
    from_currency = request.GET.get("from")
    to_currency = request.GET.get("to")

    if not all([amount, from_currency, to_currency]):
        return Response(
            {"error": "amount, from, and to are required"},
            status=400,
        )

    url = "https://api.frankfurter.app/latest"
    params = {
        "amount": amount,
        "from": from_currency,
        "to": to_currency,
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        return Response({"error": "Currency API failed"}, status=500)

    return Response(response.json())
