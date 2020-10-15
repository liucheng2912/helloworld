"""
@pytest.mark.parametrize(argnames,argvalues)
argnames  要参数化的变量 string(逗号分隔) list tuple
argvalues 要参数化的值 List list[tuple]
"""
import pytest
import yaml


class TestData:
    # 元组
    @pytest.mark.parametrize(("a","b"),[(10,20),(10,30)])
    def test_param(self,a,b):
        print(a+b)
    # 字符串
    @pytest.mark.parametrize("a,b", [(10, 20), (10, 30)])
    def test_param1(self, a, b):
        print(a + b)\
    # 列表
    @pytest.mark.parametrize(["a","b"],[(10,20),(10,30)])
    def test_param2(self,a,b):
        print(a+b)
    # 读取yaml文件
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
    def test_param3(self,a,b):
        print(a+b)



