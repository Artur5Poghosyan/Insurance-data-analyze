from rest_framework import serializers
from .models import ReportingEntity, ReportingPlan, InNetworkFile, AllowedAmountFile

class ReportingEntitySerializer(serializers.ModelSerializer):
    """ A class for serialize ReportingEntity model."""
    class Meta:
        model = ReportingEntity
        fields = '__all__'

class ReportingPlanSerializer(serializers.ModelSerializer):
    """ A class for serialize ReportingPlan model."""
    class Meta:
        model = ReportingPlan
        fields = '__all__'

class InNetworkFileSerializer(serializers.ModelSerializer):
    """ A class for serialize InNetworkFile model."""
    class Meta:
        model = InNetworkFile
        fields = '__all__'

class AllowedAmountFileSerializer(serializers.ModelSerializer):
    """ A class for serialize AllowedAmountFile model."""
    class Meta:
        model = AllowedAmountFile
        fields = '__all__'