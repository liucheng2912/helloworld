import pytest
import yaml
"""
yml文件中若是输入 - test：127.0.0.1 传递的就是一个列表，包含字典[{"test":"127.0.0.1"}] 
"""
class TestDemo:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的ip地址是",env["test"])
        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的ip地址是",env["dev"])