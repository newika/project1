from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

#создание объекта приложения
app = QApplication([])
#создание объекта окно
main_win = QWidget()
#сделать окно видимым
main_win.show()
#название окна
main_win.setWindowTitle('Моё первое приложение')
#расположение окна на экране
main_win.move(900, 700)
#изменение размеров экрана
main_win.resize(400, 200)
#создание объекта надпись
text1 = QLabel('Hello, world!')
v_line = QVBoxLayout()
v_line.addWidget(text1, alignment = Qt.AlignCenter)
main_win.setLayout(v_line)
#оставлять приложение открытым
app.exec_()