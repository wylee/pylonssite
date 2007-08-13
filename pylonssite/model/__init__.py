from paste.deploy import appconfig

from elixir import metadata, options_defaults, Entity
from elixir import has_field, has_many, belongs_to, using_options
from elixir import String, Integer


options_defaults['shortnames'] = True


class Site(Entity):
    """A `Site` contains `Directory`s."""
    has_field('title', String)
    has_field('slug', String)
    has_field('domain', String)
    has_field('logo_text', String)
    has_field('tagline', String)
    has_field('sidebar', String)
    has_field('copyright', String)
    has_many('directories', of_kind='Directory')

    def __str__(self):
        return '%s: %s' % (self.__class__.__name__, self.title)


class Directory(Entity):
    """A `Directory` belongs to a `Site` and contains `Page`s."""
    has_field('title', String)
    has_field('slug', String)
    has_field('order', Integer)
    belongs_to('site', of_kind='Site')
    has_many('pages', of_kind='Page')

    def __str__(self):
        return '%s: %s' % (self.__class__.__name__, self.title)


class Page(Entity):
    """A `Page` belongs to a `Directory`."""
    has_field('title', String)
    has_field('slug', String)
    has_field('order', Integer)
    has_field('content', String)
    has_field('sidebar', String)
    belongs_to('directory', of_kind='Directory')

    def __str__(self):
        return '%s: %s' % (self.__class__.__name__, self.title)

    def excerpt(self):
        default_limit = 100
        len_content = len(self.content)
        if len_content < default_limit:
            limit = len_content
        else:
            limit = default_limit
        return self.content[:limit]
