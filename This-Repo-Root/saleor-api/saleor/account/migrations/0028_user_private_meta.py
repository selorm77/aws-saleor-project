# Generated by Django 2.2.1 on 2019-05-31 10:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations

import saleor.core.utils.json_serializer


class Migration(migrations.Migration):
    dependencies = [("account", "0027_customerevent")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="private_meta",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True,
                default=dict,
                encoder=saleor.core.utils.json_serializer.CustomJsonEncoder,
            ),
        )
    ]
