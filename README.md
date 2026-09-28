# quiz-app-python-essentials

## Overview:- ##

This program aims to be an easy and resource efficient app to make and attempt quiz/tests. Admin will be the one using the program to add/edit/delete/view questions to the question bank which will be used to create the quiz. The student can take test by entering the no. of questions and time limit of the test, the student can also filter the questions according to topics and difficulty which would be defined by the teacher while adding question. All questions are assigned a unique id to easily access them which can be seen by view function. Once the student finishes the test or the timer runs out a report will shown which will contain score, no of questions correctly answered, no of questions incorrectly answered and the no. of questions incorrectly answered.

## Features:- ##

This program offers different functionality according to the user.

For the admin/teacher,

1. add questions to the question bank by using add_question function defined in the question_bank modules where the admin enters the question details (text, options, correct answer, topic and difficulty). Each question gets an automatic id.

2. edit a particular question from the question bank using the edit_question function defined in the question_bank module  where the admin will be first shown the question selected for editing and then prompted to again enter the details for the new question.

3. delete a question from the question bank.

4. view the question bank.

For the student.

1. take a quiz for which the follow details will be asked
	> no. of questions to be asked
	> time limit of the test
	> topics to filter the questions chosen (can be left blank to not filter by topic)
	> difficulty to filter the questions (can be left blank to not filter by difficulty)

2. the questions for the quiz will be chosen randomly

3. the answers are checked ignoring the capitalization

## Technologies and Tools used:- ##
1. the code is written in python 3.14
2. Git and Github
3. random library to choose randomised question for the quiz
4. time module to check elapsed time for the test
5. PyCharm ide used for developement

## Steps to install & run the project:- ##

### Prerequisites ###

- Python 3.10 or newer
- Git (optional, only needed to clone the repo)

No external libraries are required. The project uses only Python's standard library.

### Steps ###

1. Clone the repository:
   git clone https://github.com/mayankfwu/quiz-app-python-essentials.git

2. Move into the project folder:
   cd quiz-app-python-essentials

3. Run the application:
   python main.py

### First-time usage ###

The question bank starts empty each time the program runs, so:

1. Choose **1** (Admin) from the main menu and add some questions.
2. Choose **5** to go back to the main menu.
3. Choose **2** (Student) and then **1** to take a test.
