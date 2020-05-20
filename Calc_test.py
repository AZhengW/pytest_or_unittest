from calc import Calc
import pytest
import yaml


class TestCalc:

    @pytest.fixture()
    def instantiation(self):  # 使用 fixture 装置完成计算机器实例的初始化
        cala = Calc()
        return cala

    test_data = yaml.safe_load(open("F:\\pytest_or_unittest\\Add_and_Div_testdata.yaml"))

    def get_steps(self):

        with open('test_steps.yml') as f:

            return yaml.safe_load(f)

    def any_steps(self, data):
        step = self.get_steps()
        for steps in step:
            if 'add' == steps:
                assert self.calc_add(data[0], data[1]) == data[0]+data[1]
            elif 'div' == steps:
                assert self.calc_div(data[0], data[1]) == data[0]/data[1]

    @pytest.mark.parametrize('a,b', test_data['add_data'])
    def calc_steps(self, a, b):
        #练习执行步骤
        data = [a, b]
        print(data)
        self.any_steps(data)

    @pytest.mark.parametrize('a,b', test_data['add_data'])
    def calc_add(self, a, b):
        calc = Calc()
        result = calc.add(a, b)
        return result

    @pytest.mark.parametrize('a,b', test_data['div_data'])
    def calc_div(self, a, b):
        calc = Calc()
        result = calc.div(a, b)
        return result

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
