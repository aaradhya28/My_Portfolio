from django.contrib import admin
from .models import Certificate, Project
from .models import Project, ProjectImage

admin.site.register(Certificate)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 6  

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)