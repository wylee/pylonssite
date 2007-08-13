"""Routes configuration

The more specific and detailed routes should be defined first so they may take
precedent over the more generic routes. For more information refer to the
routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    m = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])

    # The ErrorController route (handles 404/500 error pages); it should likely
    # stay at the top, ensuring it can always be resolved
    m.connect('error/:action/:id', controller='error')

    # CUSTOM ROUTES HERE
    
    m.connect('blog*url', controller='blog')

    m.resource('site', 'sites')
    m.resource('directory', 'directories',
               parent_resource={'member_name': 'site',
                                'collection_name': 'sites'})

    dir_res = {
        'member_name': 'directory',
        'collection_name': 'directories',
        'parent_member_name': 'site',
    }

    m.resource('page', 'pages', parent_resource=dir_res)

    kwargs = dict(controller='pages', action='show',
                  directory_id='root', id='home',
                  _member_name='page', _collection_name='pages', 
                  _parent_resource=dir_res)
    m.connect(':id', **kwargs)
    m.connect(':directory_id/:id', **kwargs)

    # END CUSTOM ROUTES HERE

    #m.connect(':controller/:action/:id')
    #m.connect('*url', controller='template', action='view')

    return m
