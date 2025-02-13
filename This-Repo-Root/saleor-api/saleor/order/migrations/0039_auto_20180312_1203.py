# Generated by Django 2.0.2 on 2018-03-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("order", "0038_auto_20180228_0451")]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="total_gross",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name="order",
            name="total_net",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
