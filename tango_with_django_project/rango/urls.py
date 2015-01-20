from django.conf.urls import patterns, url
from rango import views

# This tuple must be called urlmappings for Django to pick up our URL
# mappings.

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'about/', views.about, name='about'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
                           views.category,
                           name = 'category'),
                       )

