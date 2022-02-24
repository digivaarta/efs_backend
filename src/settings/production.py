from .common import *
import os
DEBUG = False

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,"media/")
STATIC_ROOT = os.path.join(BASE_DIR,"sfiles/")
STATICFILES_DIRS = (os.path.join(BASE_DIR,"static/"),)
TIME_ZONE = "Asia/Kolkata"

ALLOWED_HOSTS = ["efs.srcouncil.in",]

INTERNAL_IPS = ALLOWED_HOSTS
USE_L10N = True

#DATABASE SETTINGS

DATABASES = {
    'default': {
        "ENGINE": 'django.db.backends.postgresql',
        "NAME": "efs",
        "USERNAME": "anton",
        "PASSWORD": "bucho",
        "ATOMIC_REQUEST":True,
        "HOST": "",
        "PORT": "",
    }
}

FCM_DJANGO_SETTINGS = {
        "APP_VERBOSE_NAME": "EFS",
         # default: _('FCM Django')
        "FCM_SERVER_KEY": "AAAANaleSYU:APA91bHcyjJJqvmNUtdP05VhSFB90yPvpcHWZDsopZ3_HPLluJ57b0iqxvHtjEcGlbAXZ2WIJGT5z1Exm7BjtCi7K8zgFfBnHOn0A29FvGlOSOFzXFh4p7L80IKEN9XnnrJL-HQ5B25A",
         # true if you want to have only one active device per registered user at a time
         # default: False
        "ONE_DEVICE_PER_USER": True,
         # devices to which notifications cannot be sent,
         # are deleted upon receiving error response from FCM
         # default: False
        "DELETE_INACTIVE_DEVICES": True,
}


#REST FRAMEWORK settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        #'firebase_auth.authentication.FirebaseToken.FokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
         #'django_filters.rest_framework.DjangoFilterBackend',
    ),
    "DEFAULT_PAGINATION_CLASS":"utils.pagination.CustomPagination",
    "PAGE_SIZE":10,
    "DATE_INPUT_FORMATS": ["%d-%m-%Y"],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework_api_key.permissions.HasAPIKey",
    ]
}

REST_AUTH_SERIALIZERS = {
    #'TOKEN_SERIALIZER':'modules.acc_api.serializer.TokenSerializer',
    'USER_DETAILS_SERIALIZER':'modules.auth.serializer.RestAuthSerializer',
}


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis:/var/run/redis/redis.sock',
        #'LOCATION':"redis://134.209.149.129:6379/1"
    },
}

SESSION_ENGINE = 'redis_sessions.session'

SESSION_REDIS_UNIX_DOMAIN_SOCKET_PATH = "/var/run/redis/redis.sock"



#AUTH_USER_MODEL = "acc.user"


# ROOT_URLCONF = 'src.urls'
# ROOT_HOSTCONF = 'src.hosts'
# DEFAULT_HOST = 'www'
# MIDDLEWARE += [
#     #'django_hosts.middleware.HostsRequestMiddleware',
#     #'django_hosts.middleware.HostsResponseMiddleware',
# ]

from .urls import *

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

API_KEY_CUSTOM_HEADER = "HTTP_X_API_KEY"

CORS_ORIGIN_ALLOW_ALL = True

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-Api-Key',
]


CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
'default': {
    # 'skin': 'moono',
    # 'skin': 'office2013',
    'toolbar_Basic': [
        ['Source', '-', 'Bold', 'Italic']
    ],
    'toolbar_YourCustomToolbarConfig': [
        {'name': 'document', 'items': [
            'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates'
        ]},
        {'name': 'clipboard', 'items': [
            'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'
        ]},
        {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
        {'name': 'forms',
         'items': [
             'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea',
             'Select', 'Button', 'ImageButton', 'HiddenField'
         ]},
        '/',
        {'name': 'basicstyles',
         'items': [
             'Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
             'Superscript', '-', 'RemoveFormat'
         ]},
        {'name': 'paragraph',
         'items': [
             'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent',
             '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft',
             'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-',
             'BidiLtr', 'BidiRtl', 'Language'
         ]},
        {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
        {'name': 'insert',
         'items': [
             'Image', 'Table', 'HorizontalRule',
             'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'
         ]},
        '/',
        {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
        {'name': 'colors', 'items': ['TextColor', 'BGColor']},
        {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
        {'name': 'about', 'items': ['About']},
        '/',  # put this to force next toolbar on new line
        {'name': 'yourcustomtools', 'items': [
            # put the name of your editor.ui.addButton here
            'Preview',
            'Maximize',

        ]},
    ],
    'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
    # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
    # 'height': 291,
    # 'width': '100%',
    # 'filebrowserWindowHeight': 725,
    # 'filebrowserWindowWidth': 940,
    # 'toolbarCanCollapse': True,
    # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
    'tabSpaces': 4,
    'extraPlugins': ','.join([
        'uploadimage',  # the upload image feature
        # your extra plugins here
        'div',
        'autolink',
        'autoembed',
        'embedsemantic',
        'autogrow',
        # 'devtools',
        'widget',
        'lineutils',
        'clipboard',
        'dialog',
        'dialogui',
        'elementspath'
    ]),
    }
}

AUTH_USER_MODEL = "account.User"
