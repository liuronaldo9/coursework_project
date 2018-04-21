from mrjob.job import MRJob

class MeanDemo(MRJob):

	def mapper(self, key, value):
		key="Mean:"
		total=0
		totalnum=0
		value=value.split(',')
		for i in value:
			if i != ',':
				total=float(i)+total
				totalnum +=1
		#print(total,totalnum)
		yield key,(total,totalnum)

	def reducer(self, key, values):
		total=0
		totalum=0		
		for i in values:
			total += i[0]
			totalum +=i[1]
		yield key, total/totalum

if __name__ == '__main__':
	MeanDemo.run()
