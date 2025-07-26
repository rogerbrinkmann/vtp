# publishconf.py

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
# IMPORTANT: Replace YOUR_GITHUB_USERNAME and YOUR_REPOSITORY_NAME
SITEURL = "https://rogerbrinkmann.github.io/vtp"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True # Recommended for clean builds

# Following items are often useful when publishing
# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""