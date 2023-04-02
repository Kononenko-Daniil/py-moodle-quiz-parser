QuizParser.py
=============

Here is detailed description of content of QuizParser.py module.

Usage
-----
In order to use answer types you should simply import MoodleQuizParser.QuizParser.

.. code-block:: python

    from MoodleQuizParser.QuizParser import *

Contents
--------

``class QuizParser()``
    This is the main class of **py-moodle-quiz-parser** package. It includes two main methods:

    ``parse_html(html_text, parse_type, as_dict)``
        It is used for parsing HTML into array of *Questions*
        **html_text** - content of HTML document (not file).
        **parse_type** - if set to *"all"*, will return all question content, including *max_grade*, *grade* and *answer*. In any other case only the "text" field will be filled.
        **as_dict** - if set to *True*, will return dictionary version. If set to *False*, will return array of *Questions*.

    ``to_dict(questions)``
        Returns dictionary version of array of *Questions*.
        **questions** - array of *Questions*.