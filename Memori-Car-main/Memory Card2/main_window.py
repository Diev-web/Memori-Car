from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
w,h = 600,500
win_card = QWidget()
win_card.resize(w,h)
win_card.setWindowTitle("Memory Card")
win_card.move(650,300)


#Buttons 1
btn_menu = QPushButton("Меню")
btn_rest = QPushButton("Відпочити")
btn_time = QSpinBox()
btn_time.setValue(30)
text_line1 = QLabel("хвилин")


#Lines
main_line = QVBoxLayout()
Header1 = QHBoxLayout()
Header2 = QHBoxLayout()
Header3 = QHBoxLayout()
Header4 = QHBoxLayout()
#Connect line
Header1.addWidget(btn_menu)
Header1.addStretch(3)
Header1.addWidget(btn_rest)
Header1.addWidget(btn_time)
Header1.addWidget(text_line1)
#Header2
text_pit = QLabel("Яблуко")
Header2.addWidget(text_pit, alignment= Qt.AlignmentFlag.AlignCenter)
#Header3
RadioBoxGroup = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()
rbtn1 =QRadioButton("Варіант 1")
rbtn2 =QRadioButton("Варіант 2")
rbtn3 =QRadioButton("Варіант 3")
rbtn4 =QRadioButton("Варіант 4")


RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

btn_line = QVBoxLayout()
btn_line1 = QHBoxLayout()
btn_line2 = QHBoxLayout()

btn_line1.addWidget(rbtn1)
btn_line1.addWidget(rbtn2)
btn_line2.addWidget(rbtn3)
btn_line2.addWidget(rbtn4)

btn_line.addLayout(btn_line1)
btn_line.addLayout(btn_line2)
RadioBoxGroup.setLayout(btn_line)

#Header4
btn_done = QPushButton("Відповісти")

#Next Done
AnsGroupBox = QGroupBox("Результат")
lb_Correct = QLabel("Правильно")
lb_Result = QLabel("Результат")

line_res = QVBoxLayout()
line_res.addWidget(lb_Result)
line_res.addWidget(lb_Correct)
AnsGroupBox.setLayout(line_res)
AnsGroupBox.hide()

Header3.addWidget(RadioBoxGroup)
Header3.addWidget(AnsGroupBox)
Header4.addWidget(btn_done)



win_card.setLayout(main_line)
main_line.addLayout(Header1)
main_line.addLayout(Header2)
main_line.addLayout(Header3, stretch=3)
main_line.addLayout(Header4)




