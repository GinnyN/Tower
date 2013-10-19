from django.db import models
from django.contrib import admin

# Create your models here.

class Character(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	def  __unicode__(self):
		return u'%s' % self.name

class Items(models.Model):
	name = models.CharField(max_length=200)
	def  __unicode__(self):
		return u'%s' % self.name

class MissionResume(models.Model):
	TRUE = 'True'
	FALSE = 'False'
	success = models.CharField(max_length=5, choices =((TRUE, 'true'),(FALSE,'false')))
	description = models.TextField()
	date = models.DateField()
	items = models.ForeignKey(Items)
	def __unicode__(self):
		return u'%s' % self.date
