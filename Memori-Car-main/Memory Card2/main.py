from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from random import *
from time import *
import json
app = QApplication([])
from main_window import *
from menu_window import *

class Question():
    right_ans = 0
    count_ans = 0
    def __init__(self, question, answer, wrong_answer1, wrong_answer2 ,wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
    def got_right(self):
        Question.right_ans +=1
        Question.count_ans +=1
    def got_wrong(self):
        Question.count_ans +=1

questions = [
Question('Яблуко', 'apple', 'application', 'pinapple', 'apply'),
Question('Дім', 'house', 'horse', 'hurry', 'hour'),
Question('Миша', 'mouse', 'mouth', 'muse', 'museum'),
Question('Число', 'number', 'digit', 'amount', 'summary')
]

radio_buttons = [rbtn1, rbtn2, rbtn3, rbtn4]
rbtn1.setStyleSheet("""
                       border: 1px orange;
                       border-radius: 4px;
                       border-style: solid;
                       padding: 4px;
                       """)
rbtn2.setStyleSheet("""
                       border: 1px orange;
                       border-radius: 4px;
                       border-style: solid;
                       padding: 4px;
                       """)
rbtn3.setStyleSheet("""
                       border: 1px orange;
                       border-radius: 4px;
                       border-style: solid;
                       padding: 4px;
                       """)
rbtn4.setStyleSheet("""
                       border: 1px orange;
                       border-radius: 4px;
                       border-style: solid;
                       padding: 4px;
                       """)



with open ("questions_list.json", "w") as file:
    data = [question.__dict__ for question in questions]
    json.dump(data, file)

def new_question():
    global cur_q
    cur_q = choice(questions)
    text_pit.setText(cur_q.question)
    lb_Correct.setText(cur_q.answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)

new_question()

def check():
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_Correct.text():
                lb_Result.setText("Вірно")
                cur_q.got_right()
                answer.setChecked(False)
                break
    else:
        cur_q.got_wrong()
        lb_Result.setText("Не вірно")

def click_ok():
    if btn_done.text() == "Відповісти":
        AnsGroupBox.show()
        RadioBoxGroup.hide()
        btn_done.setText("Наступне питання")
        check()
    else:
        btn_done.setText("Відповісти")
        AnsGroupBox.hide()
        RadioBoxGroup.show()
        new_question()

btn_done.clicked.connect(click_ok)

def menu_generation():
    if Question.count_ans == 0:
        c = 0
    else:
        c =(Question.right_ans/Question.count_ans)*100
    
    text = (f'Разів відповіли: {Question.count_ans}\n' \
           f'Вірних відповідей: {Question.right_ans}\n' \
           f'Успішність: {round(c, 2)}%')
    lb_stat_change.setText(text)
    win_card.hide()
    win_menu.show()

btn_menu.clicked.connect(menu_generation)

def back():
    win_card.show()
    win_menu.hide()

btn_back.clicked.connect(back)

def clear():
    le_question.clear()
    le_answer.clear()
    le_wrong_answer1.clear()
    le_wrong_answer2.clear()
    le_wrong_answer3.clear()

btn_clear.clicked.connect(clear)

def add_question():
    new_q = Question(le_question.text(),le_answer.text(),le_wrong_answer1.text(),le_wrong_answer2.text(),le_wrong_answer3.text())
    questions.append(new_q)
    clear()

add_new_question.clicked.connect(add_question)

def got_rest():
    n = btn_time.value() * 60
    win_card.hide()
    sleep(n)
    win_card.show()

lb_wrong_answer1.setStyleSheet("""
                        border: 1px red;
                        border-radius: 4px;
                        border-style: solid;
                        padding: 4px;""")
lb_wrong_answer2.setStyleSheet("""
                        border: 1px red;
                        border-radius: 4px;
                        border-style: solid;
                        padding: 4px;""")
lb_wrong_answer3.setStyleSheet("""
                        border: 1px red;
                        border-radius: 4px;
                        border-style: solid;
                        padding: 4px;""")
lb_answer.setStyleSheet("""
                        border: 1px green;
                        border-radius: 4px;
                        border-style: solid;
                        padding: 4px;""")



btn_back.setStyleSheet("""
                        border: 1px white;
                        border-radius: 4px;
                        border-style: solid;
                        padding: 4px;""")
btn_done.setStyleSheet("""
                        border: 1px white;
                        border-radius: 4px;
                        border-style: solid;
                        padding: 4px;""")
btn_menu.setStyleSheet("""
                       border: 1px white;
                       border-radius: 4px;
                       border-style: solid;
                       padding: 4px;
                       """)
text_pit.setStyleSheet("""
                       border: 1px orange;
                       border-radius: 4px;
                       border-style: solid;
                       padding: 4px;
                       """)
win_card.setStyleSheet("""  
                        font-family: comic sans ms, sans-serif""")



win_card.show()
app.exec()
