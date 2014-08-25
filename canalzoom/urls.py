from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from .feeds import FeedNoticias, FeedEventos, FeedOportunidades, FeedEntradasBlogs
admin.autodiscover()

feeds = {
    'noticias': FeedNoticias,
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'canalzoom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index_view', name='index_view'),

    url(r'^canal/acerca de zoom/', 'home.views.acerca_de_zoom_view', name='vista_acercadezoom'),
    url(r'^canal/equipo de trabajo/', 'home.views.equipo_zoom_view', name='vista_equipozoom'),
    url(r'^canal/comite programacion/', 'home.views.comite_programacion_view', name='vista_comiteprogramacion'),
    url(r'^canal/comites tecnicos regionales/', 'home.views.comites_tecnicos_regionales_view', name='vista_comitestecnicosregionales'),
    url(r'^canal/documentos/', 'home.views.documentos_view', name='vista_documentos'),
    url(r'^encuesta/responder/', 'home.views.responder_encuesta_view', name='vista_responder_encuesta'),

    url(r'^IES Afiliadas/page/(?P<id_pagina>.*)/$', 'entidades.views.entidades_view', name='vista_entidades'),
    url(r'^IES Afiliadas/entidades/(?P<id_entidad>.*)/$', 'entidades.views.ies_view', name='vista_ies'),

    url(r'^senal en vivo/', 'home.views.senal_en_vivo_view', name='vista_senalenvivo'),


    url(r'^noticias/categoria/(?P<id_categoria>.*)/$', 'noticias.views.noticias_view', name='vista_pagina_noticias'),
    url(r'^noticias/page/(?P<id_pagina>.*)/$', 'noticias.views.noticias_view', name='vista_pagina_noticias'),
    url(r'^noticias/(?P<id_noticia>.*)/$', 'noticias.views.noticia_view', name='vista_noticia'),
    url(r'^noticias/$', 'noticias.views.noticias_view', name='vista_default_pagina_noticias'),

    url(r'^franjas/(?P<nombre>[\w\ ]+)/', 'franjas.views.franja_view', name='vista_franja'),

    url(r'^imagenes/(?P<id_imagen>.*)/$', 'imagenes.views.imagen_view', name='vista_imagen'),

    url(r'^entidades/(?P<id_entidad>.*)/$', 'entidades.views.entidad_view', name='vista_entidad'),

    url(r'^videos/page/(?P<id_pagina>.*)/$', 'videos.views.videos_view', name='vista_videos'),
    url(r'^videos/(?P<id_video>.*)/$', 'videos.views.video_view', name='vista_video'),

    url(r'^producciones/(?P<id_programa>.*)/imagenes/(?P<id_imagen>.*)/$', 'programas.views.imagen_view', name='vista_imagenprograma'),
    url(r'^producciones/(?P<id_programa>.*)/capitulos/(?P<id_capitulo>.*)/$', 'programas.views.capitulo_view', name='vista_capitulo'),
    url(r'^producciones/(?P<id_programa>.*)/$', 'programas.views.programa_view', name='vista_programa'),

    url(r'^eventos/page/(?P<id_pagina>.*)/$', 'eventos.views.eventos_view', name='vista_pagina_eventos'),
    url(r'^eventos/(?P<id_evento>.*)/$', 'eventos.views.evento_view', name='vista_evento'),
    url(r'^eventos/$', 'eventos.views.eventos_view', name='vista_default_evento'),

    url(r'^oportunidades/page/(?P<id_pagina>.*)/$', 'oportunidades.views.oportunidades_view', name='vista_pagina_oportunidades'),
    url(r'^oportunidades/(?P<id_oportunidad>.*)/$', 'oportunidades.views.oportunidad_view', name='vista_oportunidad'),
    url(r'^oportunidades/$', 'oportunidades.views.oportunidades_view', name='vista_pagina_oportunidades'),

    url(r'^programacion/', 'programaciones.views.programacion_view', name='vista_programacion'),

    url(r'^blogs/entradas/(?P<id_entrada>.*)/$', 'blogs.views.entrada_blog_view', name='vista_entradablog'),
    url(r'^blogs/page/(?P<id_pagina>.*)/$', 'blogs.views.blogs_view', name='vista_blogs'),
    url(r'^blogs/(?P<id_blog>.*)/$', 'blogs.views.blog_view', name='vista_blog'),
    url(r'^blogs/$', 'blogs.views.blogs_view', name='vista_blogs'),

    url(r'^login/$', 'home.views.login_view', name='vista_login'),
    url(r'^logout/$', 'home.views.logout_view', name='vista_logout'),
    url(r'^registro/$', 'home.views.registro_view', name='vista_registro'),
    url(r'^mi perfil/$','home.views.perfil_view',name='vista_perfil'),
    url(r'^perfiles/(?P<id_perfil>.*)/$','home.views.verperfil_view',name='vista_verperfil'),
    url(r'^confirm/(?P<activation_key>\w+)/', 'home.views.register_confirm_view', name='vista_confirmarregistro'),
    url(r'^cambiar_contrasena/$', 'home.views.ask_email_view', name='vista_solicitaremail'),
    url(r'^cambiar_contrasena/(?P<activation_key>\w+)/', 'home.views.change_password_view', name='vista_cambiarcontrasena'),
    
    url(r'^comentario noticia/$', 'noticias.views.nuevo_comentario_noticia_view', name='vista_nuevo_comentario_noticia'),
    url(r'^comentario oportunidad/$', 'oportunidades.views.nuevo_comentario_oportunidad_view', name='vista_nuevo_comentario_oportunidad'),
    url(r'^comentario evento/$', 'eventos.views.nuevo_comentario_evento_view', name='vista_nuevo_comentario_evento'),
    url(r'^comentario entrada blog/$', 'blogs.views.nuevo_comentario_entrada_blog_view', name='vista_nuevo_comentario_entrada_blog'),
    
    url(r'^adminEntidad/$', 'admin_entidad.views.adminentidad_index_view', name='vista_adminentidadindex'),

    url(r'^adminEntidad/imagenes/page/(?P<page>.*)/$', 'admin_entidad.views.adminentidad_imagenes_view', name='vista_adminentidadimagenes'),
    url(r'^adminEntidad/add/imagen/$', 'admin_entidad.views.add_imagen_view', name='vista_adminentidadaddimagen'),
    url(r'^adminEntidad/edit/imagen/(?P<id_img>.*)/$', 'admin_entidad.views.edit_imagen_view', name='vista_adminentidadeditimagen'),
    
    url(r'^adminEntidad/videos/page/(?P<page>.*)/$', 'admin_entidad.views.adminentidad_videos_view', name='vista_adminentidadvideos'),
    url(r'^adminEntidad/add/video/$', 'admin_entidad.views.add_video_view', name='vista_adminentidadaddvideo'),
    url(r'^adminEntidad/edit/video/(?P<id_img>.*)/$', 'admin_entidad.views.edit_video_view', name='vista_adminentidadeditvideo'),
    
    url(r'^adminEntidad/documentos/page/(?P<page>.*)/$', 'admin_entidad.views.adminentidad_documentos_view', name='vista_adminentidaddocumentos'),
    url(r'^adminEntidad/add/documento/$', 'admin_entidad.views.add_documento_view', name='vista_adminentidadadddocumento'),
    url(r'^adminEntidad/edit/documento/(?P<id_img>.*)/$', 'admin_entidad.views.edit_documento_view', name='vista_adminentidadeditdocumento'),

    url(r'^adminEntidad/programas/$', 'admin_entidad.views.adminentidad_programas_view', name='vista_adminentidadprogramas'),
    url(r'^adminEntidad/edit/programa/(?P<id_img>.*)/$', 'admin_entidad.views.edit_programa_view', name='vista_adminentidadeditprograma'),
    url(r'^adminEntidad/programas/(?P<id_prg>.*)/capitulos/$', 'admin_entidad.views.adminentidad_capitulos_view', name='vista_adminentidadcapitulos'),
    url(r'^adminEntidad/add/capitulo/programa/(?P<id_prg>.*)/$', 'admin_entidad.views.add_capitulo_view', name='vista_adminentidadaddcapitulo'),
    url(r'^adminEntidad/edit/capitulo/(?P<id_cap>.*)/programa/(?P<id_prg>.*)/$', 'admin_entidad.views.edit_capitulo_view', name='vista_adminentidadeditcapitulo'),

    url(r'^adminEntidad/blogs/(?P<id_blog>.*)/entradas/page/(?P<page>.*)/$', 'admin_entidad.views.adminentidad_entradas_blog_view', name='vista_adminentidadentradasblog'),
    url(r'^adminEntidad/blogs/$', 'admin_entidad.views.adminentidad_blogs_view', name='vista_adminentidadblogs'),
    url(r'^adminEntidad/add/entrada/blog/(?P<id_blog>.*)/$', 'admin_entidad.views.add_entrada_view', name='vista_adminentidadaddentrada'),
    url(r'^adminEntidad/edit/entrada/(?P<id_entrada>.*)/blog/(?P<id_blog>.*)/$', 'admin_entidad.views.edit_entrada_view', name='vista_adminentidadeditentrada'),

    url(r'^adminEntidad/comentarios/$', 'admin_entidad.views.adminentidad_moderar_comentarios_blog_view', name='vista_adminentidadmoderarcomentariosblog'),

    url(r'^feeds/$', 'home.views.lista_fees_view'),
    url(r'^feeds/noticias/$', FeedNoticias()),
    url(r'^feeds/eventos/$', FeedEventos()),
    url(r'^feeds/oportunidades/$', FeedOportunidades()),
    url(r'^feeds/blogs/$', FeedEntradasBlogs()),

    url('', include('social.apps.django_app.urls', namespace='social')),
)

urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
)

"""
    url(r'^blogs/(?P<id_blog>.*)/page/(?P<pagina>.*)/$', 'blogs.views.blog_view', name='vista_blog'),

"""