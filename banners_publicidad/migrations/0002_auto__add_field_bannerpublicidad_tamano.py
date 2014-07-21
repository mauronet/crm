# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BannerPublicidad.tamano'
        db.add_column(u'banners_publicidad_bannerpublicidad', 'tamano',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['banner_sizes.BannerSize']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BannerPublicidad.tamano'
        db.delete_column(u'banners_publicidad_bannerpublicidad', 'tamano_id')


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
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tamano': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['banner_sizes.BannerSize']"})
        }
    }

    complete_apps = ['banners_publicidad']