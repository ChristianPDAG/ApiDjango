# Generated by Django 4.2.8 on 2023-12-16 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("perezdearceApp", "0003_usuarios_is_active_usuarios_is_staff_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usuarios",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="usuarios",
            name="is_staff",
        ),
        migrations.RemoveField(
            model_name="usuarios",
            name="last_login",
        ),
        migrations.AlterField(
            model_name="usuarios",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="usuarios",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="usuarios",
            name="password",
            field=models.CharField(max_length=20),
        ),
    ]