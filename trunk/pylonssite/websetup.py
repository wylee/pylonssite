"""Setup the PylonsSite application"""
import logging

from paste.deploy import appconfig
from pylons import config

from pylonssite.config.environment import load_environment

import sqlalchemy
import pylonssite.model as model

log = logging.getLogger(__name__)

def setup_config(command, filename, section, vars):
    """Place any commands to setup pylonssite here"""
    conf = appconfig('config:' + filename)
    load_environment(conf.global_conf, conf.local_conf)
    engine = sqlalchemy.create_engine(conf['sqlalchemy.dburi'])
    engine.echo = True
    model.metadata.connect(engine)
    drop_all_tables()
    create_all_tables()

def drop_all_tables():
    really_drop = raw_input('Really drop all tables?! [yes/N] ')
    if really_drop.lower().strip() == 'yes':
        print 'Dropping all tables...'
        model.metadata.drop_all()
    else:
        print 'Tables not dropped'

def create_all_tables():
    print 'Creating all tables...'
    model.metadata.create_all()
    print 'Done creating all tables.'
