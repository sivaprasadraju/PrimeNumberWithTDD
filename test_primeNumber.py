import unittest
import pytest
from main import *

class PrimeNumberTests(unittest.TestCase):
	
		def test_NotPrimeNumber(self):
        		self.assertFalse(prime_number(4))