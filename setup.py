from setuptools import setup

long_descript = 'Utility to organize folders while participating in a CTF competition.'


setup(
    name = 'cfo',
    version = '1.0',
    author = 'jsfleming',
    author_email = 'jsfleming@pm.me'

    url = 'https://github.com/jsfleming/cfo',
    description = 'CTF Folder Organizer',
    long_description = open('README.md').read(),
    keywords = 'ctf organize',

    packages = ['cfo'],
    provides = ['cfo'],
    install_requires = ['click'],
    scripts = ['cfo/cfo'],
)
