# Generated by Django 3.0.3 on 2020-10-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name', max_length=100)),
                ('email', models.EmailField(help_text='Enter the mail', max_length=100)),
                ('message', models.TextField(max_length=100)),
            ],
        ),
    ]
