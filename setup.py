from setuptools import setup

from src import __version__

setup(
    version=__version__,
    name='py-moodle-quiz-parser',
    description='PIP package for parsing moodle quiz HTML documents',
    url='https://github.com/Kononenko-Daniil/py-moodle-quiz-parser',
    author='Daniil Kononenko',
    packages=['py-moodle-quiz-parser'],
    install_requires=[
        'beautifulsoup4'
    ]
)
