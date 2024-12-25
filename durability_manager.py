from dataclasses import dataclass
from typing import Optional

@dataclass
class DurabilityState:
    current: int
    maximum: int
    
class DurabilityManager:
    def __init__(self, max_durability: int):
        self.state = DurabilityState(
            current=max_durability,
            maximum=max_durability
        )
    
    def calculate_consumption(self, base_cost: int, buffs: list = None) -> int:
        """
        実際の耐久度消費を計算
        
        Parameters:
        -----------
        base_cost : int
            スキルの基本消費耐久度
        buffs : list
            適用中のバフ効果のリスト（倹約など）
        """
        if base_cost <= 0:  # 回復効果の場合
            return base_cost
            
        cost = base_cost
        if buffs:
            for buff in buffs:
                if buff.durability_buff < 0:  # 倹約効果
                    cost = int(cost * (1 + buff.durability_buff))
        return max(1, cost)  # 最低でも1は消費
    
    def consume(self, amount: int) -> bool:
        """
        耐久度を消費
        
        Returns:
        --------
        bool : 耐久度が0以上ならTrue
        """
        self.state.current -= amount
        return self.state.current > 0
    
    def repair(self, amount: int):
        """耐久度を回復"""
        self.state.current = min(
            self.state.current + amount,
            self.state.maximum
        ) 