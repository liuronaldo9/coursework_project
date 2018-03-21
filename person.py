from __future__ import print_function
import sys
import csv

if sys.version_info < (3, 0):
	input = raw_input


class Person(object):
	def __init__(self, name):
		self.name = name

	def visit(self, warehouse):
		print("This is {0}.".format(self.name))
		print('\n')
		f = open('./tasks.txt', 'r')
		try:
			reader = csv.reader(f)
			for row in reader:
				if(row[0] == 'a'):# add a book
					del row[0:1]
					self.addbook(warehouse, str(row[0]), str(row[1]), str(row[2]), int(row[3]))
				elif(row[0] == 'sy'):
					del row[0:1]
					self.display_3(warehouse, int(row[0]), int(row[1]))
				elif(row[0]=='d'):
					self.display(warehouse)
				elif(row[0]=='si'):
					del row[0:1]
					self.display_4(warehouse, str(row[0]))
				elif(row[0]=='ol'):
					del row[0:1]
					self.status_changeon(warehouse, str(row[0]))
				elif(row[0]=='nol'):
					del row[0:1]
					self.status_changenot(warehouse, str(row[0]))
					
		finally:
		    f.close()


# display all information
	def display(self, warehouse):
		print("The warehouse contains:"+'\n', warehouse.list_contents())
		print('\n')
# change the status to on load and display all information
	def status_changeon(self, warehouse, isbn):
		warehouse.status_on(isbn)

# change the status to not on load and display all information
	def status_changenot(self, warehouse, isbn):
		warehouse.status_not(isbn)

# display the subset of books currently stored based on year range(2000-2010)
	def display_3(self, warehouse, year1, year2):
		print("The warehouse subset contains based on Year of Publication:"+'\n', warehouse.display_year(year1, year2))
		print('\n')
# display the subset of books currently stored based on ISBN
	def display_4(self, warehouse, isbn):
		print("The warehouse subset contains based on ISBN:"+'\n', warehouse.display_isbn(isbn))
		print('\n')
# add a book
	def addbook(self, warehouse, author, isbn, title, year):
		print("you have add a book successfully")
		print("your unique id is",warehouse.add_book(author, isbn, title, year))
		print('\n')