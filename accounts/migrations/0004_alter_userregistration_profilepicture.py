# Generated by Django 3.2.8 on 2022-01-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userregistration_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='ProfilePicture',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]