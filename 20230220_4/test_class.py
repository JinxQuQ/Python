# test_class.py

class TestClass:
    def test_one(self):
        x = "this"
        assert 'a' in x


    def test_two(self):
        class baby:
            x = 'check'

        assert hasattr(baby, 'x')