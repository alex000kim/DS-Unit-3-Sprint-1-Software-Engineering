import os
import pytest

from datetime import datetime
from random import randint
from src.computer import Computer
from glob import glob


@pytest.fixture()
def setup_teardown():
	price = 1500
	width = 9
	length = 8
	height = 7
	year_manufactured = 2015
	computer = Computer(price, width, length, height, year_manufactured)
	yield computer, price, width, length, height, year_manufactured
	for f in glob("saved_computer_*"):
		os.remove(f)


def test_repr(setup_teardown):
	computer, price, width, length, height, year_manufactured = setup_teardown
	assert repr(computer)==f"Computer(price={price}, width={width}, length={length}, height={height}, year_manufactured={year_manufactured})"

def test_str(setup_teardown):
	computer, price, width, length, height, _ = setup_teardown
	assert str(computer)==f"Price: ${price}. Dimensions: {width}x{length}x{height}"

def test_year_four_digits(setup_teardown):
	computer, *_ = setup_teardown
	assert len(str(computer.year_manufactured))==4

def test_get_years_since_manufactured(setup_teardown):
	computer, *_, year_manufactured= setup_teardown
	assert computer.get_years_since_manufactured() == (datetime.now().year - year_manufactured)

def test_is_portable(setup_teardown):
	computer, *_= setup_teardown
	with pytest.raises(NotImplementedError):
		computer.is_portable()

def test_save_to_disk(setup_teardown):
	computer, *_= setup_teardown
	obj_index = randint(0, 10000)
	computer.save_to_disk(obj_index=obj_index)
	assert os.path.isfile(f"saved_computer_{obj_index}") is True
