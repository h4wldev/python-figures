# -*- coding: utf-8 -*-
import platform

from .default import figures as default
from .windows import figures as windows



class Figures:
    _default_figures, _windows_figures = (default, windows)

    def __init__(self):
        self.platform = 'windows' if platform.system() is 'Windows' else 'default'

    def add(self, key, default, windows=None):    
        self._default_figures[key] = default

        if windows is None:
            windows = default

        self._windows_figures[key] = windows

    def get(self, key, default=None):
        if key is None:
            return None
        
        figures = self.get_all()

        return figures.get(key, default)

    def string(self, string):
        if self.platform == 'default':
            return string
        
        figures = self.get_all()

        for key in self._default_figures.keys():
            if self._default_figures[key] == figures[key]:
                continue
            
            string = string.replace(self._default_figures[key], figures[key])

        return string

    def get_all(self):
        figures = getattr(self, '_%s_figures' % self.platform)

        return figures

    def get_keys(self):
        figures = self.get_all()

        return figures.keys()


def figures(key=None, string=None, default=None):
    figures = Figures()

    if key is not None:
        return figures.get(key, default=default)

    if string is not None:
        return figures.string(string)

    return None
