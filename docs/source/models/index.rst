Models
======

``Models`` is an internal MoodleQuizParser package, in which there are models of different question types (check, matching, etc).

Usage
-----
In order to use answer types you should simply import MoodleQuizParser.Models.

.. code-block:: python

    from MoodleQuizParser.Models import *

Global Models
-------------
Here are description of two simple modules, main purpose of which is storing data

Question.py
~~~~~~~~~~~~~~~~

``class Question(text, max_grade, grade, answer)``
    Class for storing question info.

    **text: str** - question text.
    **max_grade: float** - maximum grade for this question.
    **grade: float** - current grade for this question.
    **answer: Answer** - Answer for this question. For more info see next section.

    ``to_dict()`` - returns dictionary version of question, for example:

    .. code-block::

        {
            "question": "<Question text>",
            "max_grade": <Max grade>,
            "grade": <Grade>,
            "answer": (Dictionary version of answer)
        }

Answer.py
~~~~~~~~~~~~~~

``class Answer(type, content)``
    Class for storing answer data.

    **type: AnswerType** - answer type. For more info see *class AnswerType*.
    **content** - answer content. Depends on question type. For more info see *Answer types* section.

    ``to_dict()`` - returns dictionary version of answer, for example:

    .. code-block::

        {
            "type": "<AnswerType>",
            "content": (Dictionary version of answer content)
        }

``class AnswerType``
    This is an *enum* class.
    Available types: ``CHECK``, ``TEXT``, ``MATCHING``

Answer types
------------

Every answer type class has two main methods:

``parse_answer(html)``
    Used for parsing HTML block, which contains data of corresponding answer type.

``to_dict()``
    Returns dictionary version of parsed HTML data.

Detailed info about dictionary version of each answer type you can find in corresponding sections:

.. toctree::

    choice-answer
    matching-answer
    text-answer
