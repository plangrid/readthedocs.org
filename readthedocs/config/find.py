"""Helper functions to search files."""

from __future__ import division, print_function, unicode_literals

import os


def find_all(path, filenames):
    """Find all files in ``path`` that match in ``filenames``."""
    path = os.path.abspath(path)
    try:
        for root, dirs, files in os.walk(path, topdown=True):
            dirs.sort()
            for filename in filenames:
                if filename in files:
                    yield os.path.abspath(os.path.join(root, filename))
    except UnicodeDecodeError:
        # This is an error of not being able to walk the dir when there are unicode files in them :|
        pass


def find_one(path, filenames):
    """Find the first file in ``path`` that match in ``filenames``."""
    for _path in find_all(path, filenames):
        return _path
    return ''
