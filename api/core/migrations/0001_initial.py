# Generated by Django 3.2.6 on 2021-08-17 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaterPlants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('position', models.CharField(max_length=50)),
                ('picture', models.FileField(upload_to='')),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=10)),
                ('addition_amount', models.CharField(choices=[('Low', 'Low'), ('Middle', 'Middle'), ('High', 'High')], max_length=10)),
                ('leaf_length', models.PositiveIntegerField()),
                ('water_quality', models.TextField()),
            ],
        ),
    ]
