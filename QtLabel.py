from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QVBoxLayout, QLabel
import sys
from PyQt5 import QtGui

class Window(QDialog):
	def __init__(self):
		super().__init__()

		self.title = "PyQt5 Window"
		self.top = 100
		self.left = 100
		self.width = 400
		self.height = 300

		self.InitWindow()

	def InitWindow(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		vbox = QVBoxLayout()
		label = QLabel("Label in PyQt5")
		label.setFont(QtGui.QFont("Sanserif",20))
		vbox.addWidget(label)
		self.setLayout(vbox)
		self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())