import csv
import glob
import json
import re
from termcolor import cprint
import pandas as pd
from modules.recipe_classes import Ingredient, Recipe
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


def write2json(filename: str, data: array):
	with open(filename, 'w') as file:
		serialized = '['
		for rec in data:
			serialized += rec.tojson
			serialized += ','
		serialized = serialized[:-1] + ']'
		file.writelines(serialized)


def csv2dict(fileName) -> array:
	table = []
	rdr = csv.reader(open(fileName, newline=''), delimiter=',', quotechar='"')
	add2table = False
	hdr = []
	recipes = []
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

		if re.match(dateFormat, row[0]):
			cprint( 'DATE: '+ str(row[0]), 'red')

		elif any(s in row[0] for s in meals):
			cprint('MEAL' + str(row[0]), 'yellow')
			if rec is not None and rec.kcal > 0:
				recipes.append(rec)
			rec = Recipe('', str(row[0].lstrip()), [])
			if row[1] not in (None, ''):
				rec.kcal = float(row[1])


		elif row[0].strip()[0].isdigit():
			cprint(row[0], 'blue')
			ing.add_quantity(row[0].lstrip())
			rec.add_ingredient(ing)
		else:
			cprint(row[0], 'green')
			ing = Ingredient(row[0].lstrip())

		row.append('')
		table.append(row)

	return recipes


def main():
	cprint('>> Running fridge organizer', 'green', attrs=['bold'])
	datafiles = glob.glob('data/raw/*.csv')
	recipes = []
	for f in datafiles:
		recipes += csv2dict(f)
	write2json('.recipes.json', recipes)
	cprint('>> Finished!', 'green')


if __name__ == '__main__':
	main()
