import unittest
from convert_romanos import Romano

class CreateRomanoTest(unittest.TestCase):

    def setUp(self):
        self.numero_romano = Romano()

    def test_Method_Convert_I_in_Integer(self):
        self.assertEqual(self.numero_romano.convert_Romano("I"),1)

    def test_Method_Convert_I_in_Integer(self):
        self.assertEqual(self.numero_romano.convert_Romano("MD"),1500)

    def test_Method_Convert_I_in_Integer(self):
        self.assertEqual(self.numero_romano.convert_Romano("MD"),1500)



unittest.main()

