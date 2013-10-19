from tastypie.resources import ModelResource
from characters.models import Character, MissionResume, Items

# Create your models here.

class CharactersResource(ModelResource):
    class Meta:
        queryset = Character.objects.all()
        resource_name = 'characters'

class MissionResumeResource(ModelResource):
    class Meta:
        queryset = MissionResume.objects.all()
        resource_name = 'mission-resume'