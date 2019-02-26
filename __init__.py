import unittest
from gener_iter import generator
from gener_iter import iterator

class GeneratorTests(unittest.TestCase):
    def setUp(self):
        print('Testing begins')  # действие перед каждой функцией
    def test_generator_output_is_correct(self):
        self.assertEqual(list(generator(1, 100, 10)), list(range(1, 100, 10)))
        self.assertEqual(list(generator(1, -100, -10)), list(range(1, -100, -10)))
        self.assertEqual(list(generator(-1, 100, 10)), list(range(-1, 100, 10)))
        self.assertEqual(list(generator(0, 0, 0)), list(range(0, 0, 0)))
        self.assertEqual(list(generator(0, 0, 10)), list(range(0, 0, 10)))
        self.assertEqual(list(generator(1, 100)), list(range(1, 100)))
        self.assertEqual(list(generator(-100)), list(range(-100)))
        self.assertEqual(list(generator(100)), list(range(100)))
        self.assertEqual(list(generator(a), list(range(a)))
        self.assertEqual(list(generator(10, 0, 10)), list(range(10, 0, 10)))

    def test_generator_iterator_is_correct(self):
        self.assertEqual(list(iterator(1, 100, 10)), list(range(1, 100, 10)))
        self.assertEqual(list(iterator(1, -100, -10)), list(range(1, -100, -10)))
        self.assertEqual(list(iterator(-1, 100, 10)), list(range(-1, 100, 10)))
        self.assertEqual(list(iterator(0, 0, 0)), list(range(0, 0, 0)))
        self.assertEqual(list(iterator(0, 0, 10)), list(range(0, 0, 10)))
        self.assertEqual(list(iterator(1, 100)), list(range(1, 100)))
        self.assertEqual(list(iterator(-100)), list(range(-100)))
        self.assertEqual(list(iterator(100)), list(range(100)))
        self.assertEqual(list(iterator(a), list(range(a)))
        self.assertEqual(list(iterator(10, 0, 10)), list(range(10, 0, 10)))

