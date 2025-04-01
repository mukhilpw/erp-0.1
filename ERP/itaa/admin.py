from django.contrib import admin

# Register your models here.
from .models import ShareFolderDetails,MainMenu,HistoryPC,Menu,Product # Import your model



# admin.py

from django.contrib.auth.models import User
from django.utils.html import format_html
from django import forms



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Define the list view fields
    list_display = ('name', 'category','price','stock')



# Custom form for MainMenu
class MainMenuForm(forms.ModelForm):
    class Meta:
        model = MainMenu
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial value for icon field in admin
        if not self.instance.pk:  # Only for new objects
            self.initial['icon'] = 'fa-solid fa-desktop'

@admin.register(MainMenu)
class MainMenuAdmin(admin.ModelAdmin):
    form = MainMenuForm
    list_display = ('id', 'listdata', 'icon_preview', 'icon')
    search_fields = ('listdata', 'icon')
    fields = ('listdata', 'icon')

    def icon_preview(self, obj):
        return format_html('<i class="fas {}"></i>', obj.icon)
    icon_preview.short_description = "Icon Preview"

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css',)
        }

# Custom form for Menu
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial value for icon field in admin
        if not self.instance.pk:  # Only for new objects
            self.initial['icon'] = 'fa-solid fa-desktop'

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    form = MenuForm
    list_display = ('title', 'icon_preview', 'icon', 'url', 'parent', 'display_allowed_users')
    list_filter = ('parent', 'allowed_users')
    search_fields = ('title', 'url', 'icon')
    fields = ('title', 'icon', 'url', 'parent', 'allowed_users')
    autocomplete_fields = ['parent', 'allowed_users']
    prepopulated_fields = {'url': ('title',)}

    def display_allowed_users(self, obj):
        return ", ".join([user.username for user in obj.allowed_users.all()])
    display_allowed_users.short_description = "Allowed Users"
    display_allowed_users.admin_order_field = 'allowed_users'

    def icon_preview(self, obj):
        return format_html('<i class="fas {}"></i>', obj.icon)
    icon_preview.short_description = "Icon Preview"

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css',)
        }
admin.site.unregister(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']

# @admin.register(Menu)
# class MenuAdmin(admin.ModelAdmin):
#     list_display = ('title', 'url', 'parent', 'display_allowed_users')
#     list_filter = ('parent', 'allowed_users')
#     search_fields = ('title', 'url')
#     fields = ('title', 'url', 'parent', 'allowed_users')
#     autocomplete_fields = ['parent', 'allowed_users']
#     prepopulated_fields = {'url': ('title',)}

#     # Renamed method and marked as readonly for admin display
#     def display_allowed_users(self, obj):
#         return ", ".join([user.username for user in obj.allowed_users.all()])
#     display_allowed_users.short_description = "Allowed Users"
#     display_allowed_users.admin_order_field = 'allowed_users'  # Allows sorting

# Re-register User admin for autocomplete
# admin.site.unregister(User)
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     search_fields = ['username']

@admin.register(HistoryPC)
class HistoryPCAdmin(admin.ModelAdmin):
    # Define the list view fields
    list_display = ('bios_serial', 'old_computer_name','new_computer_name','changed_at','username','recorded_at')

# Register the model
@admin.register(ShareFolderDetails)
class ShareFolderDetailsAdmin(admin.ModelAdmin):
    # Define the list view fields
    list_display = ('pcname', 'foldername', 'username', 'password')
    list_filter = ('pcname', 'foldername')  # Add filters
    search_fields = ('pcname', 'foldername', 'username')  # Add search functionality
    ordering = ('pcname',)  # Default sorting


# @admin.register(MainMenu)
# class MainMenuAdmin(admin.ModelAdmin):
#     # Define the list view fields
#     list_display = ('id', 'listdata')


from django.contrib import admin
from .models import SystemInfo, Monitor, DisplaySetting

# Customize SystemInfo admin
@admin.register(SystemInfo)
class SystemInfoAdmin(admin.ModelAdmin):
    list_display = (
        'timestamp',
        'sitename',
        'username',
        'computer_name',
        'anydesk_id',
        'ipv4',
        'ipv6',
        'bios_serial',
        'model',
        'processor',
        'ram_gb',
        'graphics_card',
        'storage',
        'os_name',
        'os_version',
        'os_manufacturer',
        'remarks',
        'created_at',
    )
    list_filter = ('username', 'computer_name', 'os_name', 'created_at')  # Optional filters
    search_fields = ('username', 'computer_name', 'anydesk_id', 'bios_serial')  # Optional search

    # Optional: Improve readability for related objects
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('monitors', 'display_settings')

# Customize Monitor admin
@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = (
        'system_info',
        'monitor_model',
        'serial_number',
    )
    list_filter = ('system_info__username',)  # Filter by related SystemInfo username
    search_fields = ('monitor_model', 'serial_number')

# Customize DisplaySetting admin
@admin.register(DisplaySetting)
class DisplaySettingAdmin(admin.ModelAdmin):
    list_display = (
        'system_info',
        'resolution',
        'refresh_rate',
        'adapter_name',
    )
    list_filter = ('system_info__username',)  # Filter by related SystemInfo username
    search_fields = ('resolution', 'adapter_name')