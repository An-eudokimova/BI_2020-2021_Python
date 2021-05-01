import unittest
from Dna_Rna_classes import Dna, Rna


class TestDna(unittest.TestCase):
    def setUp(self):
        self.Dna = Dna('agtCGAT')

    def test_wrong_sequence(self):
        with self.assertRaises(ValueError):
            Dna('AugT')

    def test_right_sequence(self):
        self.assertTrue(Dna('AcgT'))
        self.assertTrue(Dna('ACGT'))
        self.assertTrue(Dna('acgt'))

    def test_complement(self):
        self.assertEqual(self.Dna.complement(), 'tcaGCTA')

    def test_reverse_complement(self):
        self.assertEqual(self.Dna.reverse_complement(), 'ATCGact')

    def test_gc_content(self):
        self.assertEqual(self.Dna.gc_content(), 42.86)

    def test_equality(self):
        self.assertTrue(self.Dna.string.upper() == 'agtCGAT'.upper())
        self.assertFalse(self.Dna.string.upper() == 'TgtCGT'.upper())
        self.assertFalse(self.Dna.string.upper() == 'agtCGAT')

    def test_strict_equality(self):
        self.assertTrue(self.Dna.string == 'agtCGAT')
        self.assertFalse(self.Dna.string == 'agtCGAT'.upper())

    def test_length(self):
        self.assertEqual(len(self.Dna.string), 7)

    def test_transcribe(self):
        self.assertTrue(self.Dna.transcribe(), Rna)
        self.assertTrue(self.Dna.transcribe().string == 'aguCGAU')


class TestRna(unittest.TestCase):
    def setUp(self):
        self.Rna = Rna('aguCGAU')

    def test_wrong_sequence(self):
        with self.assertRaises(ValueError):
            Rna('AugT')

    def test_right_sequence(self):
        self.assertTrue(Rna('AcgU'))
        self.assertTrue(Rna('ACGU'))
        self.assertTrue(Rna('acgu'))

    def test_complement(self):
        self.assertEqual(self.Rna.complement(), 'ucaGCUA')

    def test_reverse_complement(self):
        self.assertEqual(self.Rna.reverse_complement(), 'AUCGacu')

    def test_gc_content(self):
        self.assertEqual(self.Rna.gc_content(), 42.86)

    def test_equality(self):
        self.assertTrue(self.Rna.string.upper() == 'aguCGAU'.upper())
        self.assertFalse(self.Rna.string.upper() == 'UguCGU'.upper())
        self.assertFalse(self.Rna.string.upper() == 'aguCGAU')

    def test_strict_equality(self):
        self.assertTrue(self.Rna.string == 'aguCGAU')
        self.assertFalse(self.Rna.string == 'aguCGAU'.upper())

    def test_length(self):
        self.assertEqual(len(self.Rna.string), 7)

    def test_back_transcribe(self):
        self.assertTrue(self.Rna.back_transcribe(), Dna)
        self.assertTrue(self.Rna.back_transcribe().string == 'agtCGAT')


if __name__ == '__main__':
    unittest.main()