"""
Завдання 1
Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
"""
import datetime
now = datetime.datetime.now().date()
previous_date = datetime.date(2024, 4, 23)
date_diff = (now - previous_date).days
print(f"Task 1, check: {date_diff}")


"""""
написати функцію get_numbers_ticket(min, max, quantity), 
яка допоможе генерувати набір унікальних випадкових чисел для  лотерей. 
буде повертати випадковий набір чисел у межах заданих параметрів, 
всі випадкові числа в наборі повинні бути унікальні ==  відсортований список унікальних чисел.
"""
import random

def get_numbers_ticket(min, max, quantity):
    if min > max:
        return "Your max is smaller than min number"
    elif quantity >= (max-min):
        return "You have chosen way to many numbers for your range"
    else:
        numbers = (list(range(min,max+1)))
        win_num = random.sample(numbers , quantity)
        win_num.sort()
        return win_num

print(get_numbers_ticket(1,4,3))
print(get_numbers_ticket(1,14,3))
print(get_numbers_ticket(15,4,3))


"""
Завдання 3
номери записані у різних форматах
функція, яка автоматично нормалізує номери телефонів до потрібного формату видаляючи всі зайві символи т
а додаючи міжнародний код країни

"""
import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def sanitized_numbers(raw_numbers):
    normal_num =[]
    normal_num_2 =[]

    for num in raw_numbers:
        num = num.strip()

        pattern = r"[;,\-:!\s\D]+"
        repl = ""
        num_clean = re.sub(pattern, repl, num)
        normal_num.append(num_clean)
   
    for num in normal_num:
        if num.startswith("+380"):
            normal_num_2.append(num)  
        elif num.startswith("0"):
            normal_num_2.append("+380" + num)  
        else:
            normal_num_2.append("+" + num) 

    return normal_num_2 

print(sanitized_numbers(raw_numbers))

"""
Завдання 4
створити функцію get_upcoming_birthdays
Функція повернути список у кого день народження вперед на 7 днів включаючи поточний день.
припадати на вихідні, функція повинна враховувати це та переносити  привітання на наступний робочий день
"""

from datetime import datetime
from datetime import date
from datetime import timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Brice Henonin", "birthday": "1990.03.07"},
    {"name": "Wale Owale", "birthday": "1990.03.09"},
    {"name": "John Smith", "birthday": "1990.03.10"}
]

today = datetime.today().date()
today_day_of_week = today.weekday() 
today_week_ahead = today + timedelta(days = 7)
bd_list=[]

for user in users:
  birthday = datetime.strptime(user["birthday"],"%Y.%m.%d").date()
  birthday_date_this_year = birthday.replace(year=today.year)
  birthday_date_this_year_week_ahead = birthday_date_this_year+timedelta(days=7)
  birthday_date_this_year_day_of_week = birthday_date_this_year.weekday()

  if birthday_date_this_year >= today and birthday_date_this_year <= today_week_ahead:
    bd_list.append(user["name"])
  
  if (today_day_of_week == 0) and (birthday_date_this_year >= (today - timedelta(days = 2)) and birthday_date_this_year <= (today - timedelta(days = 1))):
    bd_list.append(user["name"])
  
print(bd_list)