import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout, QLCDNumber

class MainView(QMainWindow):

    def __init__(self):
        super(MainView, self).__init__()

        self.initUI()

    def initUI(self):
        menuBar = self.menuBar()
        viewMenu = menuBar.addMenu('&Widok')
        editMenu = menuBar.addMenu('&Edycja')
        helpMenu = menuBar.addMenu('&Pomoc')

        widget = WidgetComponent(self)
        self.setCentralWidget(widget)
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()
        widget.show()


class WidgetComponent(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        display = QLCDNumber(self)
        display.setFixedHeight(80)
        display.display(0)
        grid.addWidget(display, 0, 0, 1, 5)

        names = ['MC', 'MR', 'MS', 'M+', 'M-',
                 '\u20D6', 'CE', 'C', '\u00B1', '\u221A',
                 '7', '8', '9', '/', '%',
                 '4', '5', '6', '*', '1/x',
                 '1', '2', '3', '-', '=',
                 '0', '', ',', '+', '']

        positions = [(i, j) for i in range(1, 7) for j in range(5)]
        for position, name in zip(positions, names):

            if name == '':
                continue

            button = QPushButton(name)
            if name == '0':
                grid.addWidget(button, 6, 0, 1, 2)
            elif name == '=':
                button.setFixedHeight(80)
                grid.addWidget(button, 5, 4, 2, 1)
            else:
                grid.addWidget(button, *position)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = MainView()
    sys.exit(app.exec_())
