from mrjob.job import MRJob

class MaxDemo(MRJob):

	def mapper(self, key, value):
		total=0
		value.replace(',','')
		print(value)
		for i in value:
			if i == ",":
				continue
			total=int(i)+total
		yield 1, total

	def reducer(self, key, values):
		totalL,totalW=0,0		
		for i in values:
			totalL +=1
			totalW +=1
		print(totalL)
		print(sum(values))

if __name__ == '__main__':
	MaxDemo.run()
