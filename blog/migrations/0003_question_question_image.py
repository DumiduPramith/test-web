# Generated by Django 3.0.6 on 2020-06-20 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_question_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, upload_to='question_pics'),
        ),
    ]
