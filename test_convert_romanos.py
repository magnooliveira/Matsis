import unittest
from convert_romanos import Romano

class CreateRomanoTest(unittest.TestCase):

    def setUp(self):
        self.numero_romano = Romano()

    def test_Method_Convert_I_in_Integer(self):
        self.assertEqual(self.numero_romano.convert_Romano("I"),1)

unittest.main()

