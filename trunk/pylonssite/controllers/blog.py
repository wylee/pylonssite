from pylonssite.lib.base import *

class BlogController(BaseController):
    def index(self, url):
        redirect_to('http://blog.wyattbaldwin.com%s' % url)
