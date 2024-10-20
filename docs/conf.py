project = 'Image Transformer'
copyright = '2024, Nadir Kichou'
author = 'Nadir Kichou'
release = '0.4.2'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    "sphinx.ext.todo",
    'sphinx.ext.autosummary',
    "sphinx.ext.viewcode",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']