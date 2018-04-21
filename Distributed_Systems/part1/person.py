from __future__ import print_function
import sys
import csv

if sys.version_info < (3, 0):
	input = raw_input


class Person(object):
	def __init__(self, name):
		self.name = name

# read the tasks.txt file to find command and run program

	def visit(self, warehouse):
		print("This is {0}.".format(self.name)+'\n')
		f = open('./tasks.txt', 'r')
		try:
			reader = csv.reader(f)
			for row in reader:
				if(row[0] == 'a'):# add a book
					if len(row)!=5:
						print("the command length error, MUST input four variable"+'\n')
					else:
						del row[0:1]
						try:
							self.addbook(warehouse, str(row[0]), str(row[1]), str(row[2]), int(row[3]))
						except ValueError:
							print("Please check your year, it must be an integer"+'\n')
				elif(row[0] == 'sy'):
					if len(row)!=3:
						print("the command length error, MUST input two variable"+'\n')
					else:
						del row[0:1]
						try:
							if int(row[0])<=int(row[1]):
								self.display_3(warehouse, int(row[0]), int(row[1]))
							else:
								print("Please check your year, the year1 must be greater than year2")
						except ValueError:
							print("Please check your year, it must be an integer"+'\n')
				elif(row[0]=='d'):
					if len(row)!=1:
						print("command length error, MUST input zero variable"+'\n')
					else:
						self.display(warehouse)
				elif(row[0]=='si'):
					if len(row)!=2:
						print("command length error, MUST input one variable"+'\n')
					else:
						del row[0:1]
						self.display_4(warehouse, str(row[0]))
				elif(row[0]=='ol'):
					if len(row)!=2:
						print("command length error, MUST input one variable"+'\n')
					else:
						del row[0:1]
						self.status_changeon(warehouse, str(row[0]))
				elif(row[0]=='nol'):
					if len(row)!=2:
						print("command length error, MUST input one variable"+'\n')
					else:
						del row[0:1]
						self.status_changenot(warehouse, str(row[0]))
				else:
					print("Error due to connot find command {0} ".format(",".join(row[0])))
		finally:
			f.close()


# display all information
	def display(self, warehouse):
		print("{0} is displaying all information from library:".format(self.name))
		if warehouse.list_contents():
			print("The warehouse contains:"+'\n', warehouse.list_contents(),'\n')
		else:
			print("Sorry, cannot find any books\n")


# change the status to on load and display all information
	def status_changeon(self, warehouse, isbn):
		print("{0} is changing the status to on load, the ISBN is {1}\n".format(self.name,isbn))
		warehouse.status_on(self.name,isbn)


# change the status to not on load and display all information
	def status_changenot(self, warehouse, isbn):
		print("{0} is changing the status to not on load, the ISBN is {1}\n".format(self.name,isbn))
		warehouse.status_not(self.name,isbn)


# display the subset of books currently stored based on year range(2000-2010)
	def display_3(self, warehouse, year1, year2):
		print("{0} is querying the subset of books based on year range:".format(self.name))
		result=warehouse.display_year(self.name,year1, year2)
		if result:
			print("The warehouse subset contains based on Year of Publication:"+'\n', result,'\n')
		else:
			print("we cannot find the books"+'\n')


# display the subset of books currently stored based on ISBN
	def display_4(self, warehouse, isbn):
		print("{0} is querying the subset of books based on ISBN:".format(self.name))
		result=warehouse.display_isbn(self.name,isbn)
		if result:
			print("The warehouse subset contains based on ISBN:"+'\n', result,'\n')
		else:
			print("we cannot find the books"+'\n')


# add a book
	def addbook(self, warehouse, author, isbn, title, year):
		print("{0} is adding a book:".format(self.name))
		print("your unique id is",warehouse.add_book(self.name,author, isbn, title, year))
		print("you have add a book successfully\n")

