import os
import sys
import django

sys.path.insert(0, os.path.abspath('../sticky_notes'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sticky_notes.settings')
django.setup()

project = 'Sticky Notes Django Project'
author = 'Mpho Ramodike'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'alabaster'
