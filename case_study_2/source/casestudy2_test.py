import random
import unittest
import xmlrunner
from case_study2 import randomPhrase 

class TestGeneratePhrase(unittest.TestCase):

    def setUp(self):
        self.seq1 = tuple('buz'+str(i) for i in range(1,6))
        self.seq2 = tuple('adj'+str(i) for i in range(1,6))
        self.seq3 = tuple('adv'+str(i) for i in range(1,6))
        self.seq4 = tuple('verb'+str(i) for i in range(1,6))

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq1, 20)
            random.sample(self.seq2, 20)
            random.sample(self.seq3, 20)
            random.sample(self.seq4, 20)            
        for element in random.sample(self.seq1, 2):
            self.assertTrue(element in self.seq1)
        for element in random.sample(self.seq2, 1):
            self.assertTrue(element in self.seq2)
        for element in random.sample(self.seq3, 1):
            self.assertTrue(element in self.seq3)
        for element in random.sample(self.seq4, 1):
            self.assertTrue(element in self.seq4)

    def test_randomPhrase(self):
        count = 0
        res = randomPhrase(self.seq1,self.seq2,self.seq3,self.seq4)
        for element in self.seq1:
            if(element in res):
                count = count + 1
        for element in self.seq2:
            if(element in res):
                count = count + 1
        for element in self.seq3:
            if(element in res):
                count = count + 1
        for element in self.seq4:
            if(element in res):
                count = count + 1
        self.assertEqual(count,5)

if __name__ == "__main__":
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False, buffer=False, catchbreak=False)
        
        
        
