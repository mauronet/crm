# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Programa.detalles'
        db.delete_column(u'programas_programa', 'detalles')

        # Adding M2M table for field imagenes on 'Programa'
        m2m_table_name = db.shorten_name(u'programas_programa_imagenes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('programa', models.ForeignKey(orm[u'programas.programa'], null=False)),
            ('imagen', models.ForeignKey(orm[u'imagenes.imagen'], null=False))
        ))
        db.create_unique(m2m_table_name, ['programa_id', 'imagen_id'])


    def backwards(self, orm):
        # Adding field 'Programa.detalles'
        db.add_column(u'programas_programa', 'detalles',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Removing M2M table for field imagenes on 'Programa'
        db.delete_table(db.shorten_name(u'programas_programa_imagenes'))


    models = {
        u'capitulos.capitulo': {
            'Meta': {'object_name': 'Capitulo'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'duracion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'produccion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.Video']"})
        },
        u'categorias.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'entidades.entidad': {
            'Meta': {'object_name': 'Entidad'},
            'activo': ('django.db.models.fields.BooleanField', [], {}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'telefonos': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tipos_entidades.TipoEntidad']"})
        },
        u'franjas.franja': {
            'Meta': {'object_name': 'Franja'},
            'codigo_html_video': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
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
        u'programas.programa': {
            'Meta': {'object_name': 'Programa'},
            'banner': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'capitulos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['capitulos.Capitulo']", 'symmetrical': 'False', 'blank': 'True'}),
            'color_fondo': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'color_letra': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'color_linea': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'franja': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['franjas.Franja']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'imagenes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['imagenes.Imagen']", 'symmetrical': 'False', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'produccion': ('django.db.models.fields.BooleanField', [], {}),
            'sinopsis': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tipo_letra': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.Video']", 'null': 'True', 'blank': 'True'})
        },
        u'tags.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'tipos_entidades.tipoentidad': {
            'Meta': {'object_name': 'TipoEntidad'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'videos.video': {
            'Meta': {'object_name': 'Video'},
            'categorias': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['categorias.Categoria']", 'symmetrical': 'False', 'blank': 'True'}),
            'codigo_html': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'creditos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'entidades': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['entidades.Entidad']", 'symmetrical': 'False', 'blank': 'True'}),
            'franjas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['franjas.Franja']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tags.Tag']", 'symmetrical': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['programas']