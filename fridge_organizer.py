import csv
import glob
import json
import re
from termcolor import cprint
import pandas as pd

begin = 'Fecha'
end = 'Total'
dateFormat = r"(.*\D),(.*\D) (.\d),(.*\d)"
meals = ['Desayuno', 'Almuerzo', 'Cena', 'Pasa Bocas / Otros']

def getRecipe():
	pass


def getIngeredients():
	pass


def csv2dict(fileName):
	table = []
	rdr = csv.reader(open(fileName, newline=''), delimiter=',', quotechar='"')
	add2table = False
	hdr = []
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

		if not re.match(dateFormat, row[0]):
			cprint(row[0], 'red')
		row.append('')
		table.append(row)

	df = pd.DataFrame(table, columns=hdr)
	print(df)
	df.to_json(r'exported_data.json')



def main():
	cprint('>> Running fridge organizer', 'green', attrs=['bold'])
	datafiles = glob.glob('data/raw/*.csv')
	for f in datafiles:
		csv2dict(f)


if __name__ == '__main__':
	main()
