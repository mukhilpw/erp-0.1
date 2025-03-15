from django.contrib import admin
# from .models import HeadOfficeModule,ProjectSpecificModule
from .models import OfficeModule,Department,Module


@admin.register(OfficeModule)
class OfficeModuleAdmin(admin.ModelAdmin):
    list_display = ('id','office')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','dp')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id','name','office','department')