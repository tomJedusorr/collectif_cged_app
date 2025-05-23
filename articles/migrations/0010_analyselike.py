# Generated by Django 5.2.1 on 2025-05-13 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_articlelike'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyseLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('analyse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_by_ip', to='articles.researchpaper')),
            ],
            options={
                'unique_together': {('analyse', 'ip_address')},
            },
        ),
    ]
