# Generated by Django 4.2.2 on 2023-06-15 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0003_answer_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="modified_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="modified_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]