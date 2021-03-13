from django.contrib import admin

from .models import Message, Project, Skill, Service

# Register your models here.
admin.site.register(Message)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.site_header = 'N I N E'
admin.site.site_title = 'N I N E'
