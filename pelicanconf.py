AUTHOR = 'Roger'
SITENAME = 'Value of True Parents'
SITEURL = "http://127.0.0.1:8000"  # IMPORTANT: Changed to match the address Pelican serves on

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'EN'
THEME = 'themes/custom_theme' # IMPORTANT: This path now matches your theme directory name

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Roger", "https://rogerb.de/"),
)

# Social widget (uncomment and fill if you want to use it)
# SOCIAL = (
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# )

DEFAULT_PAGINATION = True

# URL settings for pages and articles
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
ARTICLE_URL = '{slug}.html' # Default, but good to be explicit
ARTICLE_SAVE_AS = '{slug}.html' # Default, but good to be explicit

# Add this to generate a static page from your toc.html template
TEMPLATE_PAGES = {'toc.html': 'table-of-contents.html'}

# Menu items for your navigation (as used in base.html)
MENUITEMS = (
    # ('About', '/pages/about/'), # Example for a 'pages' link
    ('Archives', '/archives.html'), # Pelican automatically generates an archives page
    ('Tags', '/tags.html'),         # Pelican automatically generates a tags page
    ('Table of Contents', '/table-of-contents.html'), # New: Link to your TOC page
)

# Set to False to generate absolute URLs (recommended for deployment)
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True # Recommended for clean builds
