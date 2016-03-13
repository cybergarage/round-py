#################################################################
#
# Round for Python
#
# Copyright (C) Satoshi Konno 2016
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

import json
import urllib

from . import constants
from .method import Method

class Module:
    def __init__(self):
        self.url = ''
        self.dict = {}

    @property
    def baseurl(self):
        return self.url

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

    def is_valid(self):
        try:
            self.name
            self.version
            self.methods
        except KeyError:
            return False
        return True

    def load(self, url):
        self.url = url
        res = urllib.urlopen(url)
        if res.getcode() != 200:
            return False
        content = res.read()
        if len(content) <= 0:
            return False
        self.dict =  json.loads(content)
        return True