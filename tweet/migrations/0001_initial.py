# Generated by Django 3.0.3 on 2020-03-02 21:19

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetbody', models.CharField(max_length=140)),
                ('date_filed', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.CharField(default='', max_length=30)),
                ('twittuser', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
