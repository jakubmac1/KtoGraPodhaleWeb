# Generated by Django 4.0.4 on 2023-03-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ktogra', '0002_match_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=40)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Match',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
