from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, status_summary, budget_by_platform, monthly_trends
from .views import CampaignViewSet, status_summary, budget_by_platform, monthly_trends, convert_currency


router = DefaultRouter()
router.register(r"campaigns", CampaignViewSet, basename="campaign")

urlpatterns = [
    path("", include(router.urls)),
    path("reports/status-summary/", status_summary),
    path("reports/budget-by-platform/", budget_by_platform),
    path("reports/monthly-trends/", monthly_trends),
    path("tools/convert-currency/", convert_currency),

]
