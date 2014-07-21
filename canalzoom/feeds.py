
# -*- encoding: utf-8 -*-
from django.contrib.syndication.views import Feed
from datetime import datetime, time
from noticias.models import Noticia
from eventos.models import Evento
from oportunidades.models import Oportunidad
from entradas_blogs.models import EntradaBlog

class FeedNoticias(Feed):
    # atributos básicos del feed
    title='Noticias Canal ZOOM'
    link='http://www.zoomcanal.com.co/noticias/'
    description='Noticias publicadas por el Canal Universitario Nacional de Colombia ZOOM'

    def items(self):
        # elementos del feed
        return Noticia.objects.all()

    def item_pubdate(self,item):
        # fecha de publicación utilizada para cada elemento del feed
        return datetime.combine(item.fecha, time())

    def item_author_name(self, item):
        # nombre del autor de cada elemento del feed
        return 'Canal ZOOM'

    def item_description(self, item):
        return item.lead

class FeedEventos(Feed):
    # atributos básicos del feed
    title='Eventos Canal ZOOM'
    link='http://www.zoomcanal.com.co/eventos/'
    description='Eventos publicados por el Canal Universitario Nacional de Colombia ZOOM'

    def items(self):
        # elementos del feed
        return Evento.objects.all()

    def item_pubdate(self,item):
        # fecha de publicación utilizada para cada elemento del feed
        return datetime.combine(item.inicio, time())

    def item_author_name(self, item):
        # nombre del autor de cada elemento del feed
        return 'Canal ZOOM'

    def item_description(self, item):
        return item.descripcion

class FeedOportunidades(Feed):
    # atributos básicos del feed
    title='Oportunidades Canal ZOOM'
    link='http://www.zoomcanal.com.co/oportunidades/'
    description='Oportunidades publicadas por el Canal Universitario Nacional de Colombia ZOOM'

    def items(self):
        # elementos del feed
        return Oportunidad.objects.all()

    def item_pubdate(self,item):
        # fecha de publicación utilizada para cada elemento del feed
        return datetime.combine(item.fecha, time())

    def item_author_name(self, item):
        # nombre del autor de cada elemento del feed
        return 'Canal ZOOM'

    def item_description(self, item):
        return item.descripcion


class FeedEntradasBlogs(Feed):
    # atributos básicos del feed
    title='Blogs Canal ZOOM'
    link='http://www.zoomcanal.com.co/'
    description='Entradas de los blogs en el sitio web del Canal Universitario Nacional de Colombia ZOOM'

    def items(self):
        # elementos del feed
        return EntradaBlog.objects.all()

    def item_pubdate(self,item):
        # fecha de publicación utilizada para cada elemento del feed
        return datetime.combine(item.fecha, time())

    def item_author_name(self, item):
        # nombre del autor de cada elemento del feed
        return 'Canal ZOOM'

    def item_description(self, item):
        return item.lead
