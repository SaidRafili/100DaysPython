class check:
    def __init__(self,question_list):
        self.question_position = 0
        self.question_list = question_list
        self.score =  0

    def still_has_questons_left(self):
        return self.question_position < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Question: {self.question_number}. {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self,user_anwer, correct_answer):
        if user_anwer.lower() == correct_answer.lower():
            print("You answered right")
            self.score += 1
        else:
            print("The answer is incorrect")
