# Generated by Django 4.0.1 on 2022-01-26 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courseCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classtitle', models.CharField(max_length=200)),
                ('classTime', models.CharField(max_length=200)),
            ],
        ),
    ]