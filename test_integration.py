import unittest
from craft_optimizer import CraftOptimizer
from skills import CRAFTING_SKILLS

class TestCraftingIntegration(unittest.TestCase):
    def setUp(self):
        # レベル90装備製作を想定したパラメータ
        self.optimizer = CraftOptimizer(
            recipe_level=90,
            craftsmanship=3200,
            control=3100,
            cp=600
        )
        self.optimizer.durability_manager.state.current = 70  # 初期耐久度設定
    
    def test_basic_synthesis_combo(self):
        """基本的な作業コンボのテスト"""
        # ヴェネレーション → 作業
        veneration = CRAFTING_SKILLS['veneration']
        basic_synthesis = CRAFTING_SKILLS['basic_synthesis']
        
        # ヴェネレーション使用
        success = self.optimizer.apply_skill(veneration)
        self.assertTrue(success)
        
        # 作業実行（ヴェネレーション効果込み）
        success = self.optimizer.apply_skill(basic_synthesis)
        self.assertTrue(success)
    
    def test_quality_improvement_combo(self):
        """品質向上コンボのテスト"""
        # イノベーション → 上級加工
        innovation = CRAFTING_SKILLS['innovation']
        advanced_touch = CRAFTING_SKILLS['advanced_touch']
        
        # インナークワイエットは最初から付与されているとする
        self.optimizer.buff_manager.inner_quiet_stacks = 5
        
        # イノベーション使用
        success = self.optimizer.apply_skill(innovation)
        self.assertTrue(success)
        
        # 上級加工実行
        success = self.optimizer.apply_skill(advanced_touch)
        self.assertTrue(success)
    
    def test_full_craft_sequence(self):
        """実際のクラフト手順のテスト"""
        # よく使う手順を再現
        sequence = [
            'veneration',         # ヴェネレーション
            'basic_synthesis',    # 作業
            'manipulation',       # マニピュレーション
            'innovation',         # イノベーション
            'basic_touch',        # 加工
            'standard_touch',     # 中級加工
            'advanced_touch',     # 上級加工
        ]
        
        for skill_name in sequence:
            skill = CRAFTING_SKILLS[skill_name]
            success = self.optimizer.apply_skill(skill)
            self.assertTrue(success, f"Skill {skill_name} failed")

if __name__ == '__main__':
    unittest.main() 