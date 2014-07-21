# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'InfoCanal.imagen_acerca_de_zoom'
        db.add_column(u'informacion_canal_infocanal', 'imagen_acerca_de_zoom',
                      self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'InfoCanal.imagen_equipo_de_trabajo'
        db.add_column(u'informacion_canal_infocanal', 'imagen_equipo_de_trabajo',
                      self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, blank=True),
                      keep_default=False)

        # Adding M2M table for field imagenes_adicionales_equipo_de_trabajo on 'InfoCanal'
        m2m_table_name = db.shorten_name(u'informacion_canal_infocanal_imagenes_adicionales_equipo_de_trabajo')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('infocanal', models.ForeignKey(orm[u'informacion_canal.infocanal'], null=False)),
            ('imagen', models.ForeignKey(orm[u'imagenes.imagen'], null=False))
        ))
        db.create_unique(m2m_table_name, ['infocanal_id', 'imagen_id'])


    def backwards(self, orm):
        # Deleting field 'InfoCanal.imagen_acerca_de_zoom'
        db.delete_column(u'informacion_canal_infocanal', 'imagen_acerca_de_zoom')

        # Deleting field 'InfoCanal.imagen_equipo_de_trabajo'
        db.delete_column(u'informacion_canal_infocanal', 'imagen_equipo_de_trabajo')

        # Removing M2M table for field imagenes_adicionales_equipo_de_trabajo on 'InfoCanal'
        db.delete_table(db.shorten_name(u'informacion_canal_infocanal_imagenes_adicionales_equipo_de_trabajo'))


    models = {
        u'documentos.documento': {
            'Meta': {'object_name': 'Documento'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'imagenes.imagen': {
            'Meta': {'object_name': 'Imagen'},
            'archivo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'creditos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'informacion_canal.infocanal': {
            'Meta': {'object_name': 'InfoCanal'},
            'acerca_de_zoom': ('django.db.models.fields.TextField', [], {}),
            'comite_de_programacion': ('django.db.models.fields.TextField', [], {}),
            'comites_tecnicos_regionales': ('django.db.models.fields.TextField', [], {}),
            'documentos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['documentos.Documento']", 'symmetrical': 'False', 'blank': 'True'}),
            'equipo_de_trabajo': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen_acerca_de_zoom': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagen_equipo_de_trabajo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagenes_adicionales_equipo_de_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['imagenes.Imagen']", 'symmetrical': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['informacion_canal']