
# in-built func...
import os
"""
1. feladat:Írjatok egy olyan programot, ami paraméterként megkap egy listát, amiben stringek vannak
és visszaadja a 2. leghosszabb stringet.
A feladat során kezeljétek le az esetleges hiba eseteket
"""
def the_second_longest_string_in_list(list):
	if len(list) <= 1:
		print("Your list does NOT have enough item!!!")
		pass
	else:
		temporary = []
		for item in list:
			temporary.append(item)

		temp = sorted(temporary, key=len, reverse=True)
		return temp[1]

"""
2. feladat: Írjatok egy olyan programot, amely paraméterben megkap egy mondatot és eldönti róla, hogy
az palindrome szöveg. Palindrome fogalma: visszafelé olvasva ugyan azt kapod, mint elölrő olvasva.
Példa: Indul a görög aludni.
"""
def palidrome_validator(sentence):
	print(sentence)
	if str(sentence).isdigit() is True:
		print("The palindrome is NOT a number!")
	else:
		temp = [item.lower() for item in sentence if item.isalpha()]
		print(temp)
		if temp[::-1] == temp:
			print("The sentence is a PALIDROME!")
		else:
			print("The sentence is NOT a PALIDROME!")

"""
3. feladat: A megadott dictionary-ből gyűjtsétek ki az össze kulcsát.
"""

def keys(dict):
	keys = []
	for k, v in dict.items():
		keys.append(k)
		for kv, vv in v.items():
			keys.append(kv)
			for kvv, vvv in vv.items():
				keys.append(kvv)
	print(keys)


"""
-----------------------------------------------
4. feladat: Írjatok egy olyan programot, amely egy paraméterben megkap egy
elérési útvonalat és ha létezik az útvonal, akkor felolvassa a tartalmát,
ha nem létezik, akkor létrehozza a file-t a következő tartalommal:
{"kulcs": "érték"}

A feladat során kezeljétek le az esetleges hibákat.
"""
def write_data(f_path):

	data = {"key": "value"}
	anable_file_type_list = ['.json', '.txt', '.csv']

	if os.path.exists(f_path):
		if not os.path.isfile(f_path):
			raise ValueError("It is NOT a file path!")

		with open(f_path, "r", encoding="utf-8") as f:
			data = f.read()
		print(data)
		return data

	else:
		if f_path[-5:] not in anable_file_type_list:
			raise ValueError("It is NOT a file path!")

		import json
		with open(f_path, "w", encoding="utf-8") as f:
			json.dump(data, f, ensure_ascii=False)
"""
-----------------------------------------------
5. feladat: Írjatok egy olyan kódot, amely paraméterben megkap 1 számot
és ennek megfelelő hosszúságú jelszót generál a program.

- MAGAMTÓL NEM TUDOK HOZZÁSZOLNI -:) ÍGY EZT SKIPPELTEM...
-----------------------------------------------
"""
if __name__ == '__main__':

	# 1.st Task:
	my_list = ['alma', 'dinnye', 'vitéz_nagynányai_horty_miklós_matróza_vagyok', 'Elkelkáposztáshatatlaságoskodásoskodásaitokért', 'valami']

	print(the_second_longest_string_in_list(list = my_list))
	# -------------------------------------------------------------------------

	# 2nd. Task:
	test_sentence = 'Indul a Görög aludni!'
	palidrome_validator(sentence = test_sentence)
	# -------------------------------------------------------------------------

	# 3nd. Task:
	athletics = {
		'100m': {
			'Men': {
				'Gold': 'Marcell Jacobs',
				'Silver': 'Fred Kerley',
				'Bronze': 'Andre De Grasse'
			},
			'Women': {
				'Gold': 'Elaine Thompson-Herah',
				'Silver': 'Shelly-Ann Fraser-Pryce',
				'Bronze': 'Shericka Jackson'
			}
		}
	}
	keys(dict = athletics)
	# ---------------------------------------------------------------------------

	file_name = "examination.txt"
	f_path = f"{os.path.dirname(__file__)}\\{file_name}"
	print(f_path)
	write_data(f_path)
