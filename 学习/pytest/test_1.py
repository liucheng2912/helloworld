import pytest
def func(x):
    return x+1
# 参数化构建
@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,20),
    ('a','a1'),
    (3,4),
    (5,6)
])

# test_a指定 并获取到username返回值
@pytest.fixture()
def login():
    username="jerry"
    return username

def test_answer(a,b):
    assert func(a) == b

def test_answer1():
    assert func(4) == 5

class TestDemo:
    def test_a(self,login):
        print(f'a username = {login}')

    def test_b(self):
        print('b')

if __name__ == '__main__':
    # 执行整个文件
    # pytest.main(['test_a.py'])
    # -v打印详细日志  指定执行TestDemo类
    pytest.main(['test_a.py::TestDemo','-v'])
    # -k 指定执行某条用例
    # pytest -k test_b
    # test_answer也会被执行 因为包含了test_a
    # pytest -k 'test_a or test_b'
