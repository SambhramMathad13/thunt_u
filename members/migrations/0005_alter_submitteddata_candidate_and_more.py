# Generated by Django 4.2.6 on 2024-02-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_submitteddata_candidate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitteddata',
            name='candidate',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='submitteddata',
            name='list',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='submitteddata',
            name='time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]