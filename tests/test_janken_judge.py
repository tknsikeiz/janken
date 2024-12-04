import unittest
from source.janken_judge import judge  # judge関数をインポート

class TestJankenJudge(unittest.TestCase):

    def test_judge(self):
        # 各テストケースに対して、player_hand と computer_hand の組み合わせで結果をテスト
        test_cases = [
            # あいこ
            ('グー', 'グー', 'draw'),
            ('チョキ', 'チョキ', 'draw'),
            ('パー', 'パー', 'draw'),
            
            # プレイヤー勝ち
            ('グー', 'チョキ', 'player_win'),
            ('チョキ', 'パー', 'player_win'),
            ('パー', 'グー', 'player_win'),
            
            # コンピューター勝ち
            ('グー', 'パー', 'computer_win'),
            ('チョキ', 'グー', 'computer_win'),
            ('パー', 'チョキ', 'computer_win')
        ]

        # 各組み合わせについてテスト
        for player_hand, computer_hand, expected_result in test_cases:
            with self.subTest(player_hand=player_hand, computer_hand=computer_hand):
                result = judge(computer_hand, player_hand)  # judge関数を呼び出す
                self.assertEqual(result, expected_result)  # 結果が期待通りか確認

if __name__ == '__main__':
    unittest.main()
