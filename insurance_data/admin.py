from django.contrib import admin
from .models import ReportingEntity, ReportingPlan, InNetworkFile, AllowedAmountFile

admin.site.register(ReportingEntity)
admin.site.register(ReportingPlan)
admin.site.register(InNetworkFile)
admin.site.register(AllowedAmountFile)