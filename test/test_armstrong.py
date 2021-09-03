import code
import os
import sys
__dirname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, __dirname + '../')

from armstrong import armstrong

def test_valid():

    assert armstrong.armstrong(999) == [1, 153, 370,371, 407]

#     armstrong.input = lambda: 999
#     output = armstrong.armstrong()
#     assert output == [1, 153, 370,371, 407]       

# def teardown_method(self, method):
#     armstrong.input = input  
