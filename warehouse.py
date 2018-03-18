from __future__ import print_function
import Pyro4
import random

@Pyro4.expose
class Warehouse(object):
	def __init__(self):
		self.contents = [[1, "James Munkres", "9332549532", "Topology", 2015, False ],[2, "Allen Hatcher", "0521795400", "Topology", 2015, False]]

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
			print(id_num)
			if self.contents[id_num][2]==isbn:
				self.contents[id_num][5]=True
# change the status to on load with ISBN
	def status_not(self, isbn):
		for id_num in range(len(self.contents)):
			print(id_num)
			if self.contents[id_num][2]==isbn:
				self.contents[id_num][5]=False
# display all six pieces of information relating to the set of books currently stored
	def display_all(self):
		return list_contents()
# display the subset of books currently stored inclusive year range(e.g. 2000-2010)
	def display_year(self, year1, year2):
		if year1 > year2:
			for id_num in range(len(self.contents)):
				year1=1





def main():
	warehouse = Warehouse()
	Pyro4.Daemon.serveSimple(
		{
			warehouse: "example.warehouse"
		},
		ns=True)


if __name__ == "__main__":
	main()
