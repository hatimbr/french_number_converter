import unittest
from french_converter.converter import FrenchConverter

class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = FrenchConverter()

    def test_to_sixteen(self):
        self.assertEqual(self.converter._to_sixteen(1), "un")
        self.assertEqual(self.converter._to_sixteen(16), "seize")

    def test_to_hundred(self):
        self.assertEqual(self.converter._to_hundred(20), "vingt")
        self.assertEqual(self.converter._to_hundred(80), "quatre-vingts")
        self.assertEqual(self.converter._to_hundred(99), "quatre-vingt-dix-neuf")

    def test_to_thousand(self):
        self.assertEqual(self.converter._to_thousand(100), "cent")
        self.assertEqual(self.converter._to_thousand(200), "deux-cents")

    def test_to_million(self):
        self.assertEqual(self.converter._to_million(1000), "mille")
        self.assertEqual(self.converter._to_million(2000), "deux-milles")

    def test_convert(self):
        self.assertEqual(self.converter.convert(16), "seize")
        self.assertEqual(self.converter.convert(100), "cent")
        self.assertEqual(self.converter.convert(1000), "mille")
        self.assertEqual(self.converter.convert(200), "deux-cents")
        self.assertEqual(self.converter.convert(202), "deux-cent-deux")
        self.assertEqual(self.converter.convert(2000), "deux-milles")
        self.assertEqual(self.converter.convert(2001), "deux-mille-un")

if __name__ == '__main__':
    unittest.main()