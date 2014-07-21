# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Programacion.descripcion_programa'
        db.delete_column(u'programaciones_programacion', 'descripcion_programa')

        # Adding field 'Programacion.programa'
        db.add_column(u'programaciones_programacion', 'programa',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Programacion.descripcion_programa'
        db.add_column(u'programaciones_programacion', 'descripcion_programa',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)

        # Deleting field 'Programacion.programa'
        db.delete_column(u'programaciones_programacion', 'programa')


    models = {
        u'franjas.franja': {
            'Meta': {'object_name': 'Franja'},
            'codigo_html_video': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'horarios_programacion.horarioprogramacion': {
            'Meta': {'object_name': 'HorarioProgramacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manana': ('django.db.models.fields.TimeField', [], {}),
            'tarde_noche': ('django.db.models.fields.TimeField', [], {})
        },
        u'programaciones.programacion': {
            'Meta': {'object_name': 'Programacion'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'franja': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['franjas.Franja']"}),
            'horario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['horarios_programacion.HorarioProgramacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'programa': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['programaciones']