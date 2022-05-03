class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score=0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number+1}: {current_question.text} (True/False)")
        self.check_answer(answer, current_question.answer)

    def still_has_questions(self):
        if self.question_number < len(self.question_list)-1:
            self.question_number += 1
            return True
        else:
            return False

    def check_answer(self,answer,c_answer):
        if answer.lower() == c_answer.lower() :
            print("You got it right")
            self.score += 1
        else:
            print("That is wrong")
        print(f"The correct answer is {c_answer}")
        print(f"Your current score is: {self.score}/{self.question_number+1}.")
