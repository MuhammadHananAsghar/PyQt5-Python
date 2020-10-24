from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from PyQt5 import QtGui

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.title = "PyQt5 Window"
		self.top = 100
		self.left = 100
		self.width = 400
		self.height = 300
		# self.icon

		self.InitWindow()

	def InitWindow(self):
		self.setWindowTitle(self.title)
		# self.setWindowIcon(QtGui.QIcon(self.icon))
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.UiComponents()
		self.show()

	def UiComponents(self):
		button = QPushButton("Button",self)
		button.move(50,50)
		button.setGeometry(100,100,100,100)
		button.setToolTip("&lt;h1&gt;This Is Click Button&lt;h1&gt;")
		button.clicked.connect(self.ButtonAction)

	def ButtonAction(self):
		print("Button clicked")

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
