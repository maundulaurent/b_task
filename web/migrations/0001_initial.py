# Generated by Django 5.0.1 on 2024-01-13 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=20)),
                ('psw', models.CharField(max_length=100)),
            ],
        ),
    ]