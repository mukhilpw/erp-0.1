from django.db import models


class OfficeModule(models.Model):
    office = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.office

class Department(models.Model):
    dp = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.dp

class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)
    office = models.ForeignKey(OfficeModule, on_delete=models.CASCADE, related_name='modules')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return self.name

    


