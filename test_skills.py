import unittest
from skills import CRAFTING_SKILLS, SYNTHESIS_SKILLS, TOUCH_SKILLS, BUFF_SKILLS, RECOVERY_SKILLS

class TestCraftingSkills(unittest.TestCase):
    def test_skill_data_integrity(self):
        """スキルデータの整合性チェック"""
        for skill_id, skill in CRAFTING_SKILLS.items():
            # 基本パラメータの存在確認
            self.assertIsNotNone(skill.name)
            self.assertIsNotNone(skill.cp_cost)
            self.assertGreaterEqual(skill.cp_cost, 0)
            
            # 成功率の範囲チェック
            self.assertGreaterEqual(skill.success_rate, 0)
            self.assertLessEqual(skill.success_rate, 100)

    def test_synthesis_skills(self):
        """作業系スキルの検証"""
        for skill_id, skill in SYNTHESIS_SKILLS.items():
            self.assertGreater(skill.progress_rate, 0)
            self.assertEqual(skill.quality_rate, 0)

    def test_touch_skills(self):
        """加工系スキルの検証"""
        for skill_id, skill in TOUCH_SKILLS.items():
            self.assertGreater(skill.quality_rate, 0)
            self.assertEqual(skill.progress_rate, 0)

    def test_buff_skills(self):
        """バフ系スキルの検証"""
        for skill_id, skill in BUFF_SKILLS.items():
            # バフ持続時間のチェック（インナークワイエットは例外）
            if skill.name != 'インナークワイエット':
                self.assertGreater(skill.buff_duration, 0)

    def test_recovery_skills(self):
        """回復系スキルの検証"""
        for skill_id, skill in RECOVERY_SKILLS.items():
            # 耐久度回復効果の確認
            self.assertLessEqual(skill.durability_cost, 0)

if __name__ == '__main__':
    unittest.main() 