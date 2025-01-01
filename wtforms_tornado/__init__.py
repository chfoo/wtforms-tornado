# -*- coding: utf-8 -*-
"""WTForms extensions for Tornado."""
version_tuple = (0, 0, 3)


def get_version_string():
    if isinstance(version_tuple[-1], str):
        return '.'.join(map(str, version_tuple[:-1])) + version_tuple[-1]
    else:
        return '.'.join(map(str, version_tuple))

version = get_version_string()
"""Current version of wtforms-tornado."""

__author__ = 'Jorge Puente Sarrín <puentesarrin@gmail.com>'
__since__ = '2013-09-25'
__version__ = version


from wtforms_tornado.form import Form
