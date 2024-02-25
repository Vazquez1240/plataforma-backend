# Generated by Django 4.2.9 on 2024-01-31 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("clases", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("alumnos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="alumno",
            name="clases",
            field=models.ManyToManyField(
                blank=True, related_name="alumnos_rel", to="clases.clase"
            ),
        ),
        migrations.AddField(
            model_name="alumno",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="alumno",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]