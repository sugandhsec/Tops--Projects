# Generated by Django 4.2.2 on 2023-07-06 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_seller', '0001_initial'),
        ('app_buyer', '0002_user_propic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0)),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_buyer.user')),
                ('prd_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_seller.product')),
            ],
        ),
    ]