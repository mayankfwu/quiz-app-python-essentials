class scorer:
    def __init__(self,questions ,answers):
        self.questions = questions
        self.answers = answers
        self.score = 0
        self.correct_count = 0
        self.incorrect_count = 0
        self.unanswered = 0

    def score_calculator(self):
        index = 0
        for question in self.questions:
            if index not in self.answers:
                self.unanswered += 1
            elif question.correct_answer == self.answers[index]:
                self.correct_count += 1
                self.score += 1
            else:
                self.incorrect_count += 1

            index += 1

    def get_report(self):
        return self.score, self.correct_count, self.incorrect_count, self.unanswered