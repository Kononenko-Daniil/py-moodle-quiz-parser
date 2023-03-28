from setuptools import setup

from MoodleQuizParser import __version__

setup(
    version=__version__,
    name='py-moodle-quiz-parser',
    description='PIP package for parsing moodle quiz HTML documents',
    url='https://github.com/Kononenko-Daniil/py-moodle-quiz-parser',
    author='Daniil Kononenko',
    py_modules=['MoodleQuizParser'],
    install_requires=[
        'beautifulsoup4'
    ]
)
