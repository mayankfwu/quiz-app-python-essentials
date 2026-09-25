"""
This module manages the collection of quiz questions i.e, storing, retrieving, editing, removing and providing filtered subsets (by topics or difficulty) which will be used by the quiz engine.
"""

import random

class Question:

    def __init__(self, text, options, correct_answer, topic, difficulty):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self.topic = topic
        self.difficulty = difficulty


"""checks if the answer chosen is correct or not"""
def is_correct(self, option_chosen):
    return option_chosen.lower() == self.correct_answer.lower()


"""dictionary"""
def to_dict(self, text, option_chosen, correct_answer, topic, difficulty):
    return {
        'text': self.text,
        'options': self.options,
        'correct_answer': self.correct_answer,
        'topic': self.topic,
        'difficulty': self.difficulty
    }


class QuestionBank:
    def __init__(self):
        self.questions = {}
        self.question_count = 0

    def add_question(self, question_id):
        self.question_count += 1
        self.questions[f"q{self.question_count}"] = question_id
        return question_id

    def delete_question(self, question_id):
        if question_id in self.questions:
            del self.questions[question_id]
        else:
            print("Question not found")

    def edit_question(self, question_id, new_question):
        if question_id in self.questions:
            self.questions[question_id] = new_question
        else:
            print("Question not found")

    def filter_by_topic(self, topic):
        matches=[]
        for question_id, question in self.questions.items():
            if question.topic == topic:
                matches.append(question)
        return matches

    def filter_by_difficulty(self, difficulty):
        matches = []
        for question_id, question in self.questions.items():
            if question.difficulty == difficulty:
                matches.append(question)
        return matches

    def get_random_questions(self, num_questions):
        question_list = list(self.questions.values())
        return random.sample(question_list, num_questions)
