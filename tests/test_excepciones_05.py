import pytest 
from src.excepciones_05 import Ask_Password

def test_comparation():
    with pytest.raises(NameError):
        Ask_Password('nr')