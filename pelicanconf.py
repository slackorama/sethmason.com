#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = "theme/sethmason"

AUTHOR = u'Seth Mason <seth@sethmason.com>'
SITENAME = u'All things Seth Mason'
SITEURL = 'http://sethmason.com'
DEFAULT_CATEGORY='blog'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# urls
ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
YEAR_ARCHIVE_SAVE_AS="{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS="{date:%Y}/{date:%m}/index.html"
DAY_ARCHIVE_SAVE_AS="{date:%Y}/{date:%m}/{date:%d}/index.html"
PAGE_URL="{slug}.html"
PAGE_SAVE_AS="{slug}.html"

PDF_GENERATOR = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/google89d432cbb0319848.html': {'path':
        'google89d432cbb0319848.html'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    }
STATIC_PATHS = [
    'images',
    'extra',
    ]

RELATIVE_URLS = True

ARTICLE_EXCLUDES=['extra']

TWITTER_USERNAME='slackorama'
GITHUB_URL='https://github.com/slackorama'
LINKEDIN_URL='http://www.linkedin.com/pub/sethmason'
FACEBOOK_URL='http://www.facebook.com/sethmason'

PLUGIN_PATHS = ["plugins/pelican/plugins"]
PLUGINS=['sitemap',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
