# Generated by Django 3.2.13 on 2022-06-21 08:50

import django.contrib.postgres.indexes
from django.db import migrations, models

import saleor.core.utils.json_serializer


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0153_merge_20220615_1232"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderline",
            name="metadata",
            field=models.JSONField(
                blank=True,
                default=dict,
                encoder=saleor.core.utils.json_serializer.CustomJsonEncoder,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="orderline",
            name="private_metadata",
            field=models.JSONField(
                blank=True,
                default=dict,
                encoder=saleor.core.utils.json_serializer.CustomJsonEncoder,
                null=True,
            ),
        ),
        # nosemgrep: add-index-concurrently
        migrations.AddIndex(
            model_name="orderline",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["private_metadata"], name="orderline_p_meta_idx"
            ),
        ),
        # nosemgrep: add-index-concurrently
        migrations.AddIndex(
            model_name="orderline",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["metadata"], name="orderline_meta_idx"
            ),
        ),
    ]
