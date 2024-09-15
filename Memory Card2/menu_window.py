from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

win_menu = QWidget()

lb_question = QLabel("Введіть запитання:")
lb_answer = QLabel("Введіть правильну відповідь:")
lb_wrong_answer1 = QLabel("Введіть першу хибну відповідь:")
lb_wrong_answer2 = QLabel("Введіть другу хибну відповідь:")
lb_wrong_answer3 = QLabel("Введіть третю хибну відповідь:")

le_question = QLineEdit()
le_answer = QLineEdit()
le_wrong_answer1 = QLineEdit()
le_wrong_answer2 = QLineEdit()
le_wrong_answer3 = QLineEdit()

line1 = QVBoxLayout()
line1.addWidget(lb_question)
line1.addWidget(lb_answer)
line1.addWidget(lb_wrong_answer1)
line1.addWidget(lb_wrong_answer2)
line1.addWidget(lb_wrong_answer3)

line2 = QVBoxLayout()
line2.addWidget(le_question)
line2.addWidget(le_answer)
line2.addWidget(le_wrong_answer1)
line2.addWidget(le_wrong_answer2)
line2.addWidget(le_wrong_answer3)

line = QHBoxLayout()
line.addLayout(line1)
line.addLayout(line2)

button_line = QHBoxLayout()
add_new_question = QPushButton("Додати запитання")
btn_clear = QPushButton("Очистити")

button_line.addWidget(add_new_question)
button_line.addWidget(btn_clear)

lb_stat = QLabel("Статистика")
lb_stat_change = QLabel("")

btn_back = QPushButton("Назад")

main_line = QVBoxLayout()
main_line.addLayout(line)
main_line.addLayout(button_line)
main_line.addWidget(lb_stat)
main_line.addWidget(lb_stat_change)
main_line.addWidget(btn_back)


win_menu.setLayout(main_line)
