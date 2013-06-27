from django.conf.urls import patterns, include, url
from test_server.views import hello, index, process_xml, process_SMS, write_XML
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index),                   
    url(r'^hello/$',hello),
    url(r'^process_xml/$',process_xml),
    url(r'^process_SMS/$',process_SMS),
    url(r'^write_XML/$',write_XML),
    # Examples:
    # url(r'^$', 'test_server.views.home', name='home'),
    # url(r'^test_server/', include('test_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
