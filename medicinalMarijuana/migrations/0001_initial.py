# Generated by Django 4.2.2 on 2023-09-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadStrainToDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strain_name', models.CharField(max_length=20)),
                ('thc', models.IntegerField()),
                ('effect', models.CharField(max_length=50)),
                ('cost_blunt', models.IntegerField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='strains')),
            ],
        ),
    ]
