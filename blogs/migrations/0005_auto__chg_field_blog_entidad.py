# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Blog.entidad'
        db.alter_column(u'blogs_blog', 'entidad_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entidades.Entidad'], null=True))

    def backwards(self, orm):

        # Changing field 'Blog.entidad'
        db.alter_column(u'blogs_blog', 'entidad_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['entidades.Entidad']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'blogs.blog': {
            'Meta': {'object_name': 'Blog'},
            'administrador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['userprofiles.UserProfile']", 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'entidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entidades.Entidad']", 'null': 'True', 'blank': 'True'}),
            'entradas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['entradas_blogs.EntradaBlog']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'categorias.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'comentarios.comentario': {
            'Meta': {'object_name': 'Comentario'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['estados_comentarios.EstadoComentario']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['userprofiles.UserProfile']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'documentos.documento': {
            'Meta': {'object_name': 'Documento'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'creado_por': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['entidades.Entidad']"}),
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
            'leyenda': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sede': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'telefonos': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tipos_entidades.TipoEntidad']"})
        },
        u'entradas_blogs.entradablog': {
            'Meta': {'object_name': 'EntradaBlog'},
            'categorias': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['categorias.Categoria']", 'symmetrical': 'False', 'blank': 'True'}),
            'comentarios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['comentarios.Comentario']", 'symmetrical': 'False', 'blank': 'True'}),
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'direccion_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'documentos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['documentos.Documento']", 'symmetrical': 'False', 'blank': 'True'}),
            'entidades': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['entidades.Entidad']", 'symmetrical': 'False', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'franjas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['franjas.Franja']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen_principal': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'imagenprincipal_entrada_blog'", 'to': u"orm['imagenes.Imagen']"}),
            'imagenes_adicionales': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['imagenes.Imagen']", 'symmetrical': 'False', 'blank': 'True'}),
            'lead': ('django.db.models.fields.TextField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tags.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['videos.Video']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'estados_comentarios.estadocomentario': {
            'Meta': {'object_name': 'EstadoComentario'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'creado_por': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['entidades.Entidad']"}),
            'creditos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
        u'tipos_usuario.tipousuario': {
            'Meta': {'object_name': 'TipoUsuario'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'tipos_videos.tipovideo': {
            'Meta': {'object_name': 'TipoVideo'},
            'extra': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'userprofiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'anotaciones_internas': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'biografia': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'entidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entidades.Entidad']", 'null': 'True', 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tipos_usuario.TipoUsuario']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'videos.video': {
            'Meta': {'object_name': 'Video'},
            'categorias': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['categorias.Categoria']", 'symmetrical': 'False', 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'creado_por': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'defaultEntidad'", 'to': u"orm['entidades.Entidad']"}),
            'creditos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'entidades': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['entidades.Entidad']", 'symmetrical': 'False', 'blank': 'True'}),
            'franjas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['franjas.Franja']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['tags.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['tipos_videos.TipoVideo']"}),
            'visto': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['blogs']