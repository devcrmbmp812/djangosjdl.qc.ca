#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals



import os
import sys
#import locale

#os.environ['LC_ALL'] = 'fr_CA.UTF-8'

######################
# MEZZANINE SETTINGS #
######################

# The following settings are already defined with default values in
# the ``defaults.py`` module within each of Mezzanine's apps, but are
# common enough to be put here, commented out, for convenient
# overriding. Please consult the settings documentation for a full list
# of settings Mezzanine implements:
# http://mezzanine.jupo.org/docs/configuration.html#default-settings

# Controls the ordering and grouping of the admin menu.
#
ADMIN_MENU_ORDER = (
    ("Content", ("pages.Page", ("Bibliothèque de médias", "fb_browse"),)),
    ("Actualités", ("news.News","events.Events","infotravaux.InfoTravaux")),
    ("Emplois", ("careers.Careers",)),
    ("Coordonnées", ("coordonnees.Coordonnees",)),
    ("FAQ", ("faq.Faq",)),
    ("Formulaires", ("animaux.EnregistrementChien",)),
    ("Documentation", ("documentation.ProcesVerbauxConseil","documentation.ProcesVerbauxRegieAssainissement","documentation.ProcesVerbauxRegieTraitement","documentation.InformationsFinancieres","documentation.BulletinsMunicipaux","documentation.CalendriersMunicipaux","documentation.CommuniquesPresse","documentation.AvisPublics","documentation.InfoLoisirs")),
    ("Liens", ("usefullinks.UsefulLinks","usefullinks.RepertoryLinks")),
    ("Recherche Bacs", (("Collectes","sjdl.searchbac.admin_views.recherche_bacs_list"),)),
    ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
    ("Users", ("auth.User", "auth.Group",)),
)

# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
#
DASHBOARD_TAGS = (
    ("mezzanine_tags.app_list"),
    ("comment_tags.recent_comments",),
    ("mezzanine_tags.recent_actions",),
)

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

PAGE_MENU_TEMPLATES = (
    (1, "Navigation principale", "pages/menus/dropdown.html"),
    (2, "Plan du site", "pages/menus/tree.html"),
    (3, "Top menu", "pages/menus/top.html"),
    (4, "Menu de gauche", "pages/menus/side.html"),
)

PAGES_MENU_SHOW_ALL = False

# A sequence of fields that will be injected into Mezzanine's (or any
# library's) models. Each item in the sequence is a four item sequence.
# The first two items are the dotted path to the model and its field
# name to be added, and the dotted path to the field class to use for
# the field. The third and fourth items are a sequence of positional
# args and a dictionary of keyword args, to use when creating the
# field instance. When specifying the field class, the path
# ``django.models.db.`` can be omitted for regular Django model fields.
#
EXTRA_MODEL_FIELDS = (
#     (
#         # Dotted path to field.
#         "mezzanine.blog.models.BlogPost.image",
#         # Dotted path to field class.
#         "somelib.fields.ImageField",
#         # Positional args for field class.
#         ("Image",),
#         # Keyword args for field class.
#         {"blank": True, "upload_to": "blog"},
#     ),
#     # Example of adding a field to *all* of Mezzanine's content types:
#     (
#         "mezzanine.pages.models.Page.another_field",
#         "IntegerField", # 'django.db.models.' is implied if path is omitted.
#         ("Another name",),
#         {"blank": True, "default": 1},
#     ),
     (
         # Dotted path to field.
         "mezzanine.galleries.models.GalleryImage.credits",
         # Dotted path to field class.
         "CharField",
         # Positional args for field class.
         ("Credits",),
         # Keyword args for field class.
         {"blank": True, "null":True, "max_length":200},
     ),
    (
         # Dotted path to field.
         "mezzanine.galleries.models.GalleryImage.title",
         # Dotted path to field class.
         "CharField",
         # Positional args for field class.
         ("Titre",),
         # Keyword args for field class.
         {"blank": True, "null":True, "max_length":200},
     ),
 )

# Setting to turn on featured images for blog posts. Defaults to False.
#
# BLOG_USE_FEATURED_IMAGE = True

# If True, the south application will be automatically added to the
# INSTALLED_APPS setting.
USE_SOUTH = True


########################
# MAIN DJANGO SETTINGS #
########################

# People who get code error notifications.
# In the format (('Full Name', 'email@example.com'),
#                ('Full Name', 'anotheremail@example.com'))
ADMINS = (
    ('PythonWall', 'programmeurs@cybergeneration.com'),
)

# Code pour filtrer les erreurs de http host sur django 1.6
def skip_suspicious_operations(record):
    if record.name == 'django.security.DisallowedHost':
        return False
    return True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'skip_suspicious_operations': {
        '()': 'django.utils.log.CallbackFilter',
        'callback': skip_suspicious_operations,
    }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false', 'skip_suspicious_operations'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
    }
}

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
#ALLOWED_HOSTS = ['127.0.0.1', 'sjdl.dev', 'dev.sjdl.qc.ca', 'sjdl.qc.ca','www.sjdl.qc.ca']
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "America/Montreal"

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = False

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "fr-CA"

