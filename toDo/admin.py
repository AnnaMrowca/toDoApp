from django.contrib import admin
from .models import Task

class DisplayDate(admin.ModelAdmin):
    readonly_fields = ('creation_date',)

admin.site.register(Task, DisplayDate)


# Register your models here.
