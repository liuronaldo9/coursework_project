from mrjob.job import MRJob
import csv
import numpy as np
def csv_readline(line):
	for row in csv.reader([line]):
		return row

class MeanDemo(MRJob):

	def mapper(self, line_no, line):
		cell = csv_readline(line)
		total=0
		for w in cell:
			total = int(w)+total
			yield 1, total

	def reducer(self, row, values):
		totalrow=0
		for i in row:
			totalrow+=1
		
		print(np.mean(values))
        
if __name__ == '__main__':
	MeanDemo.run()
