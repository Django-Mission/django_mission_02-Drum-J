# Generated by Django 4.0.3 on 2022-04-13 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qus', models.TextField(verbose_name='질문')),
                ('ans', models.TextField(verbose_name='답변')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
            ],
        ),
    ]
