import pytest 
from src.excepciones_02 import impar


@pytest.mark.parametrize(
    ('age, expected'),
    
    [(5,'1,3,5'),
     (8,'1,3,5,7')
     ]
)
def test_impar_params(age,expected):
    assert impar(age) == expected