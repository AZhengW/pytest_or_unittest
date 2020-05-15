from calc import Calc
import pytest
import yaml


class TestCalc:

    def setup_class(self):
        self.cala = Calc()

    file = open("F://pytest_or_unittest//Add_and_Div_testdata.yaml", 'r', encoding="utf-8")
    file_data = file.read()
    add_data = file_data

   # @pytest.mark.parametrize('a,b', add_data)
    def test_add(self, a, b):
        result = self.cala.add(a, b)
        assert result == a + b

    def test_add2(self):
        file = open("F://pytest_or_unittest//Add_and_Div_testdata.yaml", 'r', encoding="utf-8")
        file_data = file.read()
        add_data = file_data
        print(add_data)

    def teardown_class(self):
        pass


if __name__ == '__main__':
    pytest.main(['Calc_test.py'])
