# Generated by Django 4.0.3 on 2022-03-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Input_Uri', models.CharField(max_length=255, verbose_name='Input URI')),
            ],
        ),
    ]