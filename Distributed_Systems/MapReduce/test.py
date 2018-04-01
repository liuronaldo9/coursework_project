from mrjob.job import MRJob

class MaxDemo(MRJob):

	def mapper(self, key, value):
		total=0
		totalnum=0
		value.replace(',','')
		for i in value:
			if i != ',':
				total=int(i)+total
				totalnum +=1
		yield totalnum, total
		print(totalnum)
		print(total)

	def reducer(self, totalnum, total):
		print(totalnum)
		print(total)


if __name__ == '__main__':
	MaxDemo.run()
