# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Pagina.banner_izquierdo'
        db.delete_column(u'paginas_pagina', 'banner_izquierdo_id')

        # Deleting field 'Pagina.banner_superior'
        db.delete_column(u'paginas_pagina', 'banner_superior_id')

        # Deleting field 'Pagina.banner_derecho'
        db.delete_column(u'paginas_pagina', 'banner_derecho_id')

        # Deleting field 'Pagina.banner_inferior'
        db.delete_column(u'paginas_pagina', 'banner_inferior_id')


    def backwards(self, orm):
        # Adding field 'Pagina.banner_izquierdo'
        db.add_column(u'paginas_pagina', 'banner_izquierdo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='bannerizquierdo_pagina', to=orm['banners_publicidad.BannerPublicidad'], blank=True),
                      keep_default=False)

        # Adding field 'Pagina.banner_superior'
        db.add_column(u'paginas_pagina', 'banner_superior',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='bannersuperior_pagina', to=orm['banners_publicidad.BannerPublicidad'], blank=True),
                      keep_default=False)

        # Adding field 'Pagina.banner_derecho'
        db.add_column(u'paginas_pagina', 'banner_derecho',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='bannerderecho_pagina', to=orm['banners_publicidad.BannerPublicidad'], blank=True),
                      keep_default=False)

        # Adding field 'Pagina.banner_inferior'
        db.add_column(u'paginas_pagina', 'banner_inferior',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='bannerinferior_pagina', to=orm['banners_publicidad.BannerPublicidad'], blank=True),
                      keep_default=False)


    models = {
        u'paginas.pagina': {
            'Meta': {'object_name': 'Pagina'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['paginas']