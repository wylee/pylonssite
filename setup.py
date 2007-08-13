try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='PylonsSite',
    version='0.2a0',
    description='Simple Pylons CMS',
    author='Wyatt Baldwin',
    author_email='self@wyattbaldwin.com',
    url='http://wyattbaldwin.com/',
    install_requires=[
	'Pylons>=0.9.6rc2',
	'Elixir==0.3.0',
	'SQLAlchemy==0.3.8',
    ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'pylonssite': ['i18n/*/LC_MESSAGES/*.mo']},
    zip_safe=False,
    entry_points="""
    [paste.app_factory]
    main = pylonssite.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
