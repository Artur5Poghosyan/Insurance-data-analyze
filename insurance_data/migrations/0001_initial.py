# Generated by Django 5.1.1 on 2025-03-22 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporting_entity_name', models.CharField(max_length=255)),
                ('reporting_entity_type', models.CharField(max_length=255)),
                ('last_updated_on', models.DateField()),
                ('version', models.CharField(max_length=50)),
            ],
        ),
    ]
