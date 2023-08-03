import pytest
from pseudo_code_changer.classes import PseudoCode

class TestPseudoCode:
    def test_empty_code(self):
        code = PseudoCode()

        assert isinstance(code, PseudoCode)

    @pytest.mark.parametrize('firstc',[1,'a','t','C', 'b'])
    def test_wrong_code_first_character(self,firstc):
        message = 'First character must be either A or B'
        with pytest.raises(AssertionError) as e_info:
            code = PseudoCode(f'{firstc}34567')
        assert str(e_info.value) == message