from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from blog.views import EntradaViewSet,UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'links',EntradaViewSet)
router.register(r'user',UserViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^usuario/nuevo$','blog.views.nuevo_usuario', name='nuevo_usuario'),
    url(r'^ingresar/$','blog.views.ingresar', name='ingresar'),
    url(r'^cerrar/$', 'blog.views.cerrar' , name='cerrar'),
    url(r"^about/$" ,'blog.views.acerca', name='about'),
    url(r"^post/(?P<pk>\d+)/$" ,'blog.views.post', name='post'),
    url(r'^categoria/(\d+)$', 'blog.views.categoria', name='categoria'),
    url(r'^subcategoria/(\d+)$', 'blog.views.subcategoria', name='subcategoria'),
    url(r'^plus/(\d+)$', 'blog.views.plus', name='plus'),
    url(r'^minus/(\d+)$', 'blog.views.minus', name='minus'),
    url(r'^add/$', 'blog.views.add', name='add'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    #url(r'^chaining/', include('smart_selects.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})) 

# url(r'^SitioGeek/', include('SitioGeek.foo.urls')),