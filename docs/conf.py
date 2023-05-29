import datetime
import os
import sys

import pyramid_apispec

sys.path.insert(0, os.path.abspath(".."))

assert pyramid_apispec

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_issues",
]

primary_domain = "py"
default_role = "py:obj"

intersphinx_mapping = {
    "python": ("https://python.readthedocs.io/en/latest/", None),
    "marshmallow": ("https://marshmallow.readthedocs.io/en/latest/", None),
    "pyramid": ("https://docs.pylonsproject.org/projects/pyramid/en/latest/", None),
}
issues_github_path = "Mix-Anik/pyramid-apispec"

source_suffix = ".rst"
master_doc = "index"
project = "pyramid-apispec"
copyright = "Mix-Anik, Joshua Carp and contributors {:%Y}".format(datetime.datetime.utcnow())

exclude_patterns = ["_build"]

# THEME

# on_rtd is whether we are on readthedocs.io
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

if not on_rtd:  # only import and set the theme if we're building docs locally
    # import pydata_sphinx_theme

    html_theme = "pydata_sphinx_theme"
    # html_theme_path = [pydata_sphinx_theme.get_html_theme_path()]
