from django.contrib import admin
from .models import Execursion
# Register your models here.

@admin.register(Execursion)
class ExecursionAdmin(admin.ModelAdmin):
    list_display = ['name']