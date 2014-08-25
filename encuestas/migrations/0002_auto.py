# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field respuestas on 'Encuesta'
        m2m_table_name = db.shorten_name(u'encuestas_encuesta_respuestas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('encuesta', models.ForeignKey(orm[u'encuestas.encuesta'], null=False)),
            ('respuestaencuesta', models.ForeignKey(orm[u'respuestas_encuestas.respuestaencuesta'], null=False))
        ))
        db.create_unique(m2m_table_name, ['encuesta_id', 'respuestaencuesta_id'])


    def backwards(self, orm):
        # Removing M2M table for field respuestas on 'Encuesta'
        db.delete_table(db.shorten_name(u'encuestas_encuesta_respuestas'))


    models = {
        u'encuestas.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'activa': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'respuestas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['respuestas_encuestas.RespuestaEncuesta']", 'symmetrical': 'False'})
        },
        u'respuestas_encuestas.respuestaencuesta': {
            'Meta': {'object_name': 'RespuestaEncuesta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'votos': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['encuestas']