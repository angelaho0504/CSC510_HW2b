
import code
from code.armstrong import armstrong

def test_valid():
    assert armstrong.armstrong(999) == [1, 153, 370,371, 407]