import os
import unittest

from datetime import datetime
from random import randint
from src.computer import Computer
from glob import glob

class TestComputer(unittest.TestCase):
	def setUp(self):
		self.computer = Computer(1500, 9, 8, 7, 2016)

	def tearDown(self):
		for f in glob("saved_computer_*"):
			os.remove(f)

	def test_repr(self):
		self.assertEqual(repr(self.computer), 
			"Computer(price=1500, width=9, length=8, height=7, year_manufactured=2016)")

	def test_str(self):
		self.assertEqual(str(self.computer), 
			"Price: $1500. Dimensions: 9x8x7")

	def test_year_four_digits(self):
		self.assertEqual(len(str(self.computer.year_manufactured)), 4)

	def test_get_years_since_manufactured(self):
		self.assertEqual(self.computer.get_years_since_manufactured(), datetime.now().year - 2016)

	def test_is_portable(self):
		with self.assertRaises(NotImplementedError):
			self.computer.is_portable()

	def test_save_to_disk(self):
		obj_index = randint(0, 10000)
		self.computer.save_to_disk(obj_index=obj_index)
		self.assertTrue(os.path.isfile(f"saved_computer_{obj_index}"))

if __name__ == '__main__':
	unittest.main()