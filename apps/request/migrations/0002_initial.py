# Generated by Django 4.2.7 on 2023-11-23 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('request', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_requesst', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productrequest',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='productrequest',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.request'),
        ),
    ]
