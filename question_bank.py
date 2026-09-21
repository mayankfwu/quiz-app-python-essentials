"""
This module manages the collection of quiz questions i.e, storing, retrieving, editing, removing and providing filtered subsets (by topics or difficulty) which will be used by the quiz engine.
"""

class Question:
    # TODO: attribute - the question text (str)
    # TODO: attribute - list of options (list of string)
    # TODO: attribute - the correct answer (str or index into options)
    # TODO: attribute - topic/category (str)
    # TODO: attribute - difficulty level (str or int)

    # TODO: method - __init__ to set all the above when a question is created
    # TODO: method - a way to check if given ans is correct
    # TODO: method - a way to represent the question as a dict (for saving to json)

class QuestionBank:
    # TODO: attribute - the collection of question objects (dict keyed by a unique ques id)

    # TODO: method - __init__ (sets an empty dict to hold questions)
    # TODO: method - add question (add_question)
    # TODO: method - delete question (ques id)
    # TODO: method - filter by topic (topic)
    # TODO: method - edit question (ques id)
    # TODO: method - filter by difficulty (difficulty)
    # TODO: method - get random question (count of question/ num_questions)
    # TODO: method - load from file
    # TODO: method - save to file


