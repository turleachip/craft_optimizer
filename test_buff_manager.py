import unittest
from buff_manager import BuffManager

class TestBuffManager(unittest.TestCase):
    def setUp(self):
        self.buff_manager = BuffManager()
    
    def test_buff_application(self):
        """バフの適用テスト"""
        self.buff_manager.add_buff("ヴェネレーション", 4, progress_buff=0.5)
        progress, quality, durability = self.buff_manager.get_total_buffs()
        self.assertEqual(progress, 0.5)
    
    def test_buff_duration(self):
        """バフの持続時間テスト"""
        self.buff_manager.add_buff("イノベーション", 4, quality_buff=0.5)
        self.buff_manager.tick_buffs()
        self.assertTrue("イノベーション" in self.buff_manager.active_buffs)
        
        # 4ターン経過
        for _ in range(4):
            self.buff_manager.tick_buffs()
        self.assertFalse("イノベーション" in self.buff_manager.active_buffs) 