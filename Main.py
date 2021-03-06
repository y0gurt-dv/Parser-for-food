import sqlite3
from os import system,name

db=sqlite3.connect('food.db')
sql= db.cursor()

def clear():
	 if name=='nt':
		 _=system('cls')
	 else:
		 _=system('clear')
	
def return_menu():
	print('1)Вернуться в меню')
	inp=input('>>> ').strip()
	if inp=='1':
		pass
		return
	else:
		return_menu()

def losses():
	loss=input('Введите потери при холодной: ').strip()
	try:
		for i in range(1,6):
			list_food[-1][i]-=list_food[-1][i]*(int(loss)/100)
	except:
		print('Некорректный ввод ')
		losses()
	if boole=='1':
		prise()

def prise():
	cost=input('Введите цену продукта: ')
	try:
		list_food[-1].insert((len(list_food[-1])-1),((int(cost)/1000)*int(list_food[-1][-1])))
		list_food[-1].pop()
	except:
		print('Некорректный ввод ')
		prise()
	return

def mass():
	weight=input('Введите массу продукта: ')
	try:
		list_food[-1].append(int(weight))
		list_food[-1].append(int(weight))
	except:
		print('Некорректный ввод ')
		mass()
	try:
		for i in range(1,5):
			list_food[-1][i]=list_food[-1][i]*(int(weight)/100)
	except:
		print('Некорректный ввод ')
		mass()
	losses()

def menu():
	print('\t1)Добавить продукт')
	print('\t2)Вывод списка продуктов')
	print('\t3)Удалить элемент из списка')
	print('\t4)Закончить и вывести список')
	print('\t5)Очистить список')
	print('\t6)Вернуться назад и ОЧИСТИТЬ список')

def print_list():
	clear()
	if boole=='1':
		for i in list_food:
			print(f'-----{i[0].capitalize()}')	
			print(f'\tКалорийность:{i[1]}')
			print(f'\tБелки:{i[2]}')
			print(f'\tЖиры:{i[3]}')
			print(f'\tУглеводы:{i[4]}')
			print(f'\tМасса:{i[5]}')
			print(f'\tЦена:{i[6]}')
	else:
		for i in list_food:
			print(f'-----{i[0].capitalize()}')
			print(f'\tКалорийность:{i[1]}')
			print(f'\tБелки:{i[2]}')
			print(f'\tЖиры:{i[3]}')
			print(f'\tУглеводы:{i[4]}')
			print(f'\tМасса:{i[5]}')
	return_menu()

def add_el():
	food=input("Введите название продукта: ").strip().lower()
	if food =='':
		clear()
		add_el()
	else:
		sql.execute(f"SELECT food FROM all_about_food WHERE food = '{food}'")
		if sql.fetchone() is None:
			print('Такого названия нет')
			print('Похожие:')
			sql.execute(f"SELECT food FROM all_about_food WHERE food LIKE '%{food}%'")
			result= sql.fetchall()
			for i in range(len(result)):
				print(f'\t{i}){result[i][0]}')
			print(f'{len(result)})Найти другой продукт')
			inp=input('>>> ').strip()
			if inp==str(len(result)):
				clear()
				add_el()
			else:
				try:
					sql.execute(f"SELECT * FROM all_about_food WHERE food = '{result[int(inp)][0]}'")
					list_food.append(list(sql.fetchone()))
					mass()
				except:
					print('Некорректный ввод ')
					add_el()
		else:
			sql.execute(f"SELECT * FROM all_about_food WHERE food = '{food}'")
			list_food.append(list(sql.fetchone()))
			mass()

def del_element():
	clear()
	for i in range(0,len(list_food)):
		print(f'{i}) {list_food[i]}')
	print(f'{len(list_food)})Вернуться в меню')
	inp=input('>>> ').strip()
	if inp==str(len(list_food)):
		pass
	else:
		try:
			list_food.pop(int(inp))
			del_element()
		except:
			print('Некорректный ввод ')
			del_element()

