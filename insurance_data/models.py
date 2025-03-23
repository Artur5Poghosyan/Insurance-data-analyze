from django.db import models

class ReportingEntity(models.Model):
    """ A class for processing ReportingEntity table."""
    reporting_entity_name = models.CharField(max_length=255)
    reporting_entity_type = models.CharField(max_length=255)

    def __str__(self):
        return self.reporting_entity_name

class ReportingPlan(models.Model):
    """ A class for processing ReportingPlan table."""
    reporting_entity = models.ForeignKey(ReportingEntity, related_name='reporting_plans', on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=255)
    plan_id_type = models.CharField(max_length=50)
    plan_id = models.CharField(max_length=50)
    plan_market_type = models.CharField(max_length=50)

    def __str__(self):
        return self.plan_name

class InNetworkFile(models.Model):
    """ A class for processing InNetworkFile table."""
    reporting_plan = models.ForeignKey(ReportingPlan, related_name='in_network_files', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    location = models.URLField()

    def __str__(self):
        return self.description

class AllowedAmountFile(models.Model):
    """ A class for processing AllowedAmountFile table."""
    reporting_plan = models.ForeignKey(ReportingPlan, related_name='allowed_amount_files', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    location = models.URLField()

    def __str__(self):
        return self.description









# from django.db import models

# class ReportData(models.Model):
#     reporting_entity_name = models.CharField(max_length=255)
#     reporting_entity_type = models.CharField(max_length=255)
#     last_updated_on = models.DateField()
#     version = models.CharField(max_length=50)

#     def __str__(self):
#         return self.reporting_entity_name
