'''
	Tests the method in the VectorizeTxt class
'''
import unittest
from VectorizeTxt import extractFeatures


class IsFiltered(unittest.TestCase):
	#def testOne(self):
	#	self.failUnless(filter('laksjflaksdjfldsajfdslfj'))
	def testTwo(self):
		self.failUnless(extractFeatures('hello'))

def main():
    unittest.main()

if __name__ == '__main__':
    main()