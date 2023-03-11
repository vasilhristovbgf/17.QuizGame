class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):

        curr_qt = self.question_list[self.question_number].text

        player_answer = input(f"Q{self.question_number + 1}. {curr_qt} ")
        return player_answer

    def still_has_questions(self):

        if self.question_number < len(self.question_list):
            print(f'Current Score: {self.score}/{self.question_number}')
            return True
        elif self.question_number == len(self.question_list):
            print(f'Final Score: {self.score}/{self.question_number}')
            return False

    def is_correct(self, pl_answ, q_list, q_num):
        if pl_answ == q_list[q_num].answer:
            self.score += 1
            print('That`s Correct!')
            self.question_number += 1
        else:
            print('Wrong answer!')
            self.question_number += 1
        return True
