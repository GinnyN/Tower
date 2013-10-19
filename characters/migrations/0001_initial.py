# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Character'
        db.create_table(u'characters_character', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'characters', ['Character'])

        # Adding model 'Items'
        db.create_table(u'characters_items', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'characters', ['Items'])

        # Adding model 'MissionResume'
        db.create_table(u'characters_missionresume', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('success', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('items', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['characters.Items'])),
        ))
        db.send_create_signal(u'characters', ['MissionResume'])


    def backwards(self, orm):
        # Deleting model 'Character'
        db.delete_table(u'characters_character')

        # Deleting model 'Items'
        db.delete_table(u'characters_items')

        # Deleting model 'MissionResume'
        db.delete_table(u'characters_missionresume')


    models = {
        u'characters.character': {
            'Meta': {'object_name': 'Character'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'characters.items': {
            'Meta': {'object_name': 'Items'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'characters.missionresume': {
            'Meta': {'object_name': 'MissionResume'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['characters.Items']"}),
            'success': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['characters']