class scorer:
    #TODO: attribute - score(int, starts at 0)
    #TODO: attribute - correct_count(int, starts at 0)
    #TODO: attribute - something to hold the ques+correct answers data
    #TODO: attribute - something to hold the user chosen answers
    #TODO: attribute - incorrect_count(int, starts at 0)
    #TODO: attribute - unanswered(int, starts at 0)

    #TODO: method - __init__ - takes in two data sources above, sets score/correct_count, incorrect_count and unanswered to 0
    #TODO: method - score_calculator - loops through every question, compared the chosen answer vs correct answer, increments score/correct_count when they match, increment incorrect_count when they dont match and the option is not empty and increment unanswered when the option is empty
    #TODO: method - get_report() - return correct_count, incorrect_count, unanswered
