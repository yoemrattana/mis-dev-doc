"""
Shared Sphinx configuration.

Each docset corresponds to a directory containing several rst/md files,
sharing this same conf.py file. To build a docset an environment variable
is used, ``RTD_DOCSET``, values given in the settings are relative to this
conf.py file, if you want to give a different value for a docset, use the
``docsets`` dictionary, or if you want to extend the current value,
use f'{docset}/setting' as value on the setting, for example::

    html_static_path = ['_static', f'{docset}/_static']
"""

import os
import sys
from configparser import RawConfigParser

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "readthedocs.settings.dev")

from django.utils import timezone

import django
django.setup()


# Set here the variables you want for each docset.
docsets = {
    'user': {
        'project': 'Read the Docs user documentation',
    },
    'dev': {
        'project': 'Read the Docs developer documentation',
    },
}
docset = os.environ.get('RTD_DOCSET', 'user')
if docset not in docsets:
    print(f'Invalid RTD_DOCSET value: "{docset}"')
    exit(1)

for k, v in docsets[docset].items():
    locals()[k] = v


def get_version():
    """Return package version from setup.cfg."""
    config = RawConfigParser()
    config.read(os.path.join('..', 'setup.cfg'))
    return config.get('metadata', 'version')


sys.path.append(os.path.abspath('_ext'))
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.httpdomain',
    'djangodocs',
    'doc_extensions',
    'sphinx_tabs.tabs',
    'sphinx-prompt',
    'notfound.extension',
    'hoverxref.extension',
    'sphinx_search.extension',
    'sphinxemoji.sphinxemoji',
    'myst_parser',
]

templates_path = ['_templates']

master_doc = 'index'
copyright = '2010-{}, Read the Docs, Inc & contributors'.format(
    timezone.now().year
)
version = get_version()
release = version
exclude_patterns = ['_build']
default_role = 'obj'
intersphinx_mapping = {
    'python': ('https://docs.python.org/3.6/', None),
    'django': ('https://docs.djangoproject.com/en/2.2/', 'https://docs.djangoproject.com/en/2.2/_objects/'),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'pip': ('https://pip.pypa.io/en/stable/', None),
    'nbsphinx': ('https://nbsphinx.readthedocs.io/en/0.8.6/', None),
    'myst-nb': ('https://myst-nb.readthedocs.io/en/v0.12.3/', None),
    'ipywidgets': ('https://ipywidgets.readthedocs.io/en/7.6.3/', None),
    'jupytext': ('https://jupytext.readthedocs.io/en/stable/', None),
    'ipyleaflet': ('https://ipyleaflet.readthedocs.io/en/stable/', None),
    'poliastro': ('https://docs.poliastro.space/en/v0.15.2/', None),
    'qiskit': ('https://qiskit.org/documentation/', None),
    'myst-parser': ('https://myst-parser.readthedocs.io/en/v0.15.1/', None),
    'writethedocs': ('https://www.writethedocs.org/', None),
    'jupyterbook': ('https://jupyterbook.org/', None),
    'myst-parser': ('https://myst-parser.readthedocs.io/en/v0.15.1/', None),
    'rst-to-myst': ('https://rst-to-myst.readthedocs.io/en/stable/', None),
    'rtd': ('https://docs.readthedocs.io/en/stable/', None),
    'rtd-dev': ('https://dev.readthedocs.io/en/latest/', None),
}
myst_enable_extensions = [
    "deflist",
]
hoverxref_intersphinx = [
   "sphinx",
   "pip",
   "nbsphinx",
   "myst-nb",
   "ipywidgets",
   "jupytext",
]
htmlhelp_basename = 'ReadTheDocsdoc'
latex_documents = [
    ('index', 'ReadTheDocs.tex', 'Read the Docs Documentation',
     'Eric Holscher, Charlie Leifer, Bobby Grace', 'manual'),
]
man_pages = [
    ('index', 'read-the-docs', 'Read the Docs Documentation',
     ['Eric Holscher, Charlie Leifer, Bobby Grace'], 1)
]

exclude_patterns = [
    # 'api' # needed for ``make gettext`` to not die.
]

language = 'en'

locale_dirs = [
    f'{docset}/locale/',
]
gettext_compact = False

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static', f'{docset}/_static']
html_css_files = ['css/custom.css', 'css/sphinx_prompt_css.css']
html_js_files = ['js/expand_tabs.js']
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_logo = 'img/logo.svg'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

hoverxref_auto_ref = True
hoverxref_domains = ['py']
hoverxref_roles = [
    'option',
    'doc',
]
hoverxref_role_types = {
    'mod': 'modal',  # for Python Sphinx Domain
    'doc': 'modal',  # for whole docs
    'class': 'tooltip',  # for Python Sphinx Domain
    'ref': 'tooltip',  # for hoverxref_auto_ref config
    'confval': 'tooltip',  # for custom object
}

rst_epilog = """
.. |org_brand| replace:: Read the Docs Community
.. |com_brand| replace:: Read the Docs for Business
"""

# Activate autosectionlabel plugin
autosectionlabel_prefix_document = True

# sphinx-notfound-page
# https://github.com/readthedocs/sphinx-notfound-page
notfound_context = {
    'title': 'Page Not Found',
    'body': '''
<h1>Page Not Found</h1>

<p>Sorry, we couldn't find that page.</p>

<p>Try using the search box or go to the homepage.</p>
''',
}
linkcheck_ignore = [
    r'http://127\.0\.0\.1',
    r'http://localhost',
    r'http://community\.dev\.readthedocs\.io',
    r'https://yourproject\.readthedocs\.io',
    r'https?://docs\.example\.com',
    r'https://foo\.readthedocs\.io/projects',
    r'https://github\.com.+?#L\d+',
    r'https://github\.com/readthedocs/readthedocs\.org/issues',
    r'https://github\.com/readthedocs/readthedocs\.org/pull',
    r'https://docs\.readthedocs\.io/\?rtd_search',
    r'https://readthedocs\.org/search',
    # This page is under login
    r'https://readthedocs\.org/accounts/gold',
]


def setup(app):
    app.srcdir += '/' + docset