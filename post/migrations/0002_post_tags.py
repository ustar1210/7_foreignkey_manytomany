# Generated by Django 4.1 on 2023-03-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="tags", to="post.tag"
            ),
        ),
    ]
