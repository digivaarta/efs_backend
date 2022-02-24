from django.conf import settings
from django_hosts import patterns, host
host_patterns = patterns(
    '',
    host(r'www', 'urls.master_urls', name='www'),
    
)
