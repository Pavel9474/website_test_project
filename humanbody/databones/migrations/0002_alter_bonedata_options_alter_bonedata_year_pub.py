# Generated by Django 5.0.3 on 2024-03-28 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databones', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bonedata',
            options={'verbose_name': 'BoneData', 'verbose_name_plural': 'BoneData'},
        ),
        migrations.AlterField(
            model_name='bonedata',
            name='year_pub',
            field=models.CharField(max_length=4, verbose_name='Год публикации'),
        ),
    ]
