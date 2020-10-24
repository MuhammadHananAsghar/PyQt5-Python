from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QDialog, QGroupBox, QGridLayout, QVBoxLayout
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
		gridLayout = QGridLayout()
		self.button = QPushButton("Football", self)
		self.button.setMinimumHeight(40)
		gridLayout.addWidget(self.button, 0, 0)
		self.button2 = QPushButton("Cricket", self)
		self.button2.setMinimumHeight(40)
		gridLayout.addWidget(self.button2, 0, 1)
		self.button3 = QPushButton("Tennis3", self)
		self.button3.setMinimumHeight(40)
		gridLayout.addWidget(self.button3, 1, 0)
		self.button4 = QPushButton("Tennis4", self)
		self.button4.setMinimumHeight(40)
		gridLayout.addWidget(self.button4, 1, 1)
		self.button5 = QPushButton("Tennis5", self)
		self.button5.setMinimumHeight(40)
		gridLayout.addWidget(self.button5)
		self.button6 = QPushButton("Tennis6", self)
		self.button6.setMinimumHeight(40)
		gridLayout.addWidget(self.button6)
		self.groupBox.setLayout(gridLayout)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())