# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Answer'
        db.create_table(u'fitagift_backend_app_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 22, 0, 0))),
            ('modified_data', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 22, 0, 0), auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('goto_question', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='next_question', null=True, blank=True, to=orm['fitagift_backend_app.Question'])),
            ('belong_to_question', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='answers', null=True, blank=True, to=orm['fitagift_backend_app.Question'])),
            ('words', self.gf('django.db.models.fields.CharField')(default=None, max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal(u'fitagift_backend_app', ['Answer'])

        # Adding model 'Question'
        db.create_table(u'fitagift_backend_app_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 22, 0, 0))),
            ('modified_data', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 22, 0, 0), auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=300)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('grade', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'fitagift_backend_app', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Answer'
        db.delete_table(u'fitagift_backend_app_answer')

        # Deleting model 'Question'
        db.delete_table(u'fitagift_backend_app_question')


    models = {
        u'fitagift_backend_app.answer': {
            'Meta': {'object_name': 'Answer'},
            'belong_to_question': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'answers'", 'null': 'True', 'blank': 'True', 'to': u"orm['fitagift_backend_app.Question']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 22, 0, 0)'}),
            'goto_question': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'next_question'", 'null': 'True', 'blank': 'True', 'to': u"orm['fitagift_backend_app.Question']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_data': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 22, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'words': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        u'fitagift_backend_app.question': {
            'Meta': {'object_name': 'Question'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 22, 0, 0)'}),
            'grade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_data': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 22, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'})
        }
    }

    complete_apps = ['fitagift_backend_app']