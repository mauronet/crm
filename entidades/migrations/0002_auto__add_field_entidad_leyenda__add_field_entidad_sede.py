# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entidad.leyenda'
        db.add_column(u'entidades_entidad', 'leyenda',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Entidad.sede'
        db.add_column(u'entidades_entidad', 'sede',
                      self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Entidad.leyenda'
        db.delete_column(u'entidades_entidad', 'leyenda')

        # Deleting field 'Entidad.sede'
        db.delete_column(u'entidades_entidad', 'sede')


    models = {
        u'entidades.entidad': {
            'Meta': {'object_name': 'Entidad'},
            'activo': ('django.db.models.fields.BooleanField', [], {}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'leyenda': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sede': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'telefonos': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tipos_entidades.TipoEntidad']"})
        },
        u'tipos_entidades.tipoentidad': {
            'Meta': {'object_name': 'TipoEntidad'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['entidades']