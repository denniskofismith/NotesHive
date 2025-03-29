from django.contrib import admin
from .models import Notes

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created', 'updated']

admin.site.register(Notes,NoteAdmin)
