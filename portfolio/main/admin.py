from django.contrib import admin
from.models import Tag, Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    inlines = []
    search_fields = ("title", "description")
    list_filter = ("tags", )