#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Steven Pav'
SITENAME = u'minimum-viable-parenting'
SITEURL = u'http://www.minimum-viable-parenting.com'
AUTHOR_EMAIL = u'steven@minimum-viable-parenting.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = u'misc'

HOME = os.environ['HOME']
THEME = HOME + '/github/pelican-themes/nmnlist'

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),)
LINKS = ()

# Social widget
SOCIAL = (('Twitter', 'http://www.twitter.com/gilgamath'),)

DEFAULT_PAGINATION = 10

# see http://docs.getpelican.com/en/latest/tips.html
STATIC_PATHS = ['images', 'extra/CNAME', 'extra/geetignore']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
        'extra/geetignore': {'path': '.gitignore'},}

SUMMARY_MAX_LENGTH = 100

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

