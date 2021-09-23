from PyQt5.QWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit, QListWidget
import sys



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Example')

        self.btn = QPushButton('Добавить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(400, 60)
        self.btn.clicked.connect(self.add)

        self.name_label = QLabel(self)
        self.name_label.setText("Имя:")
        self.name_label.move(40, 30)

        self.number_label = QLabel(self)
        self.number_label.setText("Номер: ")
        self.number_label.move(40, 60)

        self.name_input = QLineEdit(self)
        self.name_input.move(150, 30)
        
        self.number_input = QLineEdit(self)
        self.number_input.move(150, 60)
        
        self.memory = QListWidget(self)
        
    def add(self):
        self.memory.addItem(self.name_input.text() + ' ' + self.number_input.text())
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
        
