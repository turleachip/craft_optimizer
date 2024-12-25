import unittest
from craft_optimizer import CraftOptimizer
from skills import CRAFTING_SKILLS

class TestBaseEfficiency(unittest.TestCase):
    def setUp(self):
        self.optimizer = CraftOptimizer(
            recipe_level=90,
            craftsmanship=3200,
            control=3100,
            cp=600
        )
    
    def test_efficiency_calculation(self):
        """効率100あたりの作業/品質値の計算テスト"""
        # 作業効率のテスト
        basic_synthesis = CRAFTING_SKILLS['basic_synthesis']
        progress = self.optimizer.calculate_progress(basic_synthesis)
        self.assertGreater(progress, 0)
        
        # 加工効率のテスト
        basic_touch = CRAFTING_SKILLS['basic_touch']
        quality = self.optimizer.calculate_quality(basic_touch)
        self.assertGreater(quality, 0)

if __name__ == '__main__':
    unittest.main() 