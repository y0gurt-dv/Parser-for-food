import sqlite3
from os import system

db=sqlite3.connect('food.db')
sql= db.cursor()

list_food=[]

def clear():
	_=system('clear')



def losses():
	loss=input('Введите потери: ')
	try:
		for i in range(1,5):
			list_food[-1][i]-=list_food[-1][i]*(int(loss)/100)
	except:
		print('Некорректный ввод')
		losses()
	print('1)Вернуться в меню')
	inp=input('>>> ')
	if inp=='1':
		pass
	else:
		print('Некорректный ввод')
		losses()

def mass():
	weight=input('Введите массу продукта: ')
	try:
		for i in range(1,5):
			list_food[-1][i]=list_food[-1][i]*(int(weight)/100)
	except:
		print('Некорректный ввод')
		mass()
	losses()

def menu():
	print('\t1)Добавить продукт')
	print('\t2)Вывод списка продуктов')
	print('\t3)Удалить элемент из списка')
	print('\t4)Закончить и вывести список')
	print('\t5)Очистить список')

def print_list():
	clear()
	for i in list_food:
		print(i)
	print('1)Вернуться в меню')
	inp=input('>>> ')
	if inp=='1':
		pass
	else:
		print('Некорректный ввод')
		print_list()

def search():
	food=input("Введите название продукта: ").strip()
	if food =='':
		clear()
		search()
	else:
		sql.execute(f"SELECT food FROM all_about_food WHERE food = '{food}'")
		if sql.fetchone() is None:
			print('Такого названия нет')
			print('Похожие:')
			sql.execute(f"SELECT food FROM all_about_food WHERE food LIKE '%{food}%'")
			result= sql.fetchall()
			for i in result:
				print('\t'+i[0])
			search()
		else:
			sql.execute(f"SELECT * FROM all_about_food WHERE food = '{food}'")
			list_food.append(list(sql.fetchone()))
			mass()

def del_element():
	clear()
	for i in range(0,len(list_food)):
		print(f'{i}) {list_food[i]}')

	print(f'{len(list_food)})Вернуться в меню')
	inp=input('>>> ')
	if inp==str(len(list_food)):
		pass
	else:
		try:
			list_food.pop(int(inp))
			del_element()
		except:
			print('Некорректный ввод')
			del_element()

def end():
	clear()
	for i in list_food:
		print(i)
	quit()




while True:
	clear()
	menu()
	inp=input('>>> ')
	if inp=='1': 
		clear()
		search()
	elif inp=='2': print_list()
	elif inp=='3': del_element()
	elif inp=='4': end()
	elif inp=='5': list_food=[]
	else: print('Некорректный ввод')