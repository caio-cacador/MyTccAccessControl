# Generated by Django 2.2.3 on 2019-09-05 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Courses/image', verbose_name='Imagem')),
            ],
        ),
    ]