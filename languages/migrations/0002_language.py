# Generated by Django 2.0 on 2019-10-21 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('paradigm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.Paradigm')),
            ],
        ),
    ]
