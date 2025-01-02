from django.contrib import admin
from .models import About, Project, Technology, Skill, SkillCategory, Experience

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'email')
    search_fields = ('title', 'description')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_live', 'created_at')
    list_filter = ('is_live', 'technologies')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    filter_horizontal = ('technologies',)

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date', 'current')
    list_filter = ('current',)
    search_fields = ('position', 'company', 'description') 