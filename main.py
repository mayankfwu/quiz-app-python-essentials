"""
this is the entry point of the application
"""
from question_bank import QuestionBank, Question
from quiz_engine import Quiz
from scorer import Scorer
import random


def run_quiz(quiz):
    while not quiz.end_quiz():
        current_question = quiz.get_current_question()
        print(current_question.text)
        print(current_question.options)
        option_chosen = input("enter option chosen:")
        quiz.record_answer(option_chosen)
        quiz.go_to_question(quiz.current_index + 1)

def report(scorer):
    score, correct_count, incorrect_count, unanswered = scorer.get_report()
    print(f"score: {score}"
          f"correct_count: {correct_count}"
          f"incorrect_count: {incorrect_count}"
          f"unanswered: {unanswered}")


def admin_menu(question_bank):
    while True:
        admin_choice = int(input("press 1 to add questions\n"
                                 "press 2 to edit questions\n"
                                 "press 3 to delete questions\n"
                                 "press 4 to view questions\n"
                                 "press 5 to quit\n"
                                 "please choose an option\n"))



        if admin_choice == 1:
    #takes in the inputs of new question
            text = input("enter the text of question here:")
            option1 = input("enter option1 here:")
            option2 = input("enter option2 here:")
            option3 = input("enter option3 here:")
            option4 = input("enter option4 here:")
            options = [option1,option2,option3,option4]
            correct_answer = input("enter the correct answer here:")
            topic = input("enter topic here:")

            while True:
                difficulty = input("enter difficulty here(easy, medium, hard):")

                if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
                    break
                else:
                    print("please choose a valid difficulty option")

            new_question = Question(text, options, correct_answer, topic, difficulty)

            question_bank.add_question(new_question)




        elif admin_choice == 2:

    #takes the ques id to edit as input cnd checks the inputs validity
            while True:
                question_id_to_edit = input("enter question id you want to edit here (format must be q1, q2, etc.):")

                if question_id_to_edit not in question_bank.questions:
                    print("please choose a valid question id")

                else:
                    break

    #displays the selected question
            print("For the new question please enter the following data...")
            current_question = question_bank.get_question(question_id_to_edit)
            print(f"Current text: {current_question.text}")
            print(f"Current options: {current_question.options}")
            print(f"Current correct answer: {current_question.correct_answer}")
            print(f"Current topic: {current_question.topic}")
            print(f"Current difficulty: {current_question.difficulty}")

    #takes the input for new question
            text = input("enter the text of question here:")
            option1 = input("enter option1 here:")
            option2 = input("enter option2 here:")
            option3 = input("enter option3 here:")
            option4 = input("enter option4 here:")
            options = [option1, option2, option3, option4]
            correct_answer = input("enter the correct answer here:")
            topic = input("enter topic here:")

            while True:
                difficulty = input("enter difficulty here(easy, medium, hard):")

                if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
                    break
                else:
                    print("please choose a valid difficulty option")

            edited_question = Question(text, options, correct_answer, topic, difficulty)
            question_bank.edit_question(question_id_to_edit, edited_question)

        elif admin_choice == 3:
    #takes question id
            while True:
                question_id_to_delete = input("enter question id you want to delete here (format must be q1, q2, etc.):")

                if question_id_to_delete not in question_bank.questions:
                    print("please choose a valid question id")

                else:
                    break

            question_bank.delete_question(question_id_to_delete)


        elif admin_choice == 4:
            for question_id, question in question_bank.questions.items():
                print(f"{question_id}: {question.text}\n"
                      f"options: {question.options}\n"
                      f"correct answer: {question.correct_answer}\n"
                      f"topic: {question.topic}\n"
                      f"difficulty: {question.difficulty}\n")

    #ends this branch and returns to main menu
        elif admin_choice == 5:
            print("returning to main menu")
            break


def student_menu(question_bank):
    while True:
        student_choice = int(input("What would you like to do?\n"
                                   "press 1 to take a test\n"
                                   "press 2 to go back to main menu\n"))
        if student_choice == 1:
            quiz_topic = input("enter topic here (leave blank not filter by topic):")
            quiz_difficulty = input("enter difficulty here (leave blank not filter by difficulty):")

            matching_questions = []
            for question_id, question in question_bank.questions.items():
                if quiz_topic != "" and question.topic != quiz_topic:
                    continue
                if quiz_difficulty != "" and question.difficulty != quiz_difficulty:
                    continue
                matching_questions.append(question)

            while True:
                quiz_no_of_questions = int(input(f"enter the no. of questions you want to attempt (no. of remaining questions = {len(matching_questions)}):"))
                if quiz_no_of_questions > len(matching_questions):
                    print("invalid (not enough questions)")

                else:
                    break

            selected_questions = random.sample(matching_questions, quiz_no_of_questions)

            time_limit = int(input("enter time limit in minutes here:"))

            new_quiz = Quiz(selected_questions, time_limit)
            run_quiz(new_quiz)

            new_scorer = Scorer(new_quiz.questions, new_quiz.answers)
            new_scorer.score_calculator()
            report(new_scorer)


        elif student_choice == 2:
            print("returning")
            break

        else:
            print("please choose a valid option")


#main menu
def main_menu(question_bank):
    while True:
        menu_choice = int(input("What would you like to do?\n"
              "press 1 to get admin options\n"
              "press 2 to get student options\n"
              "press 3 to quit\n"
               "enter your choice:"))

        if menu_choice == 1:
            admin_menu(question_bank)

        elif menu_choice == 2:
            student_menu(question_bank)

        elif menu_choice == 3:
            print("goodbye\n"
                  "shutting down...")
            break

        else:
            print("please choose a valid option")


if __name__ == "__main__":
    question_bank = QuestionBank()
    main_menu(question_bank)






