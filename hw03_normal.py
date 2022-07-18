# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import math
list_of_numb = [2, -5, 8, 9, -25, 25, 4]
list_of_roots = []
for value in list_of_numb:
	if (value > 0) and ((value*100)%100 == 0):
		list_of_roots.append(math.sqrt(value))
print(list_of_roots)
print("\n"*3)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
date_string="02.11.2013"
day=int(date_string[:2])
month=int(date_string[3:5])
year=int(date_string[6:10])

def day_into_text(dig_day):
	if dig_day ==1:
		return "первое"
	elif dig_day ==2:
		return "второе"
	elif dig_day ==3:
		return "третье"
	elif dig_day ==4:
		return "четвёртое"
	elif dig_day ==5:
		return "пятое"
	elif dig_day ==6:
		return "шестое"
	elif dig_day ==7:
		return "седьмое"
	elif dig_day ==8:
		return "восьмое"
	elif dig_day ==9:
		return "девятое"
		elif dig_day ==10:
		return "десятое"


def month_into_text(dig_month):
	if dig_month ==1:
		return "января"
	elif dig_month ==2:
		return "февраля"
	elif dig_month ==3:
		return "марта"
	elif dig_month ==4:
		return "апреля"
	elif dig_month ==5:
		return "мая"
	elif dig_month ==6:
		return "июня"
	elif dig_month ==7:
		return "июля"
	elif dig_month ==8:
		return "августа"
	elif dig_month ==9:
		return "сентября"
	elif dig_month ==10:
		return "октября"
	elif dig_month ==11:
		return "ноября"
	else:
		return "декабря"


print("{} {} {} года".format(day_into_text(day), month_into_text(month), year))
print("\n"*3)
  
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random

n = int(20)
list_rnd = []
i3=int(0)
while i3 < n:
  list_rnd.append(random.randint(-100, 100))
  i3+=1
print(list_rnd)
# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst_dif=[]
lst_dif2=[]
i4a=int(0)
i4b=int(0)

#Function "not_in_list(value, list)" returns "1" if it does not find "value" in list
def not_in_list(value, list_of_val):

    flag=1
    for number in list_of_val:
        if number == value:
            flag=0
    return flag

#Function "not_duplicated(value, list)" returns "1" if it does not find "value" in list two times or more
def not_duplicated(value, list_of_val):

    flag_b=0
    for number_b in list_of_val:
        if number_b == value:
            flag_b+=1
    if flag_b > 1:
        return 0
    else:
        return 1
 


while i4a<len(lst):
    if not_in_list(lst[i4a], lst_dif):
        lst_dif.append(lst[i4a])
    i4a+=1

while i4b<len(lst):
    if not_duplicated(lst[i4b], lst) and not_in_list(lst[i4b], lst_dif2):
        lst_dif2.append(lst[i4b])
    i4b+=1

print(lst_dif)
print(lst_dif2)

