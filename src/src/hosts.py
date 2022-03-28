from django.conf import settings
from django_hosts import patterns, host
host_patterns = patterns(
    '',
    #host(r'www', 'urls.master_urls', name='www'),
    host(r'admin', 'urls.urls', name='admin'),
    host(r'api', 'urls.api_urls', name='api'),
    # host(r'docs','urls.docs_urls',name="docs"),
    # host(r'performance','src.performance_urls',name="performance"),
)
