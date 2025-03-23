from django.urls import path
from . import views
from .views import ReportingEntityList, ReportingPlanList, InNetworkFileList, AllowedAmountFileList

urlpatterns = [
    path('reporting-entities/', views.reporting_entity_list, name='reporting_entity_list'),
    path('reporting-entities/', ReportingEntityList.as_view(), name='reporting-entity-list'),
    path('reporting-plans/', ReportingPlanList.as_view(), name='reporting-plan-list'),
    path('in-network-files/', InNetworkFileList.as_view(), name='in-network-file-list'),
    path('allowed-amount-files/', AllowedAmountFileList.as_view(), name='allowed-amount-file-list'),
]
