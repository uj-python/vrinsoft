# Generated by Django 3.2.8 on 2022-01-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userregistration_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='ProfilePicture',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]