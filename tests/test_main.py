import unittest
from main import translate_text

class TestMain(unittest.TestCase):

    def test_translate_text(self):
        translated_text = translate_text('Lego', 'RU')
        self.assertEqual(translated_text, 'Лего')

if __name__ == '__main__':
    unittest.main()