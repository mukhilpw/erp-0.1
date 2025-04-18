# Generated by Django 4.2.20 on 2025-03-28 05:14

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
            name='HistoryPC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bios_serial', models.CharField(max_length=100)),
                ('old_computer_name', models.CharField(max_length=100)),
                ('new_computer_name', models.CharField(max_length=100)),
                ('changed_at', models.DateTimeField()),
                ('username', models.CharField(max_length=100)),
                ('recorded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listdata', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('icon', models.CharField(blank=True, default='fa-circle', help_text='Font Awesome icon class (e.g., fa-tachometer-alt)', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShareFolderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcname', models.CharField(max_length=100)),
                ('foldername', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SystemInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('username', models.CharField(default='', max_length=100)),
                ('sitename', models.CharField(default='', max_length=100)),
                ('computer_name', models.CharField(default='', max_length=100)),
                ('anydesk_id', models.CharField(default='', max_length=50)),
                ('ipv4', models.CharField(default='', max_length=45)),
                ('ipv6', models.CharField(default='', max_length=45)),
                ('bios_serial', models.CharField(default='', max_length=100)),
                ('model', models.CharField(default='', max_length=100)),
                ('processor', models.CharField(default='', max_length=200)),
                ('ram_gb', models.FloatField(default=0.0)),
                ('graphics_card', models.CharField(default='', max_length=200)),
                ('storage', models.CharField(default='', max_length=200)),
                ('os_name', models.CharField(default='', max_length=100)),
                ('os_version', models.CharField(default='', max_length=50)),
                ('os_manufacturer', models.CharField(default='', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('additional_hardware', models.JSONField(blank=True, default=list)),
                ('remarks', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monitor_model', models.CharField(default='', max_length=100)),
                ('serial_number', models.CharField(default='', max_length=100)),
                ('system_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monitors', to='it.systeminfo')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('url', models.CharField(blank=True, default='', max_length=200)),
                ('icon', models.CharField(blank=True, default='fa-circle', help_text='Font Awesome icon class (e.g., fa-tachometer-alt)', max_length=50)),
                ('allowed_users', models.ManyToManyField(blank=True, help_text='Users who can see this menu', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submenus', to='it.menu')),
            ],
        ),
        migrations.CreateModel(
            name='DisplaySetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolution', models.CharField(default='', max_length=20)),
                ('refresh_rate', models.CharField(default='', max_length=10)),
                ('adapter_name', models.CharField(default='', max_length=100)),
                ('system_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='display_settings', to='it.systeminfo')),
            ],
        ),
    ]
