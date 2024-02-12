# Generated by Django 5.0 on 2024-01-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0009_alter_financialdata_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormulaValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revised_tag', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=255)),
                ('audited', models.BooleanField()),
                ('standalone', models.BooleanField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('period', models.DateField()),
            ],
        ),
    ]
