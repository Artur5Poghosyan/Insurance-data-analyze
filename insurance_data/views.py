from django.shortcuts import render
from rest_framework import generics
from .models import ReportingEntity, ReportingPlan, InNetworkFile, AllowedAmountFile
from .serializers import ReportingEntitySerializer, ReportingPlanSerializer, InNetworkFileSerializer, AllowedAmountFileSerializer


def reporting_entity_list(request):
    """ 
    Create view for Report Entity table.
    return: context for html file.
    """
    reporting_entities = ReportingEntity.objects.all().prefetch_related(
        'reporting_plans__in_network_files',
        'reporting_plans__allowed_amount_files'
    )
    context = {
        'reporting_entities': reporting_entities
    }
    
    return render(request, 'insurance_data/reporting_entity_list.html', context)


class ReportingEntityList(generics.ListAPIView):
    """ A class for ReportingEntity api."""
    queryset = ReportingEntity.objects.all()
    serializer_class = ReportingEntitySerializer

class ReportingPlanList(generics.ListAPIView):
    """ A class for ReportingPlanList api."""
    queryset = ReportingPlan.objects.all()
    serializer_class = ReportingPlanSerializer

class InNetworkFileList(generics.ListAPIView):
    """ A class for InNetworkFileList api."""
    queryset = InNetworkFile.objects.all()
    serializer_class = InNetworkFileSerializer

class AllowedAmountFileList(generics.ListAPIView):
    """ A class for AllowedAmountFileList api."""
    queryset = AllowedAmountFile.objects.all()
    serializer_class = AllowedAmountFileSerializer

