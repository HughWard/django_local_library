# Generated by Django 2.2.5 on 2019-10-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='house.png', upload_to='images/'),
        ),
    ]