from PyQt5.QWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit
import sys



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Example')

        self.btn = QPushButton('Вычислить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 150)
        self.btn.clicked.connect(self.count)

        self.scr_label = QLabel(self)
        self.src_label.setText("Выражение:")
        self.src_label.move(40, 30)

        self.res_label = QLabel(self)
        self.res_label.setText("Введите имя: ")
        self.res_label.move(150, 30)

        self.src_input = QLineEdit(self)
        self.src_input.move(40, 60)
        
        self.res_input = QLineEdit(self)
        self.res_input.move(150, 60)
        
    def count(self):
        self.res_input.displayText(str(eval(self.src_input.text())))
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
        
