from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os
import time


question_bank = []
n_quest = QuizBrain(question_bank)
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)
while n_quest.still_has_questions():

    if n_quest.question_number == 0:
        input('Press Enter to start..')
    elif n_quest.question_number > 0:
        input('Press Enter to continue..')
    os.system('cls')

    pl_ans = n_quest.next_question()
    n_quest.is_correct(pl_ans, n_quest.question_list, n_quest.question_number)
    time.sleep(0.25)

input('Press Enter to quit..')
