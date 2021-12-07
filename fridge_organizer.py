import csv
import glob
import json
import re
from termcolor import cprint
import pandas as pd
from modules.receipt_classes import Ingredient, Recipe
import array

begin = 'Fecha'
end = 'Total'
dateFormat = r"(.*\D),(.*\D) (.\d),(.*\d)"
qtyFormat = r"(.\d*)"
meals = ['Desayuno', 'Almuerzo', 'Cena', 'Pasa Bocas / Otros']

def getRecipe():
	pass


def getIngeredients():
	pass


def write2json(data: array):
	with open("Dataset.json", 'w') as file:
		for rec in data:
			serialized = rec.tojson
			json.dump(serialized, file)


def csv2dict(fileName) -> array:
	table = []
	rdr = csv.reader(open(fileName, newline=''), delimiter=',', quotechar='"')
	dict = csv.DictReader(fileName, delimiter=',')
	add2table = False
	hdr = []
	recipies = []
	rec = None
	ing = None
	for row in rdr:
		if not row:
			continue

		# Skip the summary at the begining of the input file.
		if begin in row:
			add2table = True
			# Get the header information
			hdr = [c.replace(' ', '') for c in row]
			hdr.append('Cant')

		if not add2table:
			continue

#		if not re.match(dateFormat, row[0]) and not any(s in row[0] for s in meals):
#			cprint(row[0], 'red')

		if re.match(dateFormat, row[0]):
			cprint( 'DATE: '+ str(row[0]), 'red')

		elif any(s in row[0] for s in meals):
			cprint('MEAL' + str(row[0]), 'yellow')
			if rec is not None:
				recipies.append(rec)
			rec = Recipe()
			rec.type = str(row[0])
			rec.ingredients = []
			if row[1] not in (None, ''):
				rec.kcal = float(row[1])

		elif row[0].strip()[0].isdigit():
			cprint(row[0], 'blue')
			ing.quantity = row[0]
			rec.ingredients.append(ing)
		else:
			cprint(row[0], 'green')
			ing = Ingredient()
			ing.name = row[0]



		row.append('')
		table.append(row)

	df = pd.DataFrame(table, columns=hdr)
	print(df)
	df.to_json(r'exported_data.json')
	return recipies


def main():
	cprint('>> Running fridge organizer', 'green', attrs=['bold'])
	datafiles = glob.glob('data/raw/*.csv')
	recipies = []
	for f in datafiles:
		recipies += csv2dict(f)
	write2json(recipies)
	print("Finished!")


if __name__ == '__main__':
	main()
