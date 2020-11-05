import unittest

from datetime import datetime

from src.computer import Computer


class TestComputer(unittest.TestCase):

	def test_repr(self):
		computer = Computer(1500, 9, 8, 7, 2016)
		self.assertEqual(repr(computer), 
			"Computer(price=1500, width=9, length=8, height=7, year_manufactured=2016)")

	def test_str(self):
		computer = Computer(1500, 9, 8, 7, 2015)
		self.assertEqual(str(computer), 
			"Price: $1500. Dimensions: 9x8x7")

	def test_year_four_digits(self):
		computer = Computer(1500, 9, 8, 7, 2015)
		self.assertEqual(len(str(computer.year_manufactured)), 4)

	def test_get_years_since_manufactured(self):
		year_manufactured = 2015
		computer = Computer(1500, 9, 8, 7, year_manufactured)
		self.assertEqual(computer.get_years_since_manufactured(), datetime.now().year - year_manufactured)

if __name__ == '__main__':
	unittest.main()