DEFAULT_CHARSET = "utf-8"

# Supported languages
_ = lambda s: s
LANGUAGES = (
    ('fr', _('Francais')),
)

# A boolean that turns on/off debug mode. When set to ``True``, stack traces
# are displayed for error pages. Should always be set to ``False`` in
# production. Best set to ``True`` in local_settings.py
DEBUG = False

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Tuple of IP addresses, as strings, that:
#   * See debug comments, when DEBUG is true
#   * Receive x-headers
INTERNAL_IPS = ("127.0.0.1",)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# The numeric mode to set newly-uploaded files to. The value should be
# a mode you'd pass directly to os.chmod.
FILE_UPLOAD_PERMISSIONS = 0o644

#############
# DATABASES #
#############

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'sjdl_db1',
        'USER': 'sjdl_db1',
        'PASSWORD': 'iwodSKpwjd62',
        'HOST': 'localhost'
    }
}


#########
# PATHS #
#########

import os

# Full filesystem path to the project.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

#print PROJECT_ROOT

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'news'))


# Name of the directory for the project.
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]

# Every cache key will get prefixed with this value - here we set it to
# the name of the directory the project is in to try and use something
# project specific.
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = STATIC_URL + "media/"

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))

# Package/module name to import the root urlpatterns from for the project.
ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME

# Put strings here, like "/home/html/django_templates"
# or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)
#os.path.join(os.path.dirname(__file__), '..', 'templates'),

SEARCH_MODEL_CHOICES = ["news.News","events.Events","usefullinks.Repertorylinks","documentation.ReglementsMunicipaux","pages.Page","careers.Careers","infotravaux.Infotravaux"]


################
# APPLICATIONS #
################

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.pages",
    "mezzanine.galleries",
    #"mezzanine.twitter",
    #"mezzanine.accounts",
    #"mezzanine.mobile",
    "widget_tweaks",
    "crispy_forms",
    "import_export",

    "sjdl.common",
    "sjdl.news",
    "sjdl.events",
    "sjdl.documentation",
    "sjdl.careers",
    "sjdl.infotravaux",
    "sjdl.usefullinks",
    "sjdl.coordonnees",
    "sjdl.cyberimpact",
    "sjdl.faq",
    "sjdl.shortcodes",
    "sjdl.searchbac",
    "sjdl.animaux",

    "south",
)

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "mezzanine.conf.context_processors.settings",
    "mezzanine.pages.context_processors.page",
)

# List of middleware classes to use. Order is important; in the request phase,
# these middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE_CLASSES = (
    "mezzanine.core.middleware.UpdateCacheMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "mezzanine.core.request.CurrentRequestMiddleware",

    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    # Uncomment the following if using any of the SSL settings:
    # "mezzanine.core.middleware.SSLRedirectMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
)

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

#########################
# OPTIONAL APPLICATIONS #
#########################

# These will be added to ``INSTALLED_APPS``, only if available.
OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)

FILEBROWSER_DIRECTORY = 'uploads/'

FILEBROWSER_MAX_UPLOAD_SIZE = "10485760" #10MB

#Use this line to auto generate slugs with NO ACCENTs
#Default uses mezzanine slug generator that keeps accents in urls
SLUGIFY = 'django.template.defaultfilters.slugify'

#Set this variable to true to show the placeholder field in the FormPage in admin
FORMS_USE_HTML5 = True

TINYMCE_SETUP_JS = 'js/tinymce-options.js'





###################
# DEPLOY SETTINGS #
###################

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "SSH_USER": "", # SSH username for host deploying to
#     "HOSTS": ALLOWED_HOSTS[:1], # List of hosts to deploy to (eg, first host)
#     "DOMAINS": ALLOWED_HOSTS, # Domains for public site
#     "REPO_URL": "ssh://hg@bitbucket.org/user/project", # Project's repo URL
#     "VIRTUALENV_HOME":  "", # Absolute remote path for virtualenvs
#     "PROJECT_NAME": "", # Unique identifier for project
#     "REQUIREMENTS_PATH": "requirements.txt", # Project's pip requirements
#     "GUNICORN_PORT": 8000, # Port gunicorn will listen on
#     "LOCALE": "en_US.UTF-8", # Should end with ".UTF-8"
#     "DB_PASS": "", # Live database password
#     "ADMIN_PASS": "", # Live admin user password
#     "SECRET_KEY": SECRET_KEY,
#     "NEVERCACHE_KEY": NEVERCACHE_KEY,
# }


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '10.20.30.33'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False

ENREGISTREMENT_CHIEN_EMAIL_SUBJECT = 'Enregistrement d\'un chien'
ENREGISTREMENT_CHIEN_EMAIL_ADDRESS_TO = 'medaille@sjdl.qc.ca'
ENREGISTREMENT_CHIEN_EMAIL_ADDRESS_FROM = 'medaille@sjdl.qc.ca'

##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.
try:
    from local_settings import *
except ImportError as e:
    if "local_settings" not in str(e):
        raise e


####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
