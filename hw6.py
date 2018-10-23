import re
import unittest

def sumNums(fileName):
    inFile = open(fileName, 'r')
    lines = inFile.read()
    numbers = []
    findNumber = re.findall('[0-9]+', lines)
    #print(findNumber)
    numbers = [int(nums) for nums in findNumber]
    amount = sum(numbers)
    return amount

def countWord(fileName, word):
    inFile = open(fileName, "r")
    lines = inFile.read() 
    findWord = []
    file = lines.strip()
    findWord = re.findall(word+('\\b'), file, re.IGNORECASE)
    #print(findWord)
    total = len(findWord)
    print(total)
    return total

def listURLs(fileName):
    inFile = open(fileName, "r")
    lines = inFile.read()
    findURL = []
    findURL = re.findall('www.', lines)
    #print(findURL)
    return findURL

class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
