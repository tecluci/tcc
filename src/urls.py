from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'src.questao.views.home', name='home'),
    url(r'^questionario/(?P<id>\d+)/$', 'src.questao.views.questionario', name='questionario'),
    url(r'^send-post/$', 'src.questao.views.senderpost', name='senderpost'),
    url(r'^send-post2/$', 'src.questao.views.senderpost2', name='senderpost2'),
    url(r'^relatorio/(?P<id_cat>\d+)/$', 'src.questao.views.report', name='report'),
    # url(r'^src/', include('src.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))