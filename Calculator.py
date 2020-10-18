import sys, time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from mainwindow import Ui_Calculator
import functions as f


class Calculator(QMainWindow, Ui_Calculator):

	def __init__(self):
		super().__init__()
		self.x = 0
		self.y = 0
		self.setupUi(self)
		self.sign = None
		self.mem = 0
		self.flag = False

		self.rates = {}
		self.selected_currency = []

		self.f = {
			'btn_addition': '+',
			'btn_subtraction': '-',
			'btn_multiplication': '*',
			'btn_division': '÷',
			'btn_power': 'ˆ',
			'btn_root': '√',
			'btn_factorial': '!',
		}

		# CALCULATOR PAGE
		self.btn_to_calculator.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.calculator_page))


		# BUTTONS WITH DIGIT
		self.btn_0.clicked.connect(self.button_with_digit)
		self.btn_1.clicked.connect(self.button_with_digit)
		self.btn_2.clicked.connect(self.button_with_digit)
		self.btn_3.clicked.connect(self.button_with_digit)
		self.btn_4.clicked.connect(self.button_with_digit)
		self.btn_5.clicked.connect(self.button_with_digit)
		self.btn_7.clicked.connect(self.button_with_digit)
		self.btn_8.clicked.connect(self.button_with_digit)
		self.btn_6.clicked.connect(self.button_with_digit)
		self.btn_9.clicked.connect(self.button_with_digit)

		# FUNCTIONS BUTTONS
		self.btn_addition.clicked.connect(self.buttonClicked)
		self.btn_subtraction.clicked.connect(self.buttonClicked)
		self.btn_multiplication.clicked.connect(self.buttonClicked)
		self.btn_division.clicked.connect(self.buttonClicked)
		self.btn_power.clicked.connect(self.buttonClicked)
		self.btn_root.clicked.connect(lambda: self.display_2.setText(f'√{self.display.text()}'))
		self.btn_root.clicked.connect(lambda: self.display.setText(f'{f.root(self.display.text())}'))
		self.btn_factorial.clicked.connect(lambda: self.display_2.setText(f'{self.display.text()}!'))
		self.btn_factorial.clicked.connect(lambda: self.display.setText(f'{f.fctrial(self.display.text())}'))

		# MEMORY BUTTONS
		self.btn_mem_plus.clicked.connect(self.memory)
		self.btn_mem_minus.clicked.connect(self.memory)
		self.btn_mem_show.clicked.connect(self.memory)
		self.btn_mem_reset.clicked.connect(self.memory)

		self.btn_result.clicked.connect(self.result)
		self.btn_AC.clicked.connect(self.reset)
		self.btn_minus.clicked.connect(self.minus)
		self.btn_dot.clicked.connect(self.dot)

		# CURRENCY PAGE
		self.btn_to_currency.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.currency_page))
		self.btn_to_currency.clicked.connect(self.take_rates)
		self.btn_currency_result.clicked.connect(self.currency_result)

		# BUTTONS WITH CURRENCY
		self._036.clicked.connect(self.select_currency)
		self._944.clicked.connect(self.select_currency)
		self._826.clicked.connect(self.select_currency)
		self._051.clicked.connect(self.select_currency)
		self._933.clicked.connect(self.select_currency)
		self._975.clicked.connect(self.select_currency)
		self._986.clicked.connect(self.select_currency)
		self._348.clicked.connect(self.select_currency)
		self._344.clicked.connect(self.select_currency)
		self._208.clicked.connect(self.select_currency)
		self._840.clicked.connect(self.select_currency)
		self._978.clicked.connect(self.select_currency)
		self._356.clicked.connect(self.select_currency)
		self._398.clicked.connect(self.select_currency)
		self._124.clicked.connect(self.select_currency)
		self._417.clicked.connect(self.select_currency)
		self._156.clicked.connect(self.select_currency)
		self._498.clicked.connect(self.select_currency)
		self._578.clicked.connect(self.select_currency)
		self._985.clicked.connect(self.select_currency)
		self._946.clicked.connect(self.select_currency)
		self._702.clicked.connect(self.select_currency)
		self._972.clicked.connect(self.select_currency)
		self._949.clicked.connect(self.select_currency)
		self._934.clicked.connect(self.select_currency)
		self._860.clicked.connect(self.select_currency)
		self._980.clicked.connect(self.select_currency)
		self._203.clicked.connect(self.select_currency)
		self._752.clicked.connect(self.select_currency)
		self._756.clicked.connect(self.select_currency)
		self._710.clicked.connect(self.select_currency)
		self._410.clicked.connect(self.select_currency)
		self._392.clicked.connect(self.select_currency)

	def button_with_digit(self):
		sender = self.sender()
		digit = sender.objectName()[-1]
		number = self.display.text()
		if number == '0':
			self.display.setText(f'{digit}')
		elif number == 'Error' or number == 'ZeroDivisionError':
			self.display.setText(f'{digit}')
		else:
			self.display.setText(f'{number}{digit}')

	def minus(self):
		number = float(self.display.text())
		if number > 0:
			self.display.setText(f'-{self.display.text()}')
		elif number < 0:
			self.display.setText(f'{self.display.text()[1:]}')

	def reset(self):
		self.display.setText('0')
		self.display_2.setText('')
		self.x = 0
		self.y = 0

	def dot(self):
		if '.' not in self.display.text():
			self.display.setText(f'{self.display.text()}.')

	def memory(self):
		sender = self.sender().objectName()
		if sender == 'btn_mem_plus':
			try:
				self.mem += float(self.display.text())
			except ValueError:
				self.display.setText('Error')
		elif sender == 'btn_mem_minus':
			try:
				self.mem -= float(self.display.text())
			except ValueError:
				self.display.setText('Error')
		elif sender == 'btn_mem_show':
			self.display.setText(f'{self.mem}')
		else:
			self.mem = 0

	def buttonClicked(self):
		self.flag = True
		sender = self.sender()
		self.sign = sender.objectName()
		if not self.display.text():
			self.x = 0
		else:
			self.x = self.display.text()
		self.display.setText('')
		self.display_2.setText(f'{self.x} {self.f[sender.objectName()]}')

	def result(self):
		if self.flag:
			self.flag = False
			self.y = self.display.text()
			if not self.y:
				self.y = 0

			if self.sign == 'btn_addition':
				self.display.setText(f'{f.addition(self.x, self.y)}')
				self.display_2.setText(f'{self.x}+{self.y}')
			elif self.sign == 'btn_subtraction':
				self.display.setText(f'{f.subtraction(self.x, self.y)}')
				self.display_2.setText(f'{self.x}-{self.y}')
			elif self.sign == 'btn_multiplication':
				self.display.setText(f'{f.multiplication(self.x, self.y)}')
				self.display_2.setText(f'{self.x}*{self.y}')
			elif self.sign == 'btn_division':
				self.display.setText(f'{f.division(self.x, self.y)}')
				self.display_2.setText(f'{self.x}÷{self.y}')
			elif self.sign == 'btn_power':
				self.display.setText(f'{f.power(self.x, self.y)}')
				self.display_2.setText(f'{self.x}ˆ{self.y}')

		else:
			if not self.y:
				self.y = 0

			if self.sign == 'btn_addition':
				self.display.setText(f'{f.addition(self.x, self.y)}')
				self.display_2.setText(f'{self.x}+{self.y}')
			elif self.sign == 'btn_subtraction':
				self.display.setText(f'{f.subtraction(self.x, self.y)}')
				self.display_2.setText(f'{self.x}-{self.y}')
			elif self.sign == 'btn_multiplication':
				self.display.setText(f'{f.multiplication(self.x, self.y)}')
				self.display_2.setText(f'{self.x}*{self.y}')
			elif self.sign == 'btn_division':
				self.display.setText(f'{f.division(self.x, self.y)}')
				self.display_2.setText(f'{self.x}÷{self.y}')
			elif self.sign == 'btn_power':
				self.display.setText(f'{f.power(self.x, self.y)}')
				self.display_2.setText(f'{self.x}ˆ{self.y}')
		self.x = self.display.text()

	def take_rates(self):
		self.rates = f.rate_from_cbrf()
		self.selected_currency = self.rates['840']
		self.display_currency_name.setText(self.rates['840'][1])

	def select_currency(self):
		sender = self.sender()
		currency_number = sender.objectName()[1:]
		self.selected_currency = self.rates[currency_number]
		self.display_currency_name.setText(self.rates[currency_number][1])
		self.display_currency.setText(str(self.rates[currency_number][0]))
		self.display_RUB.setText(str(self.rates[currency_number][2]))

	def currency_result(self):
		x = self.display_currency.text()
		try:
			y = self.selected_currency[2] / self.selected_currency[0]
		except IndexError:
			return self.display_currency.setText('Select Currency')

		try:
			self.display_RUB.setText(str(f'{f.multiplication(x, y):.2f}'))
		except ValueError:
			self.display_RUB.setText('Error')


app = QApplication(sys.argv)
ex = Calculator()
ex.show()
sys.exit(app.exec_())
