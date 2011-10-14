from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'network_portal.views.home', name='home'),
    # url(r'^network_portal/', include('network_portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # kmf: adding haystack search URLconf
    (r'^search/', include('haystack.urls')),

    #(r'^analysis/$', 'web_app.networks.views.analysis', name='analysis'),
    #(r'^analysis/$', include('analysis.urls')),
    (r'^analysis/gene/$', 'networks.views.gene'),
    (r'^analysis/network/$', 'networks.views.network'),
    (r'^analysis/motif/$', 'networks.views.motif'),
    (r'^analysis/function/$', 'networks.views.function'),

    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL }),

)
urlpatterns += staticfiles_urlpatterns()
