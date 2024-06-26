# Generated by Django 5.0.3 on 2024-05-01 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_no',
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='static/profile_pictures', null=True, upload_to='profile_pictures'),
        ),
    ]
