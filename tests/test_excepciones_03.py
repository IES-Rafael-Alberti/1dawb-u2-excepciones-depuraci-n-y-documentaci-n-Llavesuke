import pytest 
from src.excepciones_03 import Count


@pytest.mark.parametrize(
    ('number, expected'),
    
    [(5,'1,3,5'),
     (8,'1,3,5,7')
     ]
)
def test_Counts_params(number,expected):
    assert Count(number) == expected

def test_menorque0():
    with pytest.raises(ValueError):
        Count(-2)