# Generated by Django 4.2.2 on 2023-07-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quicklink', '0002_alter_access_user_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirect',
            name='key',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
