import pytest 
from src.excepciones_03 import Count


@pytest.mark.parametrize(
    ('number, expected'),
    
    [(5,'5,4,3,2,1,0'),
     (8,'8,7,6,5,4,3,2,1,0')
     ]
)
def test_Counts_params(number,expected):
    assert Count(number) == expected

def test_menorque0():
    with pytest.raises(ValueError):
        Count(-2)