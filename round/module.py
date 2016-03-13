#################################################################
#
# Round for Python
#
# Copyright (C) Satoshi Konno 2016
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

import os
import json
import urllib

from . import constants
from .method import Method

class Module:
    def __init__(self):
        self.url = ''
        self.path = ''
        self.dict = {}

    @property
    def baseurl(self):
        return self.url

    @property
    def basepath(self):
        return os.path.dirname(self.path)

    @property
    def name(self):
        return self.dict[constants.MODULE_PARAM_NAME]

    @property
    def version(self):
        return self.dict[constants.MODULE_PARAM_VERSION]

    @property
    def methods(self):
        methods = []
        for dict in self.dict[constants.MODULE_PARAM_METHODS]:
            method = Method()
            method.dict = dict
            methods.append(method)
        return methods

    def is_url(self):
        if not 0 < len(self.url):
            return False
        return True

    def is_file(self):
        if not 0 < len(self.path):
            return False
        return True

    def is_valid(self):
        try:
            self.name
            self.version
            self.methods
        except KeyError:
            return False
        return True

    def load_url(self, url):
        res = urllib.urlopen(url)
        if res.getcode() != 200:
            return False
        content = res.read()
        if len(content) <= 0:
            return False
        self.dict =  json.loads(content)
        self.url = url
        return True

    def load_file(self, file):
        with open(file, 'r') as fd:
            content = fd.read()
            if len(content) <= 0:
                return False
            self.dict =  json.loads(content)
        self.path = file
        return True