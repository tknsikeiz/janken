import unittest
from source.janken_judge import judge 

class TestJankenJudge(unittest.TestCase):

    def test_judge(self):
        test_cases = [
            ('グー', 'グー', 'draw'),
            ('チョキ', 'チョキ', 'draw'),
            ('パー', 'パー', 'draw'),
            
            ('グー', 'チョキ', 'player_win'),
            ('チョキ', 'パー', 'player_win'),
            ('パー', 'グー', 'player_win'),
            
            ('グー', 'パー', 'computer_win'),
            ('チョキ', 'グー', 'computer_win'),
            ('パー', 'チョキ', 'computer_win')
        ]

        for player_hand, computer_hand, expected_result in test_cases:
            with self.subTest(player_hand=player_hand, computer_hand=computer_hand):
                result = judge(computer_hand, player_hand) 
                self.assertEqual(result, expected_result)  
if __name__ == '__main__':
    unittest.main()
