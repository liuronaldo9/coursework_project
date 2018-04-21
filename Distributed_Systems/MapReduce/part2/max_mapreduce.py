from mrjob.job import MRJob



class MaxDemo(MRJob):

	def mapper(self, key, value):
		value=value.split(',')
		value=[float(i) for i in value]
		yield "MAX:", max(value)

	def reducer(self, key, values):
		yield "MAX:", max(values)

if __name__ == '__main__':
	MaxDemo.run()
