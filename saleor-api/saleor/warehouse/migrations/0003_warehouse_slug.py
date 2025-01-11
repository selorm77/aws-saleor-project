# Generated by Django 2.2.9 on 2020-01-29 06:52

from django.db import migrations, models
from django.db.models.functions import Lower
from django.utils.text import slugify

DEFAULT_SLUG_VALUE = "warehouse"


def create_unique_slug_for_warehouses(apps, schema_editor):
    Warehouse = apps.get_model("warehouse", "Warehouse")

    warehouses = (
        Warehouse.objects.filter(slug__isnull=True).order_by(Lower("name")).iterator()
    )
    previous_char = None
    slug_values = []
    for warehouse in warehouses:
        if warehouse.name:
            first_char = warehouse.name[0].lower()
            if first_char != previous_char:
                previous_char = first_char
                slug_values = list(
                    Warehouse.objects.filter(slug__istartswith=first_char).values_list(
                        "slug", flat=True
                    )
                )
        elif previous_char is None:
            previous_char = ""
            slug_values = list(
                Warehouse.objects.filter(
                    slug__istartswith=DEFAULT_SLUG_VALUE
                ).values_list("slug", flat=True)
            )

        slug = generate_unique_slug(warehouse, slug_values)
        warehouse.slug = slug
        warehouse.save(update_fields=["slug"])
        slug_values.append(slug)


def generate_unique_slug(instance, slug_values):
    slug = slugify(instance.name) if instance.name else DEFAULT_SLUG_VALUE
    unique_slug = slug
    extension = 1

    while unique_slug in slug_values:
        extension += 1
        unique_slug = f"{slug}-{extension}"

    return unique_slug


class Migration(migrations.Migration):
    dependencies = [
        ("warehouse", "0002_auto_20200123_0036"),
    ]

    operations = [
        migrations.AddField(
            model_name="warehouse",
            name="slug",
            field=models.SlugField(null=True, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.RunPython(
            create_unique_slug_for_warehouses, migrations.RunPython.noop
        ),
        migrations.AlterField(
            model_name="warehouse",
            name="slug",
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
