from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Buff:
    name: str
    duration: int
    progress_buff: float = 0.0
    quality_buff: float = 0.0
    durability_buff: float = 0.0

class BuffManager:
    def __init__(self):
        self.active_buffs: Dict[str, Buff] = {}
        self.inner_quiet_stacks: int = 0
    
    def add_buff(self, skill_name: str, duration: int, 
                progress_buff: float = 0.0, 
                quality_buff: float = 0.0,
                durability_buff: float = 0.0):
        """バフを追加"""
        self.active_buffs[skill_name] = Buff(
            name=skill_name,
            duration=duration,
            progress_buff=progress_buff,
            quality_buff=quality_buff,
            durability_buff=durability_buff
        )
    
    def update_inner_quiet(self, is_touch_action: bool = False):
        """インナークワイエットスタックの更新"""
        if is_touch_action and self.inner_quiet_stacks < 10:
            self.inner_quiet_stacks += 1
    
    def get_total_buffs(self) -> tuple[float, float, float]:
        """現在のバフ効果の合計を取得"""
        total_progress = 0.0
        total_quality = 0.0
        total_durability = 0.0
        
        for buff in self.active_buffs.values():
            total_progress += buff.progress_buff
            total_quality += buff.quality_buff
            total_durability += buff.durability_buff
            
        return total_progress, total_quality, total_durability
    
    def tick_buffs(self):
        """ターン経過時のバフ更新"""
        expired_buffs = []
        for name, buff in self.active_buffs.items():
            buff.duration -= 1
            if buff.duration <= 0:
                expired_buffs.append(name)
        
        # 期限切れのバフを削除
        for name in expired_buffs:
            del self.active_buffs[name] 