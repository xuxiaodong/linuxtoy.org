#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'toy'
SITENAME = u'LinuxTOY'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'
DEFAULT_CATEGORY = 'News'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

SUMMARY_MAX_LENGTH = 30
DEFAULT_PAGINATION = 10

DISQUS_SITENAME = 'linuxtoy'
GOOGLE_ANALYTICS = 'UA-349050-2'

ARTICLE_URL = 'archives/{slug}.html'
ARTICLE_SAVE_AS = 'archives/{slug}.html'

YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/index.html'

FEED_ALL_ATOM = 'feeds/all.atom.xml'

THEME = 'themes/itoy'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-page-order', 'summary', 'neighbors', 'related_posts']
