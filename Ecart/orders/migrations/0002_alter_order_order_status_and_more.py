# Generated by Django 5.0.6 on 2024-07-23 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(0, 'Cart'), (1, 'Order Confirmed'), (2, 'Order Processed'), (3, 'Order Delivered'), (4, 'Order Rejected')], default=0),
        ),
        migrations.AlterUniqueTogether(
            name='ordereditem',
            unique_together={('product', 'owner')},
        ),
    ]
