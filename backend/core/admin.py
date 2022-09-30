from django.contrib import admin
from .models import *
admin.site.register(Feature)
admin.site.register(Assessment)
admin.site.register(Log)
admin.site.register(Comment)
admin.site.register(Artwork)

# Path: core/admin.py