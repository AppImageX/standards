# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath("."))


# -- Project information -----------------------------------------------------

project = "AppImageX Standards"
copyright = "2020, The AppImageX Team"
author = "The AppImageX Team"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx_last_updated_by_git",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "display_version": True,
    "sticky_navigation": True,
    "includehidden": True,
    "collapse_navigation": True,
    "titles_only": True,
    "prev_next_buttons_location": "both",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# try to fetch current Git commit ID from the environment
commit = os.environ.get("GITHUB_SHA", os.environ.get("GIT_COMMIT", None))

# if this is not possible for some reason, try to fetch it via the git command
if not commit:
    import subprocess
    try:
        commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode().split()[0]
    except subprocess.CalledProcessError:
        commit = "<not available>"

# make sure to use short commit
commit = commit[:7]

html_context = {
    "display_github": True,
    "github_user": "AppImage",
    "github_repo": "docs.appimage.org",
    "github_version": "master/source/",
    "commit": commit,
}

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"https://docs.python.org/": None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# apply some subtle changes to the selected theme via custom CSS file
def setup(app):
    app.add_stylesheet("css/custom.css")
