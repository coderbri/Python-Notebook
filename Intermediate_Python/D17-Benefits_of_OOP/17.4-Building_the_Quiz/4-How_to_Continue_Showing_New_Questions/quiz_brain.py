# ✓ TODO 6: Create a class called QuizBrain.
class QuizBrain:

    # ✓ TODO 7: Write an __init__() method.
    def __init__(self, q_list):
        # ✓ TODO 8: Initialize the question_number to 0.
        self.question_number = 0
        # ✓ TODO 9: Initialize the question_list to an input.
        self.questions_list = q_list

    # ✓ TODO 12: Create a method called still_has_questions().
    #  Return a boolean depending on teh value of question_number.
    #  Use the while loop to show the next question until the end.
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)  # Also means True
        # ^ Above is a simplified version of this boolean statement
        # if self.question_number < len(self.questions_list):
        #     return True
        # else:
        #     return False

    # ✓ TODO 10: Ask the question. Retrieve the item at the current question_number from
    #  the question_list. Use the input() func to show the user the Question "text"
    #  and ask for the user's "answer".
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")


# TODO 13: Checking if the answer was correct.
