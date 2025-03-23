import json
from django.core.management.base import BaseCommand
from insurance_data.models import ReportingEntity, ReportingPlan, InNetworkFile, AllowedAmountFile

class Command(BaseCommand):
    help = 'Load large JSON data into PostgreSQL database'

    def handle(self, *args, **kwargs):
        """
        Handle json file: 
            1. Clean existing data from database
            2. Read, parse data from json
            3. Store in PostgreSQL database
        """
        # Delete existing data
        ReportingEntity.objects.all().delete()
        ReportingPlan.objects.all().delete()
        InNetworkFile.objects.all().delete()
        AllowedAmountFile.objects.all().delete()
        
        json_file_path = 'insurance_data/data/new_data.json'

        # Process JSON file in chunks
        with open(json_file_path, 'r') as file:
            data = json.load(file)

            # Process ReportingEntity
            reporting_entity, created = ReportingEntity.objects.get_or_create(
                reporting_entity_name=data['reporting_entity_name'],
                defaults={
                    'reporting_entity_type': data['reporting_entity_type']
                }
            )

            # Process ReportingPlans and related files
            for reporting_structure in data['reporting_structure']:
                for reporting_plan_data in reporting_structure['reporting_plans']:
                    reporting_plan, created = ReportingPlan.objects.get_or_create(
                        reporting_entity=reporting_entity,
                        plan_name=reporting_plan_data['plan_name'],
                        defaults={
                            'plan_id_type': reporting_plan_data['plan_id_type'],
                            'plan_id': reporting_plan_data['plan_id'],
                            'plan_market_type': reporting_plan_data['plan_market_type']
                        }
                    )

                    # Process InNetworkFiles
                    for in_network_file_data in reporting_structure['in_network_files']:
                        InNetworkFile.objects.get_or_create(
                            reporting_plan=reporting_plan,
                            description=in_network_file_data['description'],
                            defaults={
                                'location': in_network_file_data['location']
                            }
                        )

                    # Process AllowedAmountFile
                    allowed_amount_file_data = reporting_structure['allowed_amount_file']
                    AllowedAmountFile.objects.get_or_create(
                        reporting_plan=reporting_plan,
                        description=allowed_amount_file_data['description'],
                        defaults={
                            'location': allowed_amount_file_data['location']
                        }
                    )

        self.stdout.write(self.style.SUCCESS('Successfully loaded JSON data into PostgreSQL'))