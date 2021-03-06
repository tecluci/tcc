# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Questao.description'
        db.delete_column(u'questao_questao', 'description')


        # Changing field 'Questao.name'
        db.alter_column(u'questao_questao', 'name', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Adding field 'Questao.description'
        db.add_column(u'questao_questao', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # Changing field 'Questao.name'
        db.alter_column(u'questao_questao', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'categoria.category': {
            'Meta': {'object_name': 'Category'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '90', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'category__self'", 'null': 'True', 'blank': 'True', 'to': u"orm['categoria.Category']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Ativo'", 'max_length': '10'})
        },
        u'questao.questao': {
            'Meta': {'object_name': 'Questao'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category__categoria'", 'to': u"orm['categoria.Category']"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'category__self'", 'null': 'True', 'blank': 'True', 'to': u"orm['questao.Questao']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Ativo'", 'max_length': '10'})
        }
    }

    complete_apps = ['questao']