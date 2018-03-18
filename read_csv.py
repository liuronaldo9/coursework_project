import csv
import sys
import Pyro4
import Pyro4.util
from person import Person

sys.excepthook = Pyro4.util.excepthook

warehouse = Pyro4.Proxy("PYRONAME:example.warehouse")

employee=Person("Employee")

f = open('./tasks.txt', 'r')
try:
	reader = csv.reader(f)
	for row in reader:
		if(row[0] == 'a'):
			del row[0:1]
			print(row)
		elif(row[0] == 'sy'):
			del row[0:1]
			print(row)
		elif(row[0]=='d'):
			employee.display(warehouse)
		elif(row[0]=='si'):
			del row[0:1]
			print(row)
		elif(row[0]=='ol'):
			del row[0:1]
			employee.status_changeon(warehouse, str(row[0]))
		elif(row[0]=='nol'):
			del row[0:1]
			employee.status_changenot(warehouse, str(row[0]))
			
finally:
    f.close()
