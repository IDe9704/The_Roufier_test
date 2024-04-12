# напиши здесь код третьего экрана приложения

from instr.py import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class FinalWin(QWidget):

    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.txt_index = QLabel(txt_index)
        self.txt_workheart = QLabel(txt_workheart)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txtindex)
        self.layout.addWidget(self.txtend)
        self.setLayout(self.layout)