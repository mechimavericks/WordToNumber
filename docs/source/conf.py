# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# Mock imports if needed
# import mock
# sys.modules['some_module'] = mock.Mock()

project = 'WordToNumber'
copyright = '2025, Mechi Mavericks'
author = 'Santosh Bhandari'
release = '1.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # for Google/NumPy-style docstrings
    "sphinx.ext.viewcode",  # for adding links to source code
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# For better Read the Docs integration, consider using this theme:
html_theme = 'sphinx_rtd_theme'  # You'll need to install this

html_static_path = ['_static']

# Add any additional configurations below
autodoc_member_order = 'bysource'