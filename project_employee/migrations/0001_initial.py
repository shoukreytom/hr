# Generated by Django 3.1.5 on 2021-01-12 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectEmployee',
            fields=[
                ('pnumber', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=250)),
                ('plocation', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Project Employee',
            },
        ),
    ]
