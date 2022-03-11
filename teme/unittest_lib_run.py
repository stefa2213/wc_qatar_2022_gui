import unittest
import unittest_library


class TestStringMethods(unittest.TestCase):

    def test_f_to_m(self):
        f = 4
        c = unittest_library.f_to_m(f)
        self.assertEqual(c, ' 1.219')

    def test_m_to_f(self):
        c = 2
        f = unittest_library.m_to_f(c)
        self.assertEqual(f, ' 0.610')

    def test_rem_lett(self):
        val = '123,45 Lei'
        val = val.replace(',', '.')
        val = val.replace(' ', '')
        val_real = 123.45
        val_real = str(val_real)
        result = unittest_library.rem_lett(val)
        self.assertEqual(result, val_real)

    def test_roman_number(self):
        nr_rom = 'xliv'
        result = unittest_library.convert_roman_number(nr_rom)
        self.assertEqual(result, 44)


if __name__ == '__main__':
    unittest.main()
