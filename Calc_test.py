from calc import Calc
import pytest
import yaml


class TestCalc:

    @pytest.fixture()
    def instantiation(self):  # 使用 fixture 装置完成计算机器实例的初始化
        cala = Calc()
        return cala

    test_data = yaml.safe_load(open("F:\\pytest_or_unittest\\Add_and_Div_testdata.yaml"))

    @pytest.mark.parametrize('a,b', test_data['add_data'])
    def calc_add(self, a, b, instantiation):
        result = instantiation.add(a, b)
        assert a + b == result

    @pytest.mark.parametrize('a,b', test_data['div_data'])
    def calc_div(self, a, b, instantiation):
        result = instantiation.div(a, b)
        assert a / b == result

    @pytest.mark.parametrize('a,b', test_data['subtract_data'])
    def calc_subtract(self, a, b, instantiation):
        result = instantiation.subtract(a, b)
        assert a - b == result

    @pytest.mark.parametrize('a,b', test_data['multiply_data'])
    def calc_multiply(self, a, b, instantiation):
        result = instantiation.multiply(a, b)
        assert a * b == result


if __name__ == '__main__':
    pytest.main(['Calc_test.py'])
