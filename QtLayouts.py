from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
import sys

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
		self.createLayout()
		vbox = QVBoxLayout()
		vbox.addWidget(self.groupBox)
		self.setLayout(vbox)
		self.show()

	def createLayout(self):
		self.groupBox = QGroupBox("What Is Your Favorite Programming Language ?")
		hboxLayout = QHBoxLayout()
		self.button = QPushButton("Football", self)
		self.button.setMinimumHeight(40)
		hboxLayout.addWidget(self.button)
		self.button2 = QPushButton("Cricket", self)
		self.button2.setMinimumHeight(40)
		hboxLayout.addWidget(self.button2)
		self.button3 = QPushButton("Tennis", self)
		self.button3.setMinimumHeight(40)
		hboxLayout.addWidget(self.button3)
		self.groupBox.setLayout(hboxLayout)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())