from mrjob.job import MRJob

class MaxDemo(MRJob):

	def mapper(self, key, value):
			yield 1, max(value)

	def reducer(self, key, values):
		print(max(values))
		

if __name__ == '__main__':
	MaxDemo.run()
