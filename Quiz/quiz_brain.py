class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):

        curr_qt = self.question_list[self.question_number].text

        player_answer = input(f"Q{self.question_number}. {curr_qt} ")
        return player_answer

    def still_has_questions(self):

        if self.question_number < len(self.question_list):
            return True
        elif self.question_number == len(self.question_list):
            return False

    def is_correct(self, pl_answ, q_list, q_num):
        if pl_answ == q_list[q_num].answer:
            print("That's Correct!")
            self.question_number += 1
            return True
        else:
            print("Wrong answer!")
            return False
