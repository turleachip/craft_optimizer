from skills import CRAFTING_SKILLS
from craft_formulas import CraftFormulas
from buff_manager import BuffManager
from durability_manager import DurabilityManager

class CraftingState:
    def __init__(self):
        self.durability = 0      # 耐久度
        self.progress = 0        # 進捗
        self.quality = 0         # 品質
        self.cp = 0             # CP
        self.inner_quiet = 0     # インナークワイエットのスタック数
        self.condition = '通常'   # 状態（通常、高品質、最高品質、低品質）

class CraftingSkill:
    def __init__(self, name, cp_cost, success_rate=100):
        self.name = name        # スキル名
        self.cp_cost = cp_cost  # CP消費
        self.success_rate = success_rate  # 成功率

class CraftOptimizer:
    def __init__(self, recipe_level, craftsmanship, control, cp):
        self.recipe_level = recipe_level
        self.craftsmanship = craftsmanship
        self.control = control
        self.max_cp = cp
        self.formulas = CraftFormulas()
        self.buff_manager = BuffManager()
        self.durability_manager = DurabilityManager(70)  # 標準的な耐久度で初期化
        
    def simulate_action(self, state, skill):
        # スキル使用時のシミュレーション処理
        pass
        
    def find_optimal_rotation(self, max_steps=20):
        # 最適なスキル回しを探索
        pass

    def calculate_progress(self, skill, current_buffs=None):
        """スキル使用時の進捗増加量を計算"""
        if not hasattr(skill, 'progress_rate') or skill.progress_rate <= 0:
            return 0
        
        base_progress = self.formulas.get_base_progress(self.recipe_level)
        return self.formulas.calculate_progress(
            base_progress,
            self.craftsmanship,
            skill.progress_rate,
            current_buffs
        )

    def calculate_quality(self, skill, inner_quiet_stacks=0, current_buffs=None):
        """スキル使用時の品質増加量を計算"""
        if not hasattr(skill, 'quality_rate') or skill.quality_rate <= 0:
            return 0
        
        base_quality = self.formulas.get_base_quality(self.recipe_level)
        return self.formulas.calculate_quality(
            base_quality,
            self.control,
            skill.quality_rate,
            inner_quiet_stacks,
            current_buffs
        )

    def apply_skill(self, skill):
        """スキルを使用し、効果を適用"""
        # バフ効果の取得
        buffs = list(self.buff_manager.active_buffs.values())
        
        # 耐久度の消費計算と適用
        durability_cost = self.durability_manager.calculate_consumption(
            skill.durability_cost,
            buffs
        )
        
        if not self.durability_manager.consume(durability_cost):
            return False
            
        # バフスキルの場合
        if skill.buff_duration > 0:
            self.buff_manager.add_buff(
                skill.name,
                skill.buff_duration,
                skill.progress_buff,
                skill.quality_buff,
                skill.durability_buff
            )
        
        # 加工スキルの場合、インナークワイエット更新
        if skill.quality_rate > 0:
            self.buff_manager.update_inner_quiet(True)
        
        # バフの更新
        self.buff_manager.tick_buffs()
        
        return True