def end():
	clear()
	if boole.lower()=='1':
		while True:
			count=input('Введите цисло порций: ').strip()
			try:
				100/int(count)
				break
			except:
				print('Некорректный ввод ')
				clear()
		calories,Protein,Fats,Carbohydrates,prise=0,0,0,0,0
		for i in range(0,len(list_food)):
			calories+=list_food[i][1]
			Protein+=list_food[i][2]
			Fats+=list_food[i][3]
			Carbohydrates+=list_food[i][4]
			prise+=list_food[i][6]
		for i in list_food:
			print(f'-----{i[0].capitalize()}')	
			print(f'\tКалорийность:{i[1]}')
			print(f'\tБелки:{i[2]}')
			print(f'\tЖиры:{i[3]}')
			print(f'\tУглеводы:{i[4]}')
			print(f'\tМасса:{i[5]}')
			print(f'\tЦена:{i[6]}')
		print(f'Общая Калорийность: {calories}ккал')
		print(f'Общие содержание белка: {Protein}')
		print(f'Общие содержание жиров: {Fats}')
		print(f'Общие содержание углеводов: {Carbohydrates}')
		print(f'Общая цена: {prise}')
		print(f'Цена каждой порции: {prise/int(count)}')
	else:
		calories,Protein,Fats,Carbohydrates=0,0,0,0
		for i in range(0,len(list_food)):
			calories+=list_food[i][1]
			Protein+=list_food[i][2]
			Fats+=list_food[i][3]
			Carbohydrates+=list_food[i][4]
		for i in list_food:
			print(f'-----{i[0].capitalize()}')	
			print(f'\tКалорийность:{i[1]}')
			print(f'\tБелки:{i[2]}')
			print(f'\tЖиры:{i[3]}')
			print(f'\tУглеводы:{i[4]}')
			print(f'\tМасса:{i[5]}')
		print(f'Общая Калорийность: {calories}ккал')
		print(f'Общие содержание белка: {Protein}')
		print(f'Общие содержание жиров: {Fats}')
		print(f'Общие содержание углеводов: {Carbohydrates}')

def consider_prise():
	while True:
		inp=input("Учитывать ли цену(1/0): ").lower().strip()
		if (inp!='1') and (inp!='0'):
			print('Некорректный ввод ')
		else:
			return inp

def reload_programm():
	print('1)Вернуться в начало программы')	
	while True: 
		inp=input('>>> ').strip()
		if inp=='1':
			break
		else:
			print('Некорректный ввод ')

def main(boole):
	while True:
		clear()
		menu()
		inp=input('>>> ').strip()
		if inp=='1': 
			clear()
			add_el()
		elif inp=='2': print_list()
		elif inp=='3': del_element()
		elif inp=='4': 
			end()
			reload_programm()
			break
		elif inp=='5': list_food=[]
		elif inp=='6': break
		else: print('Некорректный ввод ')

def search():

	food=input("Введите название продукта: ").strip().lower()
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
			for i in range(len(result)):
				print(f'\t{i}){result[i][0]}')
			print(f'{len(result)})Найти другой продукт')
			inp=input('>>>').strip()
			if inp==str(len(result)):
				clear()
				search()
			else:
				try:
					sql.execute(f"SELECT * FROM all_about_food WHERE food = '{result[int(inp)][0]}'")
					print(sql.fetchone())
					pass
				except:
					print('Некорректный ввод ')
					search()
		else:
			sql.execute(f"SELECT * FROM all_about_food WHERE food = '{food}'")
			print(sql.fetchone())
			pass

def start():
	clear()
	global list_food
	list_food=[]
	print('1)Поиск')
	print('2)Составление таблицы')
	inp=input('>>> ').strip()
	if inp=='1': 
		search()
		print('1)Вернуться в меню')
		while True:
			inp=input('>>> ').strip()
			if inp=='1':
				break
			else:
				print('Некорректный ввод ')
	elif inp=='2':
		global boole
		boole=consider_prise()
		main(boole)
	else:
		print('Некорректный ввод ')
		start()

while True:
	start()
