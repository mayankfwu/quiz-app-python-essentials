import time


class Quiz:
    def __init__(self, questions, time_limit):
        self.questions = questions
        self.time_limit = time_limit
        self.current_index = 0
        self.answers = {}
        self.start_time = time.time()

    def get_current_question(self):
        return self.questions[self.current_index]

    def go_to_question(self, question_number):
        if question_number in range(0, len(self.questions)):
            self.current_index = question_number
        else:
            print("Invalid question number")

    def record_answer(self, option_chosen):
        self.answers[self.current_index] = option_chosen

    def timer(self):
        elapsed_seconds = time.time() - self.start_time
        return elapsed_seconds >= self.time_limit*60

    def end_quiz(self):
        return self.timer() or len(self.answers) == len(self.questions)


