# Generated by Django 3.1.5 on 2021-01-14 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_smartwatches'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headphones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('type_of_connection', models.CharField(max_length=255, verbose_name='Тип подключения')),
                ('active_noise_cancelling', models.CharField(max_length=255, verbose_name='Система активного шумоподваления')),
                ('time_without_charge', models.CharField(max_length=255, verbose_name='Время работы без подзярядки')),
                ('wireless', models.CharField(max_length=255, verbose_name='Проводные/Беспроводные')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
