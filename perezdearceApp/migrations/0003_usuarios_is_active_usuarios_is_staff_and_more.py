# Generated by Django 4.2.8 on 2023-12-16 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("perezdearceApp", "0002_rename_user_usuarios"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuarios",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="usuarios",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="usuarios",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AlterField(
            model_name="usuarios",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="usuarios",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="usuarios",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]
