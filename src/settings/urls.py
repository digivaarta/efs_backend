from src.switch import SUB_DOMAIN_SETTING


if SUB_DOMAIN_SETTING:
    ROOT_URLCONF = 'urls.urls'
    ROOT_HOSTCONF = 'src.hosts'
    DEFAULT_HOST = 'admin'
    MIDDLEWARE = [
        #'silk.middleware.SilkyMiddleware',
        'django_hosts.middleware.HostsRequestMiddleware',
        'django_hosts.middleware.HostsResponseMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        #'account.middleware.TimeDelayMiddleware'

    ]
else:
    ROOT_URLCONF = 'urls.master_urls'
    ROOT_HOSTCONF = 'src.dev_hosts'
    DEFAULT_HOST = 'www'
    MIDDLEWARE = [
        #'silk.middleware.SilkyMiddleware',
        'django_hosts.middleware.HostsRequestMiddleware',
        'django_hosts.middleware.HostsResponseMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        #'account.middleware.TimeDelayMiddleware'

    ]