import joblib
from datetime import datetime

class Computer:
  # initilizer or constructor
  def __init__(self, price, width, length, height, year_manufactured):
    self.price = price
    self.width = width
    self.length = length
    self.height = height
    self.year_manufactured = year_manufactured

  def __repr__(self):
    return f"Computer(price={self.price}, width={self.width}, length={self.length}, height={self.height}, year_manufactured={self.year_manufactured})"
  
  def __str__(self):
    return f"Price: ${self.price}. Dimensions: {self.width}x{self.length}x{self.height}"

  def get_years_since_manufactured(self):
    time_now = datetime.now()
    years_since_manufactured = time_now.year - self.year_manufactured
    return years_since_manufactured

  def is_portable(self):
    raise NotImplementedError('is_portable() not implemented. Computer is a parent class')

  def save_to_disk(self, obj_index):
  	joblib.dump(self, f"saved_computer_{obj_index}")