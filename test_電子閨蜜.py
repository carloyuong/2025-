import subprocess
import sys

# 测试主程序是否能正常导入和运行（不崩溃）
def test_import_and_run():
    # 直接运行主文件，看是否报错
    result = subprocess.run([sys.executable, "電子閨蜜.py"], capture_output=True, text=True)
    assert result.returncode == 0, f"程序运行失败:\n{result.stdout}\n{result.stderr}"

# 如果你有具体函数，可以这样测试
# from 電子閨蜜 import some_function
# def test_some_function():
#     assert some_function("输入") == "预期输出"
