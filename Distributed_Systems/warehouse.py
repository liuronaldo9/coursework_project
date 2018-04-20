from __future__ import print_function
import Pyro4

@Pyro4.expose
class Warehouse(object):
	def __init__(self):
		self.contents = []

	def list_contents(self):
		return self.contents


# change the status to on load with ISBN
	def status_on(self,name, isbn):
		for id_num in range(len(self.contents)):
			if self.contents[id_num][2]==isbn:
				self.contents[id_num][5]=False
		print("{0} change the status to on load with ISBN, the isbn is {1}".format(name,isbn))


# change the status to not on load with ISBN
	def status_not(self,name, isbn):
		for id_num in range(len(self.contents)):
			if self.contents[id_num][2]==isbn:
				self.contents[id_num][5]=True
		print("{0} change the status to not on load with ISBN, the isbn is {1}".format(name,isbn))


# display all six pieces of information relating to the set of books currently stored
	def display_all(self,name):
		return list_contents()


# display the subset of books currently stored based on year range(e.g. 2000-2010)
	def display_year(self,name, year1, year2):
		subset=[]
		for id_num in range(len(self.contents)):
			if self.contents[id_num][4]>= year1 and self.contents[id_num][4]<= year2:
				subset.append(self.contents[id_num])
		print("{0} search books based on year, the year {1} - year {2}".format(name,year1,year2))
		return subset


# display the subset of books currently stored based on ISBN
	def display_isbn(self,name, isbn):
		subset=[]
		for id_num in range(len(self.contents)):
			if self.contents[id_num][2]==isbn:
				subset.append(self.contents[id_num])
		print("{0} search books based on ISBN, the isbn is {1}".format(name,isbn))
		return subset


# add a book
	def add_book(self,name, author, isbn, title, year):
		unique_id=len(self.contents)
		subset=[unique_id, author, isbn, title, year, True]
		self.contents.append(subset)
		print("{0} add a book, the unique id is {1}".format(name,unique_id))
		return unique_id


def main():
	warehouse = Warehouse()
	Pyro4.Daemon.serveSimple(
		{
			warehouse: "example.warehouse"
		},
		ns=True)


if __name__ == "__main__":
	main()
