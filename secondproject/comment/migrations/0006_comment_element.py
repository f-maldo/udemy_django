# Generated by Django 3.0.8 on 2020-07-08 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listelement', '0002_auto_20200706_1620'),
        ('comment', '0005_contact_type_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='element',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listelement.Element'),
        ),
    ]