# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Flatpage'
        db.create_table(u'fitagift_backend_app_flatpage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 31, 0, 0))),
            ('modified_data', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 31, 0, 0), auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250)),
            ('html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'fitagift_backend_app', ['Flatpage'])


    def backwards(self, orm):
        # Deleting model 'Flatpage'
        db.delete_table(u'fitagift_backend_app_flatpage')


    models = {
        u'fitagift_backend_app.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer_to_question_relevent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'relevent_question'", 'null': 'True', 'blank': 'True', 'to': u"orm['fitagift_backend_app.Question']"}),
            'belong_to_question': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'answers'", 'null': 'True', 'blank': 'True', 'to': u"orm['fitagift_backend_app.Question']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 31, 0, 0)'}),
            'goto_question': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'next_question'", 'null': 'True', 'blank': 'True', 'to': u"orm['fitagift_backend_app.Question']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_data': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 31, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'query_relevent_question': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'words': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        u'fitagift_backend_app.flatpage': {
            'Meta': {'object_name': 'Flatpage'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 31, 0, 0)'}),
            'html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_data': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 31, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        },
        u'fitagift_backend_app.question': {
            'Meta': {'object_name': 'Question'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 31, 0, 0)'}),
            'grade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_data': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 31, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'})
        }
    }

    complete_apps = ['fitagift_backend_app']