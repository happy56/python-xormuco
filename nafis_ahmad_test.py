import unittest
import a,b,c

class Ntest(unittest.TestCase):

	def test_a(self):
		self.assertEqual(a.does_overlaps( (1, 5), (2, 6)), True, "Overlaping ... ")
		self.assertEqual(a.does_overlaps( (1, 5), (6, 8)), False, "Not Overlaping ... ")
		self.assertEqual(a.does_overlaps( (2, 6), (1, 5)), True, "Overlaping ... ")
	
	def test_b(self):
		self.assertEqual(b.compa('1.1', '1.2'), 'less')
		self.assertEqual(b.compa('1.1.2.0', '1.1.2.0.1'), 'less')
		self.assertEqual(b.compa('1.1.2.9', '1.1.2'), 'greater')
		self.assertEqual(b.compa('2', '1.1.2.0.1'), 'greater')
		self.assertEqual(b.compa('2', '2.0.0.0.0'), 'equal')
		self.assertEqual(b.compa('30', '2.1.2.0.1'), 'greater')
		self.assertEqual(b.compa('8.04.84', '1.1.2.0.1'), 'greater')
		
	def test_c_sum(self):
		import time
	

		

		# print sum([6, 22])
		# print hello('nafis')
		c.CACHE_LIFE_TIME_IN_SEC = 2
		
		self.assertEqual(c.ncache(sum, [6, 22, 9, 121]), 158, 'no chaching / init ');
		self.assertEqual(c.ncache(sum, [6, 22, 9, 121]), 158, 'chached ... ');
		time.sleep(3)
		self.assertEqual(c.ncache(sum, [6, 22, 9, 121]), 158, 'No chached ... ');
		self.assertEqual(c.ncache(sum, [6, 22, 9, 121]), 158, 'chached ... ');
		
	def test_c_hello(self):

		def hello(name):
			return 'hello ' + name + ' !!' 

		c.CACHE_LIFE_TIME_IN_SEC = 2

		self.assertEqual(c.ncache(hello, 'nafis'), 'hello nafis !!', 'init / not Caching ... ');
		self.assertEqual(c.ncache(hello, 'nafis'), 'hello nafis !!', 'Caching ... ');
		self.assertEqual(c.ncache(hello, 'Doremon'), 'hello Doremon !!', 'diffrent value ... ');
		
		





if __name__ == '__main__':
	unittest.main()