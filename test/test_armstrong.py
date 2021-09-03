import armstong

def test_valid(self):

    armstong.input = lambda: 999
    output = armstong.armstrong()
    assert output == [1, 153, 370,371, 407]       

def teardown_method(self, method):
    armstong.input = input  