import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from mainwindow import Ui_Calculator


class Calculator(QMainWindow, Ui_Calculator):
	def __init__(self):
		super().__init__()
		self.x = 0
		self.y = 0
		self.setupUi(self)
		self.sign = None
		self.result.setText('0')

		self.plus.clicked.connect(self.buttonClicked)
		self.minus.clicked.connect(self.buttonClicked)
		self.mult.clicked.connect(self.buttonClicked)
		self.divis.clicked.connect(self.buttonClicked)
		self.enter.clicked.connect(self.res)

	def buttonClicked(self):
		sender = self.sender()
		self.sign = sender.text()
		self.x = self.display.text()
		if not self.x:
			self.x = 0
		self.result.setText(f'{self.x} {sender.text()}')
		self.display.setText('')

	def isInteger(self, i):
		return int(i) if i.is_integer() else i

	def res(self):
		self.y = self.display.text()
		if not self.y:
			self.y = 0

		if self.sign == '+':
			self.result.setText(f'{self.x} {self.sign} {self.y} =\n {self.addition()}')
			self.display.setText('')
		elif self.sign == '-':
			self.result.setText(f'{self.x} {self.sign} {self.y} =\n {self.subtraction()}')
			self.display.setText('')
		elif self.sign == '*':
			self.result.setText(f'{self.x} {self.sign} {self.y} =\n {self.multiplication()}')
			self.display.setText('')
		elif self.sign == '/':
			self.result.setText(f'{self.x} {self.sign} {self.y} =\n {self.division()}')
			self.display.setText('')

	def addition(self):
		try:
			return f'{self.isInteger(float(float(self.x) + float(self.y)))}'
		except ValueError:
			return 'Неправильный ввод!'

	def subtraction(self):
		try:
			return f'{self.isInteger(float(float(self.x) - float(self.y)))}'
		except ValueError:
			return 'Неправильный ввод!'

	def multiplication(self):
		try:
			return f'{self.isInteger(float(float(self.x) * float(self.y)))}'
		except ValueError:
			return 'Неправильный ввод!'

	def division(self):
		try:
			return f'{self.isInteger(float(float(self.x) / float(self.y)))}'
		except ZeroDivisionError:
			return 'На ноль делить нельзя!'
		except ValueError:
			return 'Неправильный ввод!'


app = QApplication(sys.argv)
ex = Calculator()
ex.show()
sys.exit(app.exec_())
