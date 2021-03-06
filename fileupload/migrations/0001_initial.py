# Generated by Django 2.0.4 on 2018-05-24 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import fileupload.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, upload_to=fileupload.models.upload_to)),
                ('slug', models.SlugField(blank=True, max_length=20, null=True)),
                ('thumbnail', models.ImageField(blank=True, upload_to='thumbnails/%Y/%m/%d')),
                ('deleted', models.BooleanField(default=False)),
                ('show', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
