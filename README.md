# FRIDGE_ORGANIZER.PY
## Introduction

This script takes the data from the CSV files exported from Fatsecret app
and it writes a YAML file with all the different meals, its ingredients
and its nutritional informatio.

### YAML data format:
```
[
	- recipe:
		- name:
		- id:
		- meal: breakfast/lunch/dinner/other
		- nutritional_info:
		- kcal:
		- ch:
		- protein:
		- fat:
		- sugar:
		- fiber:
		etc.
		- ingredients:{
			- ingredient:
			- weight:
			- kcal:
			- ch:
			- protein:
			- fat:
			- sugar:
			- fiber:
			etc.
				- ingredient: 
					(...)
		},
	- recipe:
		(...)
]
```

## References:
https://github.com/jrnold/fatsecretExporter/blob/master/fatsecretExport.py

https://pypi.org/project/fatsecret/