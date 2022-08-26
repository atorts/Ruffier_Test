from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout
from instr import*



app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle(txt_title)
main_win.move(800,100)
main_win.resize(500, 500)
b1 = QPushButton(btn1)
text1 = QLabel(txt1_txt)
text2 = QLabel(description)

main_v = QVBoxLayout()
main_v.addWidget(text1, alignment = Qt.AlignLeft)
main_v.addWidget(text2, alignment = Qt.AlignLeft)
main_v.addWidget(b1, alignment = Qt.AlignCenter)


main_win.setLayout(main_v)

main_win.show()
app.exec_()