# Generated by Django 2.2 on 2019-04-11 08:04

from django.db import migrations, models
import django.db.models.deletion
import shy.utils.unique


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', verbose_name='text')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Mount name')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.CharField(default=shy.utils.unique.unique_id, max_length=50, unique=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='posts.Post')),
            ],
        ),
    ]
