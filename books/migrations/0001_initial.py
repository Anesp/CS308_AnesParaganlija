# Generated by Django 3.1.7 on 2021-05-22 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=35)),
                ('authors', models.CharField(blank=True, default='', max_length=100)),
                ('publisher', models.CharField(blank=True, default='', max_length=35)),
                ('publication_date', models.DateField(blank=True, default='')),
                ('number_of_pages', models.IntegerField(blank=True, default='')),
                ('highlighted', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]