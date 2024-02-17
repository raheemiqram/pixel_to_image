# Generated by Django 4.2 on 2024-02-15 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OriginalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('csv_file', models.FileField(upload_to='csv_files/')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('original_image', models.ImageField(blank=True, upload_to='original_images/')),
                ('original_width', models.IntegerField()),
                ('original_height', models.IntegerField()),
                ('error_message', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(app_label)s_%(class)s', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(app_label)s_%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReConstructImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resized_image', models.ImageField(upload_to='resized_images/')),
                ('resized_width', models.IntegerField()),
                ('resized_height', models.IntegerField()),
                ('original_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_builder.originalimage')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalOriginalImage',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('csv_file', models.TextField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('original_image', models.TextField(blank=True, max_length=100)),
                ('original_width', models.IntegerField()),
                ('original_height', models.IntegerField()),
                ('error_message', models.TextField(blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('created_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical original image',
                'verbose_name_plural': 'historical original images',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
