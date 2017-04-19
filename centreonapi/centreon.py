# -*- coding: utf-8 -*-

from centreonapi.webservice import Webservice
from centreonapi.webservice.configuration.host import Host
from centreonapi.webservice.configuration.poller import Poller
from centreonapi.webservice.configuration.hostgroups import Hostgroups
from centreonapi.webservice.configuration.templates import Templates


class Centreon(object):

    def __init__(self, url=None, username=None, password=None):
        Webservice.getInstance(
            url,
            username,
            password
        )

        self.host = Host()
        self.poller = Poller()
        self.hostgroups = Hostgroups()
        self.templates = Templates()

        self.availableHost = None
        self.availableHostGroups = None
        self.availablePoller = None
        self.availableTemplates = None

    def get_available_object(self):
        try:
            self.availableHost = self.host.list()
            self.availableHostGroups = self.hostgroups.list()
            self.availablePoller = self.poller.list()
            self.availableHostTemplates = self.templates.list()
        except Exception as exc:
            raise exc

    def _exists(self, pattern, list):
        for info in list['result']:
            if info['name'] == pattern:
                return True
        return False

    def exists_host(self, name):
        if self.availableHost is None:
            self.get_available_object()
        return self._exists(name, self.availableHost)

    def exists_hostgroups(self, name):
        if self.availableHostGroups is None:
            self.get_available_object()
        return self._exists(name, self.availableHostGroups)

    def exists_poller(self, name):
        if self.availablePoller is None:
            self.get_available_object()
        return self._exists(name, self.availablePoller)

    def exists_hosttemplates(self, name):
        if self.availableHostTemplates is None:
            self.get_available_object()
        return self._exists(name, self.availableHostTemplates)

