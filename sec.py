import sqlite3
import config
import vk_api


vk_session = vk_api.VkApi(token=config.token)
api = vk_session.get_api()
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



api.messages.send(user_id = 439720761 , message= 'Программа закончила', v="5.38" )
