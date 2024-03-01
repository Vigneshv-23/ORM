# Generated by Django 5.0.2 on 2024-02-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('copies', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
