# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'FreeTaxUSA 2025'
copyright = '2025, FreeTaxUSA Guide'
author = 'FreeTaxUSA Help Center'

# The full version, including alpha/beta/rc tags
release = '2026'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (leave blank or add as needed)
extensions = []

# Allow reStructuredText raw HTML (needed for buttons & styling)
raw_enabled = True

# Templates and patterns to ignore
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (optional)
# html_theme = 'sphinx_rtd_theme'

# Basic page info (SEO-friendly)
html_title = "FreeTaxUSA 2025 | File Taxes Online & Account Guide"
html_short_title = "FreeTaxUSA 2025"

# Favicon (place in _static or root folder)
html_favicon = 'favicon.ico'

# Hide "View page source"
html_show_sourcelink = False

# Allow unsafe raw HTML in .rst files
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static assets (uncomment if used)
# html_static_path = ['_static']
