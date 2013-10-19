from django.contrib import admin
from characters import models

admin.site.register(models.Character)
admin.site.register(models.Items)
admin.site.register(models.MissionResume)