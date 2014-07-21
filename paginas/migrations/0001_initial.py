# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pagina'
        db.create_table(u'paginas_pagina', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'paginas', ['Pagina'])

        # Adding M2M table for field banners on 'Pagina'
        m2m_table_name = db.shorten_name(u'paginas_pagina_banners')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pagina', models.ForeignKey(orm[u'paginas.pagina'], null=False)),
            ('bannerpublicidad', models.ForeignKey(orm[u'banners_publicidad.bannerpublicidad'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pagina_id', 'bannerpublicidad_id'])


    def backwards(self, orm):
        # Deleting model 'Pagina'
        db.delete_table(u'paginas_pagina')

        # Removing M2M table for field banners on 'Pagina'
        db.delete_table(db.shorten_name(u'paginas_pagina_banners'))


    models = {
        u'banners_publicidad.bannerpublicidad': {
            'Meta': {'object_name': 'BannerPublicidad'},
            'codigo_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'direccion_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'paginas.pagina': {
            'Meta': {'object_name': 'Pagina'},
            'banners': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['banners_publicidad.BannerPublicidad']", 'symmetrical': 'False', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['paginas']