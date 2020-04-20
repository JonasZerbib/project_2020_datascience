from django.contrib import admin
from .models import Patient, Column, Cell
# Register your models here.
admin.site.register(Patient)
admin.site.register(Column)
admin.site.register(Cell)


