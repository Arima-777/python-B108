# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fr_list = ["яблоко", "банан", "киви", "арбуз"]
i = int(0)
while i < len(fr_list):
	print("{}. {:>6}".format(i+1, fr_list[i]))
	i+=1
print("\n"*3)
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
smart_lst= ["Tony", "Jhony", "Alex", "Putin", "Keyton", "Lenin", "Jason", "Arthur"]
handsome_lst= ["Kyler", "Tyler", "Romul", "Putin", "Keyton", "Lenin", "Hugo", "Arthur"]

def intersections_filter(list1, list2):
	current_index=int(0)
	while current_index<len(list2):
		secondary_index=int(0)
		while secondary_index<len(list1):
			if list2[current_index] == list1[secondary_index]:
				list1.pop(secondary_index)
			secondary_index+=1
		current_index+=1
intersections_filter(handsome_lst, smart_lst)
for name in handsome_lst:
	print(name)
print("\n"*3)
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
f_list=[64, 6, 1, 8, 3, 65, 321, 5, 2, 200, 12, 50]
s_list=[]
counter = int(0)
while counter < len(f_list):
	if f_list[counter]%2 == 0:
		s_list.append(f_list[counter]/4)
	else:
		s_list.append(f_list[counter]*2)
	counter+=1
print(s_list)
