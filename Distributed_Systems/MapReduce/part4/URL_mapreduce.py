from mrjob.job import MRJob

class UrlDemo(MRJob):
	
	def mapper(self, key, value):
		mylist=value.split(',')
		yield 0, mylist

	def reducer(self, key, values):
		fcolumn=[]
		scolumn=[]
		for i in values:
			fcolumn.append(i[0])
			scolumn.append(i[1])

		for i in range(len(fcolumn)):
			for j in range(len(scolumn)):
				if i != j:
					if fcolumn[i] == scolumn[j]:
						yield 0, (fcolumn[j],scolumn[j],scolumn[i])

if __name__ == '__main__':
	UrlDemo.run()
