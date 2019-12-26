# Generated by Django 2.2.6 on 2019-12-26 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_name', models.CharField(max_length=50)),
                ('voter_age', models.IntegerField(null=True)),
                ('voter_city', models.CharField(max_length=50)),
                ('voter_county', models.CharField(max_length=50)),
                ('voter_address', models.CharField(max_length=100)),
                ('voter_vote', models.CharField(max_length=50)),
            ],
        ),
    ]
