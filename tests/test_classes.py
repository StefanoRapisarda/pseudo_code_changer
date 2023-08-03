import pytest
from pseudo_code_changer.classes import PseudoCode

class TestPseudoCode:
    def test_empty_code(self):
        code = PseudoCode()

        assert isinstance(code, PseudoCode)

    @pytest.mark.parametrize('firstc',['A1','B23','A123', 'B9870'])
    def test_wrong_code_lenght(self,firstc):
        message = 'Pseudo code must contain exactly 6 characters'
        with pytest.raises(AssertionError) as e_info:
            code = PseudoCode(f'{firstc}34567')
        assert str(e_info.value) == message

    @pytest.mark.parametrize('firstc',[1,'a','t','C', 'b'])
    def test_wrong_code_first_character(self,firstc):
        message = 'First character must be either A or B'
        with pytest.raises(AssertionError) as e_info:
            code = PseudoCode(f'{firstc}34567')
        assert str(e_info.value) == message

    @pytest.mark.parametrize('numeric',['aytrr','tbhhb','213fg', 'oiu76'])
    def test_wrong_code_numeric(self,numeric):
        message = 'All but first character must be numbers'
        with pytest.raises(AssertionError) as e_info:
            code = PseudoCode(f'A{numeric}')
        assert str(e_info.value) == message