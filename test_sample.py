import unittest


def add(a, b):
    return a + b


class SampleTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-2, 2), 0)


if __name__ == "__main__":
    unittest.main()
