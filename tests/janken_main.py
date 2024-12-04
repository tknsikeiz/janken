import unittest
from unittest.mock import patch
from source.janken_main import play_round, update_score, display_final_result

class TestJankenMain(unittest.TestCase):

    @patch('source.computer.computer_pon', return_value='グー')
    @patch('source.player.player_pon', return_value='チョキ')
    @patch('source.janken_judge.judge', return_value='computer_win')
    def test_play_round(self, mock_judge, mock_player_pon, mock_computer_pon):
        result, computer_hand, player_hand = play_round(1)
        self.assertEqual(result, 'computer_win')
        self.assertEqual(computer_hand, 'グー')
        self.assertEqual(player_hand, 'チョキ')

    def test_update_score(self):
        player_win, computer_win = update_score('player_win', 0, 0)
        self.assertEqual(player_win, 1)
        self.assertEqual(computer_win, 0)

    @patch('builtins.print')
    def test_display_final_result(self, mock_print):
        display_final_result(2, 1)
        mock_print.assert_any_call("あなたの総合勝利です！")

if __name__ == '__main__':
    unittest.main()
