#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# THEME = "./pelican-themes/mnmlist"
# THEME = "./pelican-themes/elegant"  # Nice categories BUT articles are narrow
# THEME = "./pelican-themes/aboutwilson"  # archive has nice categories, but main page/structure sucks.

# THEME = "./pelican-themes/pelican-simplegrey"  # No effect...hmmmm
# 

# sudo netstat -tulpn | grep :8000

AUTHOR = 'Kevin Wall'
SITENAME = 'College Baseball'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Canada/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('CBN articles', 'https://www.canadianbaseballnetwork.com/canadian-baseball-network-articles/?author=58c9e297893fc030cbdfe760'),
    ('College Wrap', 'https://www.canadianbaseballnetwork.com/canadian-baseball-network-articles/college-wrap-week-xvi'),
    ('Canadian in College', 'https://www.canadianbaseballnetwork.com/new-blog-62//2017-canadians-in-college'))

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Aug 12, 2017 https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['ipynb.markup']


STATIC_PATHS = ['theme/images', 'images']





# PLUGINS = ['ipynb.markup', 'sitemap', 'extract_toc', 'tipue_search']

# Aug 14, 2017 Elegant - Technical nitty gritty
# http://oncrashreboot.com/elegant-best-pelican-theme-features

# PLUGINS = PLUGINS + ['sitemap', 'extract_toc', 'tipue_search']
# MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
# MARKDOWN = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
# DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
# STATIC_PATHS = ['theme/images', 'images']
# TAG_SAVE_AS = ''
# CATEGORY_SAVE_AS = ''
# AUTHOR_SAVE_AS = ''
# ---
# RECENT_ARTICLES_COUNT (integer)  
# COMMENTS_INTRO ('string')
# SITE_LICENSE ('string')
# SITE_DESCRIPTION = 'SITE DESCRIPTION'
# EMAIL_SUBSCRIPTION_LABEL ('string')
# EMAIL_FIELD_PLACEHOLDER ('string')
# SUBSCRIBE_BUTTON_TITLE ('string')
# MAILCHIMP_FORM_ACTION ('string')
# SITESUBTITLE ('string')
# LANDING_PAGE_ABOUT ({})
# PROJECTS ([{},...])

# https://github.com/fle/pelican-sober
# PELICAN_SOBER_ABOUT = "College baseball stats"
# PELICAN_SOBER_STICKY_SIDEBAR = True


