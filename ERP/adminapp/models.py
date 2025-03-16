from django.db import models


#for User_Permission
from django.contrib.auth.models import User,Permission,Group





class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, unique=True)
    mobile  = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    website = models.URLField(unique=True)
    logo = models.ImageField(upload_to='media/logo/', blank=True, null=True)
    description = models.TextField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# office type (head office, branch office, project office)
class OfficeModule(models.Model):
    office = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.office

# department (sales,purchase,Procurement, accounts, hr, it, )
class Department(models.Model):
    dp = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.dp


# department (sales,purchase,Procurement, accounts, hr, it, )
class Projects(models.Model):
    project = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.project


# module (sales,purchase,Procurement, accounts, hr, it, ) head office, branch office, project office
class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)
    office = models.ForeignKey(OfficeModule, on_delete=models.CASCADE, related_name='modules')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='modules', null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return self.name

    

# user and permission user have acess for multiple company and module








class User_Permission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_permission')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='user_permission')
    office = models.ForeignKey(OfficeModule, on_delete=models.CASCADE, related_name='user_permission', null=True, blank=True)
    department = models.ManyToManyField(Department, related_name='user_permission')
    project = models.ManyToManyField(Projects, related_name='user_permission')
    company = models.ManyToManyField(Company, related_name='user_permission')
    module = models.ManyToManyField(Module, related_name='user_permission')
    # permission = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name='user_permission')


    def __str__(self):
        return self.user.username
