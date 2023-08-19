# Generated by Django 4.2.1 on 2023-06-25 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, max_length=150, null=True, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Изображение')),
                ('create_date', models.DateField(verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('count_of_view', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'новости',
                'ordering': ('title',),
            },
        ),
    ]
