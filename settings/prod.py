from regluit.settings.common import *

ALLOWED_HOSTS = ['.unglue.it']
DEBUG = False
TEMPLATE_DEBUG = DEBUG
# we are launched!
IS_PREVIEW = False

SITE_ID = 1

ADMINS = (
    ('Raymond Yee', 'rdhyee+ungluebugs@gluejar.com'),
    ('Eric Hellman', 'eric@gluejar.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'unglueit',
        'USER': 'root',
        'PASSWORD': 'unglue1t',
        'HOST': 'production.cboagmr25pjs.us-east-1.rds.amazonaws.com',
        'PORT': '',
        'TEST_CHARSET': 'utf8',
    }
}

TIME_ZONE = 'America/New_York'
SECRET_KEY = u'_^_off!8zsj4+)%qq623m&$7_m-q$iau5le0w!mw&n5tgt#x=t'

# settings for outbout email
# if you have a gmail account you can use your email address and password

#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'accounts@gluejar.com'
#EMAIL_HOST_PASSWORD = '7k3sWyzHpI'
#EMAIL_PORT = 587
#DEFAULT_FROM_EMAIL = 'accounts@gluejar.com'

# testing out using Amazon SES

EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
MAIL_USE_TLS = True 
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_HOST_USER = 'AKIAJXM4QX324HXCH54Q'
EMAIL_HOST_PASSWORD = 'AgR9hVmSSOhetuLOnbFEFo9PTnL9iAM/52NOPGkS3Rwh'
EMAIL_PORT = 465
DEFAULT_FROM_EMAIL = 'notices@gluejar.com'

# googlebooks
# key generated by rdhyee@gluejar.com 2013/07/02
GOOGLE_BOOKS_API_KEY = 'AIzaSyAGUEeGJXXLj9Tau4fpIFUCdOSKfDmJDVw'

# twitter auth
SOCIAL_AUTH_TWITTER_KEY = 'sd9StEg1N1qB8gGb2GRX4A'
SOCIAL_AUTH_TWITTER_SECRET = 'YSKHn8Du6EWqpcWZ6sp5tqDPvcOBXK0WJWVGWyB0'

# facebook auth
SOCIAL_AUTH_FACEBOOK_KEY = '211951285561911'
SOCIAL_AUTH_FACEBOOK_SECRET = '42efef7e540b80479dbbb69490cd902a'

# get these (as oauth2 client ID and Secret from 
# https://console.developers.google.com/project/569579163337/apiui/credential?authuser=1
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '569579163337-k83htoc5h00mqs4rr6tv22tdcc23jh4r.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'ZyV5Q-E2MkJhRGm42XQAPeZi'

# Goodreads API
GOODREADS_API_KEY = "vfqIO6QAhBVvlxt6hAzZJg"
GOODREADS_API_SECRET = "57tq4MpyJ15Hgm2ToZQQFWJ7vraZzOAqHLckWRXQ"

# Freebase credentials
FREEBASE_USERNAME = ''
FREEBASE_PASSWORD = ''

# send celery log to Python logging
CELERYD_HIJACK_ROOT_LOGGER = False

# Next step to try https
#BASE_URL = 'http://unglue.it'
BASE_URL_SECURE = 'https://unglue.it'
IPN_SECURE_URL = False

# use redis for production queue
BROKER_TRANSPORT = "redis"
BROKER_HOST = "localhost"
BROKER_PORT = 6379
BROKER_VHOST = "0"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'brief': {
            'format': '%(asctime)s %(levelname)s %(name)s[%(funcName)s]: %(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': join('/var/log/regluit', 'unglue.it.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter': 'brief',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        '': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': False,
        },
    }
}

STATIC_ROOT = '/var/www/static'
#CKEDITOR_UPLOAD_PATH = '/var/www/static/media/'
#CKEDITOR_UPLOAD_PREFIX = 'https://unglue.it/static/media/'

# decide which of the period tasks to add to the schedule
CELERYBEAT_SCHEDULE['send_test_email'] = SEND_TEST_EMAIL_JOB
# update the statuses of campaigns
CELERYBEAT_SCHEDULE['update_active_campaign_statuses'] = UPDATE_ACTIVE_CAMPAIGN_STATUSES
CELERYBEAT_SCHEDULE['report_new_ebooks'] = EBOOK_NOTIFICATIONS_JOB
CELERYBEAT_SCHEDULE['notify_ending_soon'] = NOTIFY_ENDING_SOON_JOB
CELERYBEAT_SCHEDULE['update_account_statuses'] = UPDATE_ACCOUNT_STATUSES
CELERYBEAT_SCHEDULE['notify_expiring_accounts'] = NOTIFY_EXPIRING_ACCOUNTS
CELERYBEAT_SCHEDULE['refresh_acqs'] = REFRESH_ACQS_JOB
CELERYBEAT_SCHEDULE['refresh_acqs'] = NOTIFY_UNCLAIMED_GIFTS

# set -- sandbox or production Amazon FPS?
#AMAZON_FPS_HOST = "fps.sandbox.amazonaws.com"
AMAZON_FPS_HOST = "fps.amazonaws.com"

# local settings for maintenance mode
MAINTENANCE_MODE = True

# Amazon keys to permit S3 access
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAIRLBDIET3DFCNU4A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'unglueit-files'

# we should suppress Google Analytics outside of production
SHOW_GOOGLE_ANALYTICS = True

BOOXTREAM_API_KEY = '987n76Zsc4hj9jUvfctxezZQZ2vnhm'
BOOXTREAM_API_USER = 'unglueprod'

# if settings/local.py exists, import those settings -- allows for dynamic generation of parameters such as DATABASES
try:
    from regluit.settings.local import *
except ImportError:
    pass
