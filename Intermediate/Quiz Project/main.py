from check import check
from questionformat import questionformat
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = questionformat(question_text, question_answer)
    question_bank.append(new_question)

quiz = check(question_bank)

while quiz.still_has_questons_left():
    quiz.next_question()

print("Thanks for completing")