import sqlite3
import config

def main()
	f=int()

	db=sqlite3.connect('food.db')
	sql= db.cursor()

	sql.execute("""CREATE TABLE IF NOT EXISTS all_about_food (
		food TEXT,
		calories INTEGER,
		Protein INTEGER,
		Fats INTEGER,
		Carbohydrates INTEGER	
	)""")
	db.commit()



	Food_calories=config.Food_calories
	for i in Food_calories:
		for w in i:
			f+=1
			sql.execute(f"INSERT INTO all_about_food VALUES (?, ?, ?, ?, ?)",(w['food'].lower(),w['calories'],w['Protein'],w['Fats'],w['Carbohydrates']))
			print(str(str(w['food'])+' '+str(f)))
			db.commit()


if int(input("Перезапись таблицы(1/0)"))==1:
	main()
