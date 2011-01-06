from django.conf.urls.defaults import *
from easy_pages.models import Page

active_pages = Page.objects.filter(published=True, page_type='norm')

urlpatterns = patterns('easy_pages.views',
                       *[('^'+p.get_absolute_url()[1:]+'$',
                          'easy_page',
                          {'page':p,}
                         )
                         for p in active_pages]
                       )
