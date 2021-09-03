import mock
import code

def test_valid():
    with mock.patch.object(__builtins__, 'input', lambda: 999):
        assert armstrong.function() == [1, 153, 370,371, 407]  