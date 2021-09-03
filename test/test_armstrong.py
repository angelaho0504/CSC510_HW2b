import sys
sys.path.insert('../code')
import armstrong

def test_valid(self):

    armstrong.input = lambda: 999
    output = armstrong.armstrong()
    assert output == [1, 153, 370,371, 407]       

def teardown_method(self, method):
    armstrong.input = input  