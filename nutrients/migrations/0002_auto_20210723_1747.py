# Generated by Django 3.2.5 on 2021-07-23 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutrients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertable',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='userfamilymember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutrients.usertable'),
        ),
    ]