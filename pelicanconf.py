#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

THEME = "theme/sethmason"

AUTHOR = 'Seth Mason <seth@sethmason.com'
SITENAME = 'All things Seth Mason'
SITEURL = ''
DEFAULT_CATEGORY = 'blog'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# urls
ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
YEAR_ARCHIVE_SAVE_AS="{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS="{date:%Y}/{date:%m}/index.html"
DAY_ARCHIVE_SAVE_AS="{date:%Y}/{date:%m}/{date:%d}/index.html"
PAGE_URL="{slug}.html"
PAGE_SAVE_AS="{slug}.html"

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/google89d432cbb0319848.html': {'path':
        'google89d432cbb0319848.html'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/.htaccess': {'path': '.htaccess'},
    }
STATIC_PATHS = [
    'images',
    'extra',
    ]

ARTICLE_EXCLUDES=['extra']

DEFAULT_PAGINATION = 20

TWITTER_USERNAME='slackorama'
GITHUB_URL='https://github.com/slackorama'
LINKEDIN_URL='http://www.linkedin.com/pub/sethmason'
FACEBOOK_URL='http://www.facebook.com/sethmason'
INSTAGRAM_URL='https://www.instagram.com/slackorama'
GOODREADS_URL='https://www.goodreads.com/user/show/1519786-slackorama'
STRAVA_URL='https://www.strava.com/athletes/16584859'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# PLUGIN_PATHS = [os.path.expanduser("~/projects/pelican-plugins")]
PLUGINS=['pelican.plugins.sitemap', 'pelican.plugins.webassets']

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
