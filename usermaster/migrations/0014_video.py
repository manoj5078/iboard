# Generated by Django 4.0 on 2022-01-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermaster', '0013_gaugesmachine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
            ],
        ),
    ]
