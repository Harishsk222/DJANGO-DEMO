# Generated by Django 4.1.2 on 2022-11-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Factories', '0003_rename_bl1_mumbai_ml1_rename_bl2_mumbai_ml2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chennai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Ml1', models.IntegerField(default=0)),
                ('Ml2', models.IntegerField(default=0)),
                ('Ml3', models.IntegerField(default=0)),
                ('Ml4', models.IntegerField(default=0)),
            ],
        ),
    ]
