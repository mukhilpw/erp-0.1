from django.db import models
import json
from django.contrib.auth.models import User
from django.urls import reverse, NoReverseMatch




class Menu(models.Model):
    title = models.CharField(max_length=100,default="")
    url = models.CharField(max_length=200, blank=True,default="")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='submenus')
    icon = models.CharField(max_length=50, blank=True, default="fa-circle", help_text="Font Awesome icon class (e.g., fa-tachometer-alt)")
    # Add allowed_users field to specify which users can see this menu
    allowed_users = models.ManyToManyField(User, blank=True, help_text="Users who can see this menu")

    def get_absolute_url(self):
            if self.url.startswith('http'):
                return self.url
            try:
                return reverse(self.url)
            except NoReverseMatch:
                return self.url or "#"

    def __str__(self):
        return self.title


# Create your models here.
class ShareFolderDetails(models.Model):
    pcname = models.CharField(max_length=100)
    foldername = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.pcname


class MainMenu(models.Model):
    listdata = models.CharField(max_length=255, default=None, null=True, blank=True)  # Default is None, and field is nullable
    icon = models.CharField(max_length=50, blank=True, default="fa-circle", help_text="Font Awesome icon class (e.g., fa-tachometer-alt)")


from django.db import models

class SystemInfo(models.Model):
    timestamp = models.DateTimeField()
    username = models.CharField(max_length=100, default="")
    sitename = models.CharField(max_length=100, default="")
    computer_name = models.CharField(max_length=100, default="")
    anydesk_id = models.CharField(max_length=50, default="")
    ipv4 = models.CharField(max_length=45, default="")  # Supports IPv4 length
    ipv6 = models.CharField(max_length=45, default="")  # Supports IPv6 length
    bios_serial = models.CharField(max_length=100, default="")
    model = models.CharField(max_length=100, default="")
    processor = models.CharField(max_length=200, default="")
    ram_gb = models.FloatField(default=0.0)  # Default to 0.0 for numeric field
    graphics_card = models.CharField(max_length=200, default="")
    storage = models.CharField(max_length=200, default="")
    os_name = models.CharField(max_length=100, default="")
    os_version = models.CharField(max_length=50, default="")
    os_manufacturer = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of record creation
    additional_hardware = models.JSONField(default=list, blank=True)
    remarks = models.TextField(default="", blank=True)  # New field for remarks


    def __str__(self):
        return f"{self.username} - {self.computer_name} - {self.timestamp}"

    def save(self, *args, **kwargs):
            # Check if this is an update or new record
            if self.pk is not None:
                try:
                    old_record = SystemInfo.objects.get(pk=self.pk)
                    if old_record.computer_name != self.computer_name:
                        # Save to history if computer name changed
                        HistoryPC.objects.create(
                            bios_serial=self.bios_serial,
                            old_computer_name=old_record.computer_name,
                            new_computer_name=self.computer_name,
                            changed_at=self.timestamp,
                            username=self.username
                        )
                except SystemInfo.DoesNotExist:
                    pass
            elif SystemInfo.objects.filter(bios_serial=self.bios_serial).exists():
                # If this is a new record but bios_serial exists, check last record
                last_record = SystemInfo.objects.filter(bios_serial=self.bios_serial).latest('timestamp')
                if last_record.computer_name != self.computer_name:
                    HistoryPC.objects.create(
                        bios_serial=self.bios_serial,
                        old_computer_name=last_record.computer_name,
                        new_computer_name=self.computer_name,
                        changed_at=self.timestamp,
                        username=self.username
                    )

            super().save(*args, **kwargs)

class Monitor(models.Model):
    system_info = models.ForeignKey(SystemInfo, on_delete=models.CASCADE, related_name='monitors')
    monitor_model = models.CharField(max_length=100, default="")
    serial_number = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.monitor_model} ({self.serial_number})"

class DisplaySetting(models.Model):
    system_info = models.ForeignKey(SystemInfo, on_delete=models.CASCADE, related_name='display_settings')
    resolution = models.CharField(max_length=20, default="")  # e.g., "1920x1080"
    refresh_rate = models.CharField(max_length=10, default="")  # e.g., "60 Hz"
    adapter_name = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.resolution} @ {self.refresh_rate}"

class HistoryPC(models.Model):
    bios_serial = models.CharField(max_length=100)
    old_computer_name = models.CharField(max_length=100)
    new_computer_name = models.CharField(max_length=100)
    changed_at = models.DateTimeField()
    username = models.CharField(max_length=100)
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bios_serial}: {self.old_computer_name} -> {self.new_computer_name}"



from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

