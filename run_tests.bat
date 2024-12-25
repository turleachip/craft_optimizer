@echo off
echo 🧪 FF14クラフター最適化ツール テスト実行
echo ----------------------------------------

python -m unittest ^
    test_skills.py ^
    test_buff_manager.py ^
    test_durability.py ^
    test_integration.py ^
    test_base_efficiency.py ^
    -v

echo.
echo テスト完了
pause 