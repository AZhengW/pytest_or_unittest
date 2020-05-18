from calc import Calc
import pytest
import yaml


class TestCalc:

    def setup_class(self):
        self.cala = Calc()

    test_data = yaml.safe_load(open("F:\\pytest_or_unittest\\Add_and_Div_testdata.yaml"))

    @pytest.mark.parametrize('a,b', test_data['add_data'])
    def test_add(self, a, b):
        result = self.cala.add(a, b)
        assert a + b == result

    def test_div(self, a, b,):
        result = self.cala.div(a, b)




if __name__ == '__main__':
    pytest.main(['Calc_test.py'])
