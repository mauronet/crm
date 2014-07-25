# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pagina.banner_robapagina'
        db.add_column(u'paginas_pagina', 'banner_robapagina',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='banner5', null=True, to=orm['banners_publicidad.BannerPublicidad']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Pagina.banner_robapagina'
        db.delete_column(u'paginas_pagina', 'banner_robapagina_id')


    models = {
        u'banner_sizes.bannersize': {
            'Meta': {'object_name': 'BannerSize'},
            'alto': ('django.db.models.fields.SmallIntegerField', [], {}),
            'ancho': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'banners_publicidad.bannerpublicidad': {
            'Meta': {'object_name': 'BannerPublicidad'},
            'codigo_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'direccion_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tamano': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['banner_sizes.BannerSize']"})
        },
        u'paginas.pagina': {
            'Meta': {'object_name': 'Pagina'},
            'banner_derecho': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'banner3'", 'null': 'True', 'to': u"orm['banners_publicidad.BannerPublicidad']"}),
            'banner_inferior': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'banner4'", 'null': 'True', 'to': u"orm['banners_publicidad.BannerPublicidad']"}),
            'banner_izquierdo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'banner2'", 'null': 'True', 'to': u"orm['banners_publicidad.BannerPublicidad']"}),
            'banner_robapagina': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'banner5'", 'null': 'True', 'to': u"orm['banners_publicidad.BannerPublicidad']"}),
            'banner_superior': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'banner1'", 'null': 'True', 'to': u"orm['banners_publicidad.BannerPublicidad']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['paginas']