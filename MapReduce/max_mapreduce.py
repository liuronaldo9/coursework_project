from mrjob.job import MRJob

class MaxDemo(MRJob):

	def mapper(self, key, value):
			yield 0, max(value)

	def reducer(self, key, values):
		yield 0, max(values)
		

if __name__ == '__main__':
	MaxDemo.run()
