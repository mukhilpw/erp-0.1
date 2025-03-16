from django.contrib import admin
from .models import OfficeModule, Department, Module, Company, Projects, User_Permission




@admin.register(User_Permission)
class User_PermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group', 'office', 'get_department', 'get_project', 'get_company', 'get_module')
    list_filter = ('company', 'module')
    search_fields = ('user__username',)
    def get_company(self, obj):
        return ", ".join([company.name for company in obj.company.all()]) or '-'
    get_company.short_description = 'Company'

    def get_module(self, obj):
        return ", ".join([module.name for module in obj.module.all()]) or '-'
    get_module.short_description = 'Module'

    def get_department(self, obj):
        return ", ".join([department.name for department in obj.department.all()]) or '-'
    get_department.short_description = 'Department'

    def get_project(self, obj):
        return ", ".join([project.name for project in obj.project.all()]) or '-'
    get_project.short_description = 'Project'

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'mobile', 'email', 'website', 'description', 'is_active')
    list_filter = ('is_active', 'is_verified', 'is_blocked')
    search_fields = ('name', 'email', 'location')
    list_editable = ('is_active',)


@admin.register(OfficeModule)
class OfficeModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'office')
    search_fields = ('office',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'dp')
    search_fields = ('dp',)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'office', 'department', 'project', 'name')
    list_filter = ('office', 'department', 'project')
    search_fields = ('name',)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'project')
    search_fields = ('project',)