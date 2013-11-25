# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Resposta.skey'
        db.add_column(u'questao_resposta', 'skey',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Resposta.skey'
        db.delete_column(u'questao_resposta', 'skey')


    models = {
        u'categoria.category': {
            'Meta': {'object_name': 'Category'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'category__self'", 'null': 'True', 'blank': 'True', 'to': u"orm['categoria.Category']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Ativo'", 'max_length': '10'})
        },
        u'questao.questao': {
            'Meta': {'object_name': 'Questao'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'category__categoria'", 'null': 'True', 'blank': 'True', 'to': u"orm['categoria.Category']"}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'category__self'", 'null': 'True', 'blank': 'True', 'to': u"orm['questao.Questao']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Ativo'", 'max_length': '10'})
        },
        u'questao.resposta': {
            'Meta': {'object_name': 'Resposta'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questao': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questao__resposta'", 'to': u"orm['questao.Questao']"}),
            'resposta': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'skey': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['questao']