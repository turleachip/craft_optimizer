class CraftFormulas:
    @staticmethod
    def calculate_progress(base_progress: int, craftsmanship: int, progress_rate: float, 
                         buffs: list = None) -> int:
        """進捗値を計算"""
        if progress_rate <= 0:
            return 0
            
        progress = (base_progress * (craftsmanship / 100)) * progress_rate
        
        if buffs:
            for buff in buffs:
                if hasattr(buff, 'progress_buff') and buff.progress_buff > 0:
                    progress *= (1 + buff.progress_buff)
        
        return int(progress)

    @staticmethod
    def get_base_progress(recipe_level: int) -> int:
        """
        レシピレベルに応じたベース進捗値を返す
        """
        # レシピレベルに応じたベース進捗値のマッピング
        # 実際のゲームデータに基づいて設定する必要あり
        level_progress_map = {
            90: 100,
            # 他のレベルも追加
        }
        return level_progress_map.get(recipe_level, 100) 

    @staticmethod
    def calculate_quality(base_quality: int, control: int, quality_rate: float,
                        inner_quiet_stacks: int = 0, buffs: list = None) -> int:
        """
        品質値を計算する
        
        Parameters:
        -----------
        base_quality : int
            ベースの品質値
        control : int
            加工精度
        quality_rate : float
            スキルの品質倍率
        inner_quiet_stacks : int
            インナークワイエットのスタック数
        buffs : list
            適用中のバフ効果のリスト
            
        Returns:
        --------
        int : 計算された品質値
        """
        # インナークワイエトの効果を計算（スタックごとに10%上昇）
        inner_quiet_bonus = 1.0 + (inner_quiet_stacks * 0.1)
        
        # 基本計算式
        quality = (base_quality * (control / 100)) * quality_rate * inner_quiet_bonus
        
        # バフ効果の適用（イノベーションなど）
        if buffs:
            for buff in buffs:
                if buff.quality_buff > 0:
                    quality *= (1 + buff.quality_buff)
        
        return int(quality)

    @staticmethod
    def get_base_quality(recipe_level: int) -> int:
        """
        レシピレベルに応じたベース品質値を返す
        """
        # レシピレベルに応じたベース品質値のマッピング
        level_quality_map = {
            90: 100,
            # 他のレベルも追加
        }
        return level_quality_map.get(recipe_level, 100)