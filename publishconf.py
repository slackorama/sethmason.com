#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://sethmason.com'
RELATIVE_URLS = False

FEED_ATOM="sethmason"
FEED_DOMAIN="http://feeds.feedburner.com"

FEED_ALL_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

GOOGLE_ANALYTICS='UA-2071015-1'
GOOGLE_ANALYTICS_SITENAME='sethmason.com'
DISQUS_SITENAME='seths-blog'

