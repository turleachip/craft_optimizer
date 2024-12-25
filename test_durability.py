import unittest
from durability_manager import DurabilityManager
from buff_manager import Buff

class TestDurabilityManager(unittest.TestCase):
    def setUp(self):
        self.durability_manager = DurabilityManager(40)  # 初期耐久度40
    
    def test_basic_consumption(self):
        """基本的な耐久度消費のテスト"""
        cost = self.durability_manager.calculate_consumption(10, [])
        self.assertEqual(cost, 10)
        
        self.durability_manager.consume(cost)
        self.assertEqual(self.durability_manager.state.current, 30)
    
    def test_waste_not_effect(self):
        """倹約効果のテスト"""
        waste_not_buff = Buff("倹約", 4, durability_buff=-0.5)
        cost = self.durability_manager.calculate_consumption(10, [waste_not_buff])
        self.assertEqual(cost, 5)
    
    def test_repair(self):
        """耐久度回復のテスト"""
        self.durability_manager.consume(10)
        self.durability_manager.repair(5)
        self.assertEqual(self.durability_manager.state.current, 35) 