from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit
import PyQt5
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Example')

        self.btn = QPushButton('Вычислить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 150)
        self.btn.clicked.connect(self.count)

        self.src_label = QLabel(self)
        self.src_label.setText("Выражение:")
        self.src_label.move(40, 30)

        self.res_label = QLabel(self)
        self.res_label.setText("Результат: ")
        self.res_label.move(200, 30)

        self.src_input = QLineEdit(self)
        self.src_input.move(40, 60)

        self.res_input = QLineEdit(self)
        self.res_input.move(200, 60)

    def count(self):
        self.res_input.setText(str(eval(self.src_input.text())))
        self.src_input.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
