from dataclasses import dataclass
from typing import Optional

@dataclass
class CraftingSkill:
    name: str
    cp_cost: int
    success_rate: int = 100
    progress_rate: float = 0.0    
    quality_rate: float = 0.0     
    durability_cost: int = 10     
    buff_duration: int = 0        
    progress_buff: float = 0.0    
    quality_buff: float = 0.0     
    durability_buff: float = 0.0  

# 作業系スキル
SYNTHESIS_SKILLS = {
    'basic_synthesis': CraftingSkill(
        name='作業',
        cp_cost=0,
        progress_rate=1.0,
        durability_cost=10
    ),
    'careful_synthesis': CraftingSkill(
        name='倹約作業',
        cp_cost=7,
        progress_rate=1.5,
        durability_cost=10
    ),
    'prudent_synthesis': CraftingSkill(
        name='倹約作業',
        cp_cost=18,
        progress_rate=1.8,
        durability_cost=5,
    ),
    'groundwork': CraftingSkill(
        name='下地作業',
        cp_cost=18,
        progress_rate=3.0,
        durability_cost=20
    ),
    'focused_synthesis': CraftingSkill(
        name='注視作業',
        cp_cost=5,
        progress_rate=2.0,
        success_rate=50,
        durability_cost=10
    ),
    'intensive_synthesis': CraftingSkill(
        name='集中作業',
        cp_cost=6,
        progress_rate=4.0,
        durability_cost=10
    ),
}

# 加工系スキル
TOUCH_SKILLS = {
    'basic_touch': CraftingSkill(
        name='加工',
        cp_cost=18,
        quality_rate=1.0,
        durability_cost=10
    ),
    'standard_touch': CraftingSkill(
        name='中級加工',
        cp_cost=32,
        quality_rate=1.25,
        durability_cost=10
    ),
    'advanced_touch': CraftingSkill(
        name='上級加工',
        cp_cost=46,
        quality_rate=1.5,
        durability_cost=10
    ),
    'prudent_touch': CraftingSkill(
        name='倹約加工',
        cp_cost=25,
        quality_rate=1.0,
        durability_cost=5
    ),
    'focused_touch': CraftingSkill(
        name='注視加工',
        cp_cost=18,
        quality_rate=1.5,
        success_rate=50,
        durability_cost=10
    ),
    'preparatory_touch': CraftingSkill(
        name='下地加工',
        cp_cost=40,
        quality_rate=2.0,
        durability_cost=20
    ),
}

# バフ系スキル
BUFF_SKILLS = {
    'inner_quiet': CraftingSkill(
        name='インナークワイエット',
        cp_cost=18,
        buff_duration=0,  # 永続
        quality_buff=0.1  # スタックごとに品質+10%
    ),
    'veneration': CraftingSkill(
        name='ヴェネレーション',
        cp_cost=18,
        buff_duration=4,
        progress_buff=0.5
    ),
    'innovation': CraftingSkill(
        name='イノベーション',
        cp_cost=18,
        buff_duration=4,
        quality_buff=0.5
    ),
    'great_strides': CraftingSkill(
        name='グレートストライド',
        cp_cost=32,
        buff_duration=3,
        quality_buff=1.0
    ),
    'waste_not': CraftingSkill(
        name='倹約',
        cp_cost=56,
        buff_duration=4,
        durability_buff=-0.5
    ),
    'waste_not_ii': CraftingSkill(
        name='長期倹約',
        cp_cost=98,
        buff_duration=8,
        durability_buff=-0.5
    ),
}

# 回復系スキル
RECOVERY_SKILLS = {
    'masters_mend': CraftingSkill(
        name='マスターズメンド',
        cp_cost=88,
        durability_cost=-30  # 耐久度回復はマイナス値で表現
    ),
    'manipulation': CraftingSkill(
        name='マニピュレーション',
        cp_cost=96,
        buff_duration=8,
        durability_cost=-5  # 毎ターン5回復
    ),
}

# 全スキルを1つの辞書にまとめる
CRAFTING_SKILLS = {
    **SYNTHESIS_SKILLS,
    **TOUCH_SKILLS,
    **BUFF_SKILLS,
    **RECOVERY_SKILLS
}
