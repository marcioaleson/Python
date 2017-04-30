# encoding: utf-8

from column import Column
import unittest

class ColumnTest(unittest.TestCase):
    def test_validate_bigint(self):
        self.assertTrue(Column.validate('bigint', 100))
        self.assertTrue( not Column.validate('bigint', 10.1))
        self.assertTrue( not Column.validate('bigint', 'teste'))

    def test_validate_numeric(self):
        self.assertTrue(Column.validate('numeric', 10.1))
        self.assertTrue(Column.validate('numeric', 100))
        self.assertTrue( not Column.validate('numeric', 'teste'))

    def test_validate_varchar(self):
        self.assertTrue(Column.validate('varchar', 'teste'))
        self.assertTrue( not Column.validate('varchar', 100))
        self.assertTrue( not Column.validate('varchar', 10.1))
