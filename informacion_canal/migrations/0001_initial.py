# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InfoCanal'
        db.create_table(u'informacion_canal_infocanal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('acerca_de_zoom', self.gf('django.db.models.fields.TextField')()),
            ('equipo_de_trabajo', self.gf('django.db.models.fields.TextField')()),
            ('comite_de_programacion', self.gf('django.db.models.fields.TextField')()),
            ('comites_tecnicos_regionales', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'informacion_canal', ['InfoCanal'])

        # Adding M2M table for field documentos on 'InfoCanal'
        m2m_table_name = db.shorten_name(u'informacion_canal_infocanal_documentos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('infocanal', models.ForeignKey(orm[u'informacion_canal.infocanal'], null=False)),
            ('documento', models.ForeignKey(orm[u'documentos.documento'], null=False))
        ))
        db.create_unique(m2m_table_name, ['infocanal_id', 'documento_id'])


    def backwards(self, orm):
        # Deleting model 'InfoCanal'
        db.delete_table(u'informacion_canal_infocanal')

        # Removing M2M table for field documentos on 'InfoCanal'
        db.delete_table(db.shorten_name(u'informacion_canal_infocanal_documentos'))


    models = {
        u'documentos.documento': {
            'Meta': {'object_name': 'Documento'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['informacion_canal']