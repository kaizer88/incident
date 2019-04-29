# Add any helper classes/functions here. If a function/class can be removed from the context of the project and is still valid, it can be stored here

from datetime import datetime
import math
from django.conf import settings
from dateutil.relativedelta import relativedelta

class DictDiffer(object):
  """
  Calculate the difference between two dictionaries as:
  (1) items added
  (2) items removed
  (3) keys same in both but changed values
  (4) keys same in both and unchanged values
  """
  def __init__(self, current_dict, past_dict):
    self.current_dict, self.past_dict = current_dict, past_dict
    self.set_current, self.set_past = set(current_dict.keys()), set(past_dict.keys())
    self.intersect = self.set_current.intersection(self.set_past)
  def added(self):
    return self.set_current - self.intersect
  def removed(self):
    return self.set_past - self.intersect
  def changed(self):
    return set(o for o in self.intersect if self.past_dict[o] != self.current_dict[o])
  def unchanged(self):
    return set(o for o in self.intersect if self.past_dict[o] == self.current_dict[o])


class IdNumberValidation():
  def generate_luhn_digit(self, id_number):
    total = 0
    count = 0
    i = 0
    while i < len(id_number):
      multiple = (count % 2) + 1
      count += 1
      temp = multiple * int(id_number[i])
      temp = int(math.floor(temp / 10) + (temp % 10))
      total += temp
      i += 1

    total = (total * 9) % 10

    return total

  def validate(self, id_number):
    if not settings.VALIDATE_ID_NUMBERS:
      return True

    try:
      if not id_number.isdigit() or not len(id_number) == 13:
        return False

      if not self.get_birthdate(id_number[:6]):
        return False

      last_number = int(id_number[-1])
      number_section = id_number[0:-1]

      return last_number == self.generate_luhn_digit(number_section)

    except:
      return False


  def get_birthdate(self, id_number):
    try:

      dob = datetime.strptime(id_number[0:6], "%y%m%d")
      if dob > datetime.now():
        dob = dob - relativedelta(years=100)
      return dob
    except:
      return None

  def get_age(self, id_number):
    try:
      delta =  datetime.now() - datetime.strptime(id_number[0:6], "%y%m%d")
      return delta.days / 365
    except:
      return None

  def Id_number_details(self, id_number):
    valid = self.validate(id_number)

    birth_date = None  if valid is False else self.get_birthdate(id_number)
    age = None if valid is False else self.get_age(id_number)
    is_male = None if valid is False else int(id_number[6]) >= 5

    return birth_date, age, is_male
