# Generated by Django 5.1.2 on 2024-11-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unixni', '0005_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Pertanyaan')),
                ('answer', models.TextField(verbose_name='Jawaban')),
            ],
        ),
    ]