from django.conf.urls import patterns, include, url

from django.contrib import admin
from Cadastro.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SistemaFinanceiroJR.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^homepage/$','Cadastro.views.homepage',name='homepage'),
    #contato
    url(r'^contato/novo/$','Cadastro.views.edita_contato', name='novo_contato'),
    url(r'^contato/(?P<contato_id>\d+)/$','Cadastro.views.edita_contato', name='edita_contato'),
    url(r'^contato/excluir/(?P<contato_id>\d+)/$','Cadastro.views.excluir_contato', name='excluir_contato'),
    url(r'^contatos/$', 'Cadastro.views.Contatos', name='Contatos'),
    url(r'^contato/search/$','Cadastro.views.search_contato', name='search_contato'),


    #produto
    url(r'^produto/novo/$','Cadastro.views.edita_produto', name='novo_produto'),
    url(r'^produto/(?P<produto_id>\d+)/$','Cadastro.views.edita_produto', name='edita_produto'),
    url(r'^produto/excluir/(?P<produto_id>\d+)/$','Cadastro.views.excluir_produto', name='excluir_produto'),
    url(r'^produto/search/$', 'Cadastro.views.search_produto', name='search_produto'),
   # url(r'^produto/search/$','Cadastro.views.search_contato', name='search_contato'),


   #NaoImplementado
   url(r'^faltaimplementacao/$','Cadastro.views.falta_implementacao',name='semImplementacao'),

   #about
   url(r'^about/$','Cadastro.views.about',name='about'),
)
