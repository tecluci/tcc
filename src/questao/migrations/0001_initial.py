# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Questao'
        db.create_table(u'questao_questao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=90, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='Ativo', max_length=10)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='category__self', null=True, blank=True, to=orm['questao.Questao'])),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(related_name='category__categoria', to=orm['categoria.Category'])),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'questao', ['Questao'])


    def backwards(self, orm):
        # Deleting model 'Questao'
        db.delete_table(u'questao_questao')


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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '90', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'category__self'", 'null': 'True', 'blank': 'True', 'to': u"orm['questao.Questao']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Ativo'", 'max_length': '10'})
        }
    }

    complete_apps = ['questao']