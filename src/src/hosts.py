from django.conf import settings
from django_hosts import patterns, host
host_patterns = patterns(
    '',
    #host(r'www', 'urls.master_urls', name='www'),
    host(r'efs', 'urls.master_urls', name='efs'),
    #host(r'efs', 'urls.api_urls', name='api'),
    # host(r'docs','urls.docs_urls',name="docs"),
    # host(r'performance','src.performance_urls',name="performance"),
)
