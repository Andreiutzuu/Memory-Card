from PyQt5.QtCore import Qt  
from random import shuffle
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QVBoxLayout,QHBoxLayout,QGroupBox,QButtonGroup,QRadioButton,QPushButton
class Question():
    def __init__(self, question, answer,
    wrong1,wrong2,wrong3):
        self.question=question
        self.answer=answer 
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3
    
questions_list=[]
questions_list.append(
    Question("The state of Portugal", "Portugesse","English","French","Spanish"))
questions_list.append(
    Question("The state of England", "English","Italiano","French","Spanish"))
questions_list.append(
    Question("The state of Spain", "Spanish","Portugesse","French","English"))
questions_list.append(
    Question("The state of France", "French","Portugesse","Spanish","English"))
    
    
    



def show_result():
    radiogroupbox.hide()
    ansgroupbox.show()
    answerbtn.setText("Urmatoarea intrebare")

def show_question():
    radiogroupbox.show()
    ansgroupbox.hide()
    answerbtn.setText("Raspuns")

    radiogroup.setExclusive(False)
    radiobtn1.setChecked(False)
    radiobtn2.setChecked(False)
    radiobtn3.setChecked(False)
    radiobtn4.setChecked(False)
    radiogroup.setExclusive(True)
def start_test():
    if answerbtn.text()=="Raspuns":
        show_result()
    else:
        show_question()
def next_question():
    window.cur_question+= 1
    if window.cur_question>=len(questions_list):
        window.cur_question=0
    q=questions_list[window.cur_question]
    ask(q)

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_corect.setText(q.answer)
    show_question()
def show_corect(res):
    lb_corect.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_corect("corect")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked() :
            show_corect("incorect")
def click_ok():
    if answerbtn.text()=="Raspuns":
        check_answer()
    else:
        next_question()

app=QApplication([])
window=QWidget()
window.setWindowTitle("Memo Card")
window.cur_question= -1 
radiogroup=QButtonGroup()
question=QLabel("Aici o sa fie intebare")
answerbtn=QPushButton("Raspuns")
answerbtn.clicked.connect(click_ok)
radiobtn1=QRadioButton("Optiunea 1")
radiobtn2=QRadioButton("Optiunea 2")
radiobtn3=QRadioButton("Optiunea 3")
radiobtn4=QRadioButton("Optiunea 4")
radiogroup.addButton(radiobtn1)
radiogroup.addButton(radiobtn2)
radiogroup.addButton(radiobtn3)
radiogroup.addButton(radiobtn4)
layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()

layout_ans2.addWidget(radiobtn1)
layout_ans2.addWidget(radiobtn2)
layout_ans3.addWidget(radiobtn3)
layout_ans3.addWidget(radiobtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

radiogroupbox=QGroupBox("Variante raspuns")
radiogroupbox.setLayout(layout_ans1)
radiogroupbox.show()

ansgroupbox=QGroupBox("Rezulat")
lb_result=QLabel("Ai raspuns corect?")
lb_corect=QLabel("Aici o sa fie raspunsul")

layout_res=QVBoxLayout()

layout_res.addWidget(lb_result,alignment=Qt.AlignTop)
layout_res.addWidget(lb_corect,alignment=Qt.AlignHCenter,stretch=3)
ansgroupbox.setLayout(layout_res)
ansgroupbox.hide()


mainlayout=QVBoxLayout()
mainlayout.setSpacing(5)
mainlayout.addWidget(question,alignment=Qt.AlignCenter)
mainlayout.addWidget(radiogroupbox,alignment=Qt.AlignCenter)
mainlayout.addWidget(ansgroupbox,alignment=Qt.AlignCenter)
mainlayout.addWidget(answerbtn,alignment=Qt.AlignCenter)
answers=[radiobtn1,radiobtn2,radiobtn3,radiobtn4]

window.setLayout(mainlayout)







window.show()
app.exec()

                    