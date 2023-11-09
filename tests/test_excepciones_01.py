import pytest 
from src.excepciones_01 import Age_Loop, Ask_User

def test_Ask_User(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 12)
    result = Ask_User()
    assert result == 12

@pytest.mark.parametrize(
    ('age, expected'),
    
    [(5,'1,2,3,4,5'),
     (8,'1,2,3,4,5,6,7,8')
     ]
)
def test_Age_Loop_params(age,expected):
    assert Age_Loop(age) == expected