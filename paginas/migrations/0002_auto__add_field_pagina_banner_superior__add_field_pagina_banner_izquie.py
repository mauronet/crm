# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pagina.banner_superior'
        db.add_column(u'paginas_pagina', 'banner_superior',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='bannersuperior_pagina', blank=True, to=orm['banners_publicidad.BannerPublicidad']),
                      keep_default=False)

        # Adding field 'Pagina.banner_izquierdo'
        db.add_column(u'paginas_pagina', 'banner_izquierdo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='bannerizquierdo_pagina', blank=True, to=orm['banners_publicidad.BannerPublicidad']),
                      keep_default=False)

        # Adding field 'Pagina.banner_derecho'
        db.add_column(u'paginas_pagina', 'banner_derecho',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='bannerderecho_pagina', blank=True, to=orm['banners_publicidad.BannerPublicidad']),
                      keep_default=False)

        # Adding field 'Pagina.banner_inferior'
        db.add_column(u'paginas_pagina', 'banner_inferior',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='bannerinferior_pagina', blank=True, to=orm['banners_publicidad.BannerPublicidad']),
                      keep_default=False)

        # Removing M2M table for field banners on 'Pagina'
        db.delete_table(db.shorten_name(u'paginas_pagina_banners'))


    def backwards(self, orm):
        # Deleting field 'Pagina.banner_superior'
        db.delete_column(u'paginas_pagina', 'banner_superior_id')

        # Deleting field 'Pagina.banner_izquierdo'
        db.delete_column(u'paginas_pagina', 'banner_izquierdo_id')

        # Deleting field 'Pagina.banner_derecho'
        db.delete_column(u'paginas_pagina', 'banner_derecho_id')

        # Deleting field 'Pagina.banner_inferior'
        db.delete_column(u'paginas_pagina', 'banner_inferior_id')

        # Adding M2M table for field banners on 'Pagina'
        m2m_table_name = db.shorten_name(u'paginas_pagina_banners')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pagina', models.ForeignKey(orm[u'paginas.pagina'], null=False)),
            ('bannerpublicidad', models.ForeignKey(orm[u'banners_publicidad.bannerpublicidad'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pagina_id', 'bannerpublicidad_id'])


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
            'banner_derecho': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bannerderecho_pagina'", 'blank': 'True', 'to': u"orm['banners_publicidad.BannerPublicidad']"}),
            'banner_inferior': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bannerinferior_pagina'", 'blank': 'True', 'to': u"orm['banners_publicidad.BannerPublicidad']"}),
            'banner_izquierdo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bannerizquierdo_pagina'", 'blank': 'True', 'to': u"orm['banners_publicidad.BannerPublicidad']"}),
            'banner_superior': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bannersuperior_pagina'", 'blank': 'True', 'to': u"orm['banners_publicidad.BannerPublicidad']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['paginas']