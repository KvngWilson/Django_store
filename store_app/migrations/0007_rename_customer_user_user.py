# Generated by Django 4.2.16 on 2024-11-13 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0006_user_customer_alter_order_customer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='customer',
            new_name='user',
        ),
    ]
