# Generated by Django 3.2.17 on 2024-01-15 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0005_delete_financialdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialdetails',
            name='industry',
            field=models.CharField(blank=True, choices=[('OPTION_ONE', 'Option 1'), ('OPTION_TWO', 'Option 2'), ('OPTION_THREE', 'Option 3')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='forecastedfinancialdetails',
            name='industry',
            field=models.CharField(blank=True, choices=[('OPTION_ONE', 'Option 1'), ('OPTION_TWO', 'Option 2'), ('OPTION_THREE', 'Option 3')], max_length=20, null=True),
        ),
    ]
