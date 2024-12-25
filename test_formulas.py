import unittest
from craft_formulas import CraftFormulas
from skills import CRAFTING_SKILLS

class TestCraftFormulas(unittest.TestCase):
    def setUp(self):
        self.formulas = CraftFormulas()
        
    def test_basic_progress_calculation(self):
        """基本的な進捗計算のテスト"""
        base_progress = 100
        craftsmanship = 2500
        skill = CRAFTING_SKILLS['basic_synthesis']
        
        progress = self.formulas.calculate_progress(
            base_progress,
            craftsmanship,
            skill.progress_rate
        )
        
        self.assertGreater(progress, 0)
        # 具体的な期待値との比較も追加 
        
    def test_quality_calculation(self):
        """品質計算のテスト"""
        base_quality = 100
        control = 2500
        skill = CRAFTING_SKILLS['basic_touch']
        
        # 通常の品質計算
        quality = self.formulas.calculate_quality(
            base_quality,
            control,
            skill.quality_rate
        )
        self.assertGreater(quality, 0)
        
        # インナークワイエット効果込みの計算
        quality_with_iq = self.formulas.calculate_quality(
            base_quality,
            control,
            skill.quality_rate,
            inner_quiet_stacks=5
        )
        self.assertGreater(quality_with_iq, quality)