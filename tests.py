import unittest
from gener_iter import generator
from gener_iter import Iterator


class GeneratorIteratorTests(unittest.TestCase):

    def test_generator_output_is_correct(self):
        a = 'sometext'
        self.assertEqual(list(generator(1, 100, 10)), list(range(1, 100, 10)))
        self.assertEqual(list(generator(1, -100, -10)), list(range(1, -100, -10)))
        self.assertEqual(list(generator(-1, 100, 10)), list(range(-1, 100, 10)))
        self.assertEqual(list(generator(0, 0, 10)), list(range(0, 0, 10)))
        with self.assertRaises(ValueError):
            list(generator(a))

    def test_generator_on_reduced_data(self):
        self.assertEqual(list(generator(1, 100)), list(range(1, 100)))
        self.assertEqual(list(generator(-100)), list(range(-100)))
        self.assertEqual(list(generator(100)), list(range(100)))
        self.assertEqual(list(generator(10, 0, 10)), list(range(10, 0, 10)))

    def test_Iterator_is_correct(self):
        a = 'sometext'
        self.assertEqual(list(Iterator(1, 100, 10)), list(range(1, 100, 10)))
        self.assertEqual(list(Iterator(1, -100, -10)), list(range(1, -100, -10)))
        self.assertEqual(list(Iterator(-1, 100, 10)), list(range(-1, 100, 10)))
        self.assertEqual(list(Iterator(0, 0, 10)), list(range(0, 0, 10)))
        with self.assertRaises(ValueError):
            list(Iterator(a))


    def test_Iterator_on_reduced_data(self):
        self.assertEqual(list(Iterator(1, 100)), list(range(1, 100)))
        self.assertEqual(list(Iterator(-100)), list(range(-100)))
        self.assertEqual(list(Iterator(100)), list(range(100)))
        self.assertEqual(list(Iterator(10, 0, 10)), list(range(10, 0, 10)))

