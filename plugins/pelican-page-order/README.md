Page Order
==========
*Author: Ahmad Khayyat (<akhayyat@gmail.com>)*

A [Pelican][1] plugin that adds a `page_order` attribute to all pages
if one is not defined. Allows your templates to sort pages as follows:

```python
{% for p in PAGES|sort(attribute='page_order') %}
```

Without this plugin, to be able to use the line above in your
templates, you would have to define the `page_order` attribute in all
pages. This plugin sets the value of this attribute to a default value
of 100, unless a `DEFAULT_PAGE_ORDER` setting is defined.

The `page_order` attribute is cast to an `int`, so only use numeric
values. This is to have a value of `11` be greater than `2`.

[1]: http://getpelican.com/
