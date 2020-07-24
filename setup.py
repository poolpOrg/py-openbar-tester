#
# Copyright (c) 2017 Gilles Chehade <gilles@poolp.org>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
"""
setup script for the openbar project
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

CONFIGURATION = {
    'description':      'py-foobar test API for the openbar framework',
    'author':           'Gilles Chehade',
    'url':              '',
    'download_url':     '',
    'author_email':     'gilles@poolp.org',
    'version':          '0.1',
    'packages':         ['openbar-tester'],
    'name':             'py-openbar-tester'
}

setup(**CONFIGURATION)
