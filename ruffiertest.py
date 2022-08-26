from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Здоровье')
main_win.move(800,100)
main_win.resize(500, 500)
b1 = QPushButton('Начать')
text1 = QLabel('Добро пожаловатьв программу по определению состояния здоровья!')
text2 = QLabel('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                   'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                   'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                   'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                   'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                   'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
                   'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                   'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.')

main_v = QVBoxLayout()
main_v.addWidget(text1, alignment = Qt.AlignLeft)
main_v.addWidget(text2, alignment = Qt.AlignLeft)
main_v.addWidget(b1, alignment = Qt.AlignCenter)


main_win.setLayout(main_v)

main_win.show()
app.exec_()
