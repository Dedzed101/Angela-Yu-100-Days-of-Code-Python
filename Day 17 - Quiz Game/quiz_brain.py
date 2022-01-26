class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.player_score = 0

    def still_has_questions(self):
        # Returns True or False depending on the situation
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        Checks for correct answer by taking two parameters, the user input and the answer (passed in from data.py)
        """

        if user_answer.lower() == correct_answer.lower():
            self.player_score += 1
            print("You got it right!")
        else:
            print("Thats's wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(
            f"Your current score is: {self.player_score}/{self.question_number}.")
        print("\n")
