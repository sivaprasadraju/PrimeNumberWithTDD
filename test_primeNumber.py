#this program will check for prime nos.
import unittest
import pytest
from main import *

class PrimeNumberTests(unittest.TestCase):
	
		def test_NotPrimeNumber(self):
        		self.assertFalse(prime_number(4))
		
		def test_PrimeNumber(self):
        		self.assertTrue(prime_number(2))
			
		def test_PrimeNumberTestForZero(self):
        		self.assertFalse(prime_number(0))
				
		def test_negative(self):
        		with pytest.raises(ValueError):
            			prime_number(-1)
