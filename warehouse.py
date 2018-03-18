from __future__ import print_function
import Pyro4
import random

@Pyro4.expose
class Warehouse(object):
	def __init__(self):
		self.contents = [[0, "James Munkres", "9332549532", "Topology", 2014, True ],[1, "Allen Hatcher", "0521795400", "Topology", 2001, True]]

	def uniqueid():
		seed=random.getrandbits(32)
		while True:
			yield seed
			seed+=1
	def list_contents(self):
		return self.contents
# change the status to on load with ISBN
	def status_on(self, isbn):
		for id_num in range(len(self.contents)):
			if self.contents[id_num][2]==isbn:
				self.contents[id_num][5]=False
# change the status to not on load with ISBN
	def status_not(self, isbn):
		for id_num in range(len(self.contents)):
			if self.contents[id_num][2]==isbn:
				self.contents[id_num][5]=True
# display all six pieces of information relating to the set of books currently stored
	def display_all(self):
		return list_contents()
# display the subset of books currently stored based on year range(e.g. 2000-2010)
	def display_year(self, year1, year2):
		subset=[]
		if year1<= year2:
			for id_num in range(len(self.contents)):
				if self.contents[id_num][4]>= year1 and self.contents[id_num][4]<= year2:
					subset.append(self.contents[id_num])
		return subset
# display the subset of books currently stored based on ISBN
	def display_isbn(self, isbn):
		subset=[]
		for id_num in range(len(self.contents)):
			if self.contents[id_num][2]==isbn:
				subset.append(self.contents[id_num])
		return subset

# add a book
	def add_book(self, author, isbn, title, year):
		unique_id=len(self.contents)
		subset=[unique_id, author, isbn, title, year, True]
		self.contents.append(subset)


def main():
	warehouse = Warehouse()
	Pyro4.Daemon.serveSimple(
		{
			warehouse: "example.warehouse"
		},
		ns=True)


if __name__ == "__main__":
	main()
