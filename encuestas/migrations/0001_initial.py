# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Encuesta'
        db.create_table(u'encuestas_encuesta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('activa', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'encuestas', ['Encuesta'])


    def backwards(self, orm):
        # Deleting model 'Encuesta'
        db.delete_table(u'encuestas_encuesta')


    models = {
        u'encuestas.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'activa': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['encuestas']