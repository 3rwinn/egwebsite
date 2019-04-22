from django.contrib import admin

from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'project_date')
    list_display_links = ('id', 'name')
    list_editable = ('is_published',)
    search_fields = ('name', 'description', 'technology_used', 'project_type')
    list_per_page = 25

admin.site.register(Project, ProjectAdmin) 