"""
Page Order
==========

Adds a `page_order` attribute to all pages if one is not defined.
"""

from pelican import signals

def set_page_order(generator):
    for page in generator.pages:
        if hasattr(page, 'page_order'):
            page.page_order = int(page.page_order)
        elif 'DEFAULT_PAGE_ORDER' in generator.settings:
            page.page_order = int(generator.settings['DEFAULT_PAGE_ORDER'])
        else:
            page.page_order = 100

def register():
    signals.page_generator_finalized.connect(set_page_order)
