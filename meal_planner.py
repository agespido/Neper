import json
from termcolor import cprint
import random


class Day:
	def __init__(self):
		self.bfast = {}
		self.lunch = {}
		self.dinner = {}
		self.other = {}


def horizontalSeparator():
	print('{}'.format((12+1)*8*'-'))


def row(l):
	if len(l) < 8:
		print('ERROR: Not enough elements (obtained {}, should be {}'.format(len(l), 8))
		return
	print('{:>12}|{:>12}|{:>12}|{:>12}|{:>12}|{:>12}|{:>12}|{:>12}'.format(
		l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7]))


def printWeekMenu(week):
	horizontalSeparator()
	row(['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
	horizontalSeparator()
	list = ['Breakfast']
	for d in week:
		list.append(d.bfast['name'])
	horizontalSeparator()


def main():
	# Open json
	recipes = []
	f = open('.recipes.json', 'r')
	recipes = json.load(f)

	# Meals
	bfast = []
	lunch = []
	dinner = []
	other = []
	for r in recipes:
		if r['type'] == 'Desayuno':
			bfast.append(r)
		elif r['type'] == 'Almuerzo':
			lunch.append(r)
		elif r['type'] == 'Cena':
			dinner.append(r)
		else:
			other.append(r)

	week = []
	for i in range(7):
		d = Day()
		d.bfast = random.choice(bfast)
		d.lunch = random.choice(lunch)
		d.dinner = random.choice(dinner)
		d.other = random.choice(other)
		week.append(d)
	
	print(week[0].bfast)

	printWeekMenu(week)


if __name__ == '__main__':
	main()
