# -- Project information -----------------------------------------------------

project = "Enchanted-Book"
copyright = "2024, Enchanted Book Community"
author = "Enchanted Book"


# -- General configuration ---------------------------------------------------

extensions = [
	"_exts.treeview",
	"_exts.nbt",
	"myst_parser",
	"sphinx_design",
	"sphinx_togglebutton",
	"sphinx_copybutton",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["../_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- MyST options ------------------------------------------------------------

myst_heading_anchors = 6
myst_enable_extensions = [
	"amsmath",
	"colon_fence",
	"deflist",
	"dollarmath",
	"fieldlist",
	"html_admonition",
	"html_image",
	"linkify",
	"replacements",
	"smartquotes",
	"strikethrough",
	"substitution",
	"tasklist",
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = "pydata_sphinx_theme"
html_logo = "../_static/logo-enchanted-book.svg"
html_favicon = "../_static/logo-enchanted-book.svg"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["../_static"]
html_css_files = ["eb.css"]
html_js_files = ["eb.js"]

html_context = {
	"github_user": "Enchanted-Book",
	"github_repo": "Enchanted-Book",
	"github_version": "main",
	"doc_path": "docs",
	"languages": {
		"fr": "Français",
		"en": "English",
	}
}


# -- PyData Theme options ----------------------------------------------------

html_theme_options = {
	"navbar_start": ["navbar-logo", "language-switcher"],
	"navbar_persistent": ["search-button"],
	"navigation_with_keys": True,
	"use_edit_page_button": True,
	"header_links_before_dropdown": 4,
	"logo": {
		"text": "Enchanted Book",
	},
	"icon_links": [
		{
			"name": "GitHub",
			"url": "https://github.com/Enchanted-Book/Enchanted-Book",
			"icon": "fa-brands fa-github",
		},
	],
}
