# Generated by Django 4.1.7 on 2023-03-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('site', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
