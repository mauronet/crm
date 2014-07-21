# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Pagina.banner_izquierdo'
        db.alter_column(u'paginas_pagina', 'banner_izquierdo_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['banners_publicidad.BannerPublicidad']))

        # Changing field 'Pagina.banner_superior'
        db.alter_column(u'paginas_pagina', 'banner_superior_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['banners_publicidad.BannerPublicidad']))

        # Changing field 'Pagina.banner_derecho'
        db.alter_column(u'paginas_pagina', 'banner_derecho_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['banners_publicidad.BannerPublicidad']))

        # Changing field 'Pagina.banner_inferior'
        db.alter_column(u'paginas_pagina', 'banner_inferior_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['banners_publicidad.BannerPublicidad']))

    def backwards(self, orm):

        # Changing field 'Pagina.banner_izquierdo'
        db.alter_column(u'paginas_pagina', 'banner_izquierdo_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['banners_publicidad.BannerPublicidad']))

        # Changing field 'Pagina.banner_superior'
        db.alter_column(u'paginas_pagina', 'banner_superior_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['banners_publicidad.BannerPublicidad']))

        # Changing field 'Pagina.banner_derecho'
        db.alter_column(u'paginas_pagina', 'banner_derecho_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['banners_publicidad.BannerPublicidad']))

        # Changing field 'Pagina.banner_inferior'
        db.alter_column(u'paginas_pagina', 'banner_inferior_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['banners_publicidad.BannerPublicidad']))

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
        },
        u'paginas.pagina': {
            'Meta': {'object_name': 'Pagina'},
            'banner_derecho': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'banner3'", 'null': 'True', 'to': u"orm['banners_publicidad.BannerPublicidad']"}),
            'banner_inferior': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'banner4'", 'null': 'True', 'to': u"orm['banners_publicidad.BannerPublicidad']"}),
            'banner_izquierdo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'banner2'", 'null': 'True', 'to': u"orm['banners_publicidad.BannerPublicidad']"}),
            'banner_superior': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'banner1'", 'null': 'True', 'to': u"orm['banners_publicidad.BannerPublicidad']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['paginas']