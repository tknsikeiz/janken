import unittest
from unittest.mock import patch
import source.janken_main
import source.player
import source.computer
import source.janken_judge

class TestJankenMain(unittest.TestCase):

    @patch('player.player_pon', return_value='グー')
    @patch('computer.computer_pon', return_value='チョキ')
    @patch('janken_judge.judge', return_value='player_win')
    def test_player_wins(self, mock_judge, mock_computer, mock_player):
        with patch('builtins.print') as mock_print:
            source.janken_main.main()
            mock_print.assert_any_call("あなたの勝ちです！")

    @patch('player.player_pon', return_value='グー')
    @patch('computer.computer_pon', return_value='パー')
    @patch('janken_judge.judge', return_value='computer_win')
    def test_computer_wins(self, mock_judge, mock_computer, mock_player):
        with patch('builtins.print') as mock_print:
            source.janken_main.main()
            mock_print.assert_any_call("コンピューターの勝ちです！")

if __name__ == '__main__':
    unittest.main()
