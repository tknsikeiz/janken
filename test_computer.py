import unittest
from unittest.mock import patch
from source.computer import computer_pon 

class TestComputerPon(unittest.TestCase):
    
    @patch('random.choice', return_value='グー')
    def test_random_choice_1(self, mock_random_choice):
        self.assertEqual(computer_pon(), 'グー')

    @patch('random.choice', return_value='チョキ')
    def test_random_choice_2(self, mock_random_choice):
        self.assertEqual(computer_pon(), 'チョキ')

    @patch('random.choice', return_value='パー')
    def test_random_choice_3(self, mock_random_choice):
        self.assertEqual(computer_pon(), 'パー')

if __name__ == '__main__':
    unittest.main()
