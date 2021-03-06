# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

import os

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'indexes'

USE_I18N = True

gettext = lambda s: s

LANGUAGE_CODE = 'en'
LANGUAGES = (
	('en', gettext('English')),
	('de', gettext('German')),
	('sp', gettext('Spanish')),
)

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

AUTHENTICATION_BACKENDS = (
	'permission_backend_nonrel.backends.NonrelPermissionBackend',
)

#DOJANGO_DATAGRID_ACCESS = (
#	'loans.MortgageOriginator',
#	'loans.Loan',
#	'bids.Bid',
#	'engine.Loan',
#	'engine.Bid',
#	'engine.UserFunds',
#	'engine.BidsAllocation',
#)

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.contenttypes',
	'django.contrib.auth',
	'django.contrib.sessions',
	'django.contrib.staticfiles',
	'djangotoolbox',
	'dojango',
	'datable',
	# It's important to put 'permission_backend_nonrel after djangotoolbox,
	# because 'permission_backend_nonrel.admin replaces djangotoolbox's User
	# admin site. 
	'permission_backend_nonrel',
	'autoload',
	'dbindexer',
	#'djmoney',
	'loans',
	'bids',
	'engine',
	'home',
	'search',
	'login',
	'users',
	# djangoappengine should come last, so it can override a few manage.py commands
	'djangoappengine',
	#'django_iso8601',
	#'isodate',
	#'iso8601',
	#'xlwt',
)

MIDDLEWARE_CLASSES = (
	# This loads the index definitions, so it has to come first
	'autoload.middleware.AutoloadMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'dojango.middleware.AJAXSimpleExceptionResponse',
	'dojango.middleware.DojoCollector',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.middleware.csrf.CsrfResponseMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.request',
	'django.core.context_processors.static',
	'django.core.context_processors.media',
	#'dojango.context_processors.config',
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'))
		#os.path.join(os.path.dirname(__file__), 'dojango/templates'),
#TEMPLATE_DIRS = (
#	'/home/juanfe/Vichara/liquidity/Web/templates',
#)

ROOT_URLCONF = 'urls'

#TODO add relative dir as in TEMPLATE_DIRS
STATICFILES_DIRS = (
	os.path.join(os.path.dirname(__file__), 'static'),
	os.path.join(os.path.dirname(__file__), 'scripts'),
	os.path.join(os.path.dirname(__file__), 'css'),
)

STATIC_URL = '/static/'

#DOJANGO Configuration variables
# See https://github.com/klipstein/dojango/wiki/Configuration

#DOJANGO_DOJO_PROFILE = "google"

#DOJANGO_DOJO_VERSION = "1.5.0"

#DOJANGO_DOJO_PROFILE = "local_release" # local, local_release, google, aol
#DOJANGO_DOJO_VERSION = "1.4.0-dojango-with-dojo"

DOJANGO_DOJO_THEME = "claro" #Available "tundra", "soria", or "nihilo"

#DOJANGO_DOJO_THEME_URL #It defaults to dojo base url/dijit/themes and there
						#you can look at the dojo theme structure, e.g.:
						#_dojo base url_/dijit/themes/tundra
						#_dojo base url_/dijit/themes/tundra/tundra.css

DOJANGO_DOJO_DEBUG = True

#DOJANGO_CDN_USE_SSL = True

#DOJANGO_DOJO_MEDIA_URL #default: "dojo-media"

#DOJANGO_BASE_MEDIA_URL #default: /dojango/ + DOJANGO_DOJO_MEDIA_URL

#DOJANGO_BUILD_MEDIA_URL #default: DOJANGO_BASE_MEDIA_URL + "/release"

#DOJANGO_BASE_MEDIA_ROOT #default: _django project directory_/dojango/media
#With this config, each app can have his own dojo media
DOJANGO_BASE_MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "dojo-media"))

DOJANGO_DOJO_BUILD_PROFILES = {
	'liq-spot': {
		'options': 'profileFile="%(BASE_MEDIA_ROOT)s/liq-spot.profile.js" action=release optimize=shrinksafe.keepLines cssOptimize=comments.keepLines',
	},
}

#DOJANGO_BASE_DOJO_ROOT #default: DOJANGO_BASE_MEDIA_ROOT + "/dojo")

