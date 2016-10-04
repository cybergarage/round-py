#################################################################
#
# Round for Python
#
# Copyright (C) Satoshi Konno 2016
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

from __future__ import absolute_import

import json
import urllib
import urlparse

from . import constants

class Method:
    def __init__(self):
        self.dict = {}

    @property
    def name(self):
        return self.dict[constants.MODULE_PARAM_NAME]

    @property
    def language(self):
        return self.dict[constants.MODULE_PARAM_LANGUAGE]

    @property
    def file(self):
        return self.dict[constants.MODULE_PARAM_FILE]

    @property
    def code(self):
        return self.dict[constants.MODULE_PARAM_CODE]

    def is_valid(self):
        try:
            self.name
            self.language
            self.file
            self.code
        except KeyError:
            return False
        return True

    def load_url(self, baseurl = ''):
        url = self.file
        if 0 < len(baseurl):
            url = urlparse.urljoin(baseurl, url)

        res = urllib.urlopen(url)
        if res.getcode() != 200:
            return False
        code = res.read()
        if len(code) <= 0:
            return False
        self.dict[constants.MODULE_PARAM_CODE] = code

        return True

    def load_file(self, basepath = ''):
        path = self.file
        if 0 < len(basepath):
            path = '%s/%s' % (basepath, path)

        with open(path, 'r') as fd:
            code = fd.read()
            if len(code) <= 0:
                return False
            self.dict[constants.MODULE_PARAM_CODE] = code

        return True