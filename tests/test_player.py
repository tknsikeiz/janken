import unittest
from unittest.mock import patch

from source.player import player_pon

class TestPlayerPon(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_input_1(self, mock_input):
        self.assertEqual(player_pon(), 'グー')

    @patch('builtins.input', return_value='2')
    def test_input_2(self, mock_input):
        self.assertEqual(player_pon(), 'チョキ')

    @patch('builtins.input', return_value='3')
    def test_input_3(self, mock_input):
        self.assertEqual(player_pon(), 'パー')

    @patch('builtins.input', side_effect=['0', '1'])
    def test_invalid_input_0(self, mock_input):
        self.assertEqual(player_pon(), 'グー')  

    @patch('builtins.input', side_effect=['4', '2'])
    def test_invalid_input_4(self, mock_input):
        self.assertEqual(player_pon(), 'チョキ') 

if __name__ == '__main__':
    unittest.main()
