#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matt Craig'
SITENAME = u'Py hole'
SITEURL = 'http://mwcraig.github.io'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'
#DEFAULT_DATE = 'fs'  # use file timestamp
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = False

# Blogroll

# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['liquid_tags.notebook', 'tag_cloud', 'tipue_search']

# cruft for manually including notebooks
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

THEME = "pelican-bootstrap3"
SITELOGO = None
SITETAGLINE = "It's best to keep it shut"

# pelican-bootstrap3
BOOTSTRAP_THEME = 'sandstone'
FAVICON = 'favicon.png'

DISPLAY_ARTICLE_INFO_ON_INDEX = True

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True

BANNER = 'static/skinny-buttes.jpg'
BANNER_SUBTITLE = "It's best to keep it shut"

CUSTOM_CSS = 'static/custom.css'

SHARIFF = True
SHARIFF_LANG = 'en'
SHARIFF_THEME = 'gray'
# Tell Pelican to add 'extra/custom.css' to the output dir
STATIC_PATHS = ['images', 'extra']

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/skinny-buttes.jpg': {'path': 'static/skinny-buttes.jpg'},
    'extra/concrete-wall.png': {'path': 'static/concrete-wall.png'},
    'extra/bison-mine.png': {'path': 'favicon.png'}
}

# ABOUT_ME = "Daughter of the day: Emma"

SOCIAL = (('github', 'https://github.com/mwcraig'),
          ('twitter', 'http://twitter.com/astronomatty'),
          ('facebook', 'https://www.facebook.com/matthew.craig.94043'),
          ('linkedin', 'www.linkedin.com/in/mwcraig'),)

GITHUB_USER = 'mwcraig'


DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
PYGMENTS_STYLE = 'monokai'

BOOTSTRAP_NAVBAR_INVERSE = False

# plumage
# MENUITEMS = (
#     ('Home', '/'),
#     ('Archive', 'archives.html'),
#     ('Code', '/code/'),
#     ('Themes', '/themes/'),
#     ('About', '/about/'),
# )

# For chameleon
# AUTHORS = {}

# MENUITEMS = [
#     ('Home', '/'),
#     ('Archives', [
#         ('Tags', '/tags.html'),
#         ('Categories', '/categories.html'),
#         ('Chronological', '/archives.html'),
#         ]),
#     ('Social', [
#         ('Email', 'mailto: maurelinus@stoic.edu'),
#         ('Github', 'http://url-to-github-page'),
#         ('Facebook', 'http://url-to-facebook-page'),
#         ]),
#     ]

#BS3_THEME = 'http://bootswatch.com/sandstone/bootstrap.min.css'
# sober
#PELICAN_SOBER_STICKY_SIDEBAR = True

# something else

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
