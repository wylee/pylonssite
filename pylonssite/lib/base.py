"""The base Controller API

This module provides the BaseController for all controllers to subclass, as
well as functions and objects for use by those controllers.
"""
from pylons import c, cache, config, g, request, response, session
from pylons.controllers import WSGIController
from pylons.decorators import jsonify, validate
from pylons.helpers import abort, etag_cache, redirect_to
from pylons.i18n import _, ungettext, N_
from pylons.templating import render

import pylonssite.lib.helpers as h
import pylonssite.model as model

import restler


class RestController(restler.BaseController(model)):
    def __call__(self, environ, start_response):
        return super(RestController, self).__call__(environ, start_response)

    def abort_all(self):
        abort(403)
    #edit = delete = new = abort_all


class BaseController(WSGIController):
    pass


# Include the '_' function in the public names
__all__ = [__name for __name in locals().keys() if not __name.startswith('_')
           or __name == '_']
