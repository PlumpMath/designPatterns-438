import unittest
import math

class TestCase(unittest.TestCase):
	def testNeg(self):
		prog = Programa()
		prog.verificaN(-3)
		self.assertFalse(self.result)

class Programa():
	def __init__(self, n):
		if n <= 0:
			self.result = False
		else:
			self.result = [True] * n

__name__ == "__main__"

# 1: [True]
# 2: [True, False]
# 3: [True, False, False]
# 4: [True, False, False, True]
# 5: [True, False, False, True, False]
# 6: [True, False, False, True, False, False]
# 7: [True, False, False, True, False, False, False]
# 8: [True, False, False, True, False, False, False, False]

