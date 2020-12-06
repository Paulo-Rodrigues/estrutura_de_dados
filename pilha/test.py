from stack import Stack
# import unittest
from unittest import main, TestCase

class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_add(self):
        self.stack.add(2)
        self.assertEqual(self.stack.peek(), 2)

    def test_remove(self):
        self.stack.add(2)
        self.stack.add(5)
        self.stack.add(7)
        self.stack.remove()
        self.assertEqual(self.stack.items, [2, 5])

    def test_peek(self):
        self.stack.add(2)
        self.stack.add(4)
        self.assertEqual(self.stack.peek(), 4)

    def test_peek_none(self):
        self.assertEqual(self.stack.peek(), None)

    def test_items(self):
        self.stack.add(2)
        self.stack.add(5)
        self.assertEqual(self.stack.items, [2, 5])

    def test_size(self):
        self.stack.add(2)
        self.assertEqual(self.stack.size(), 1)

    def test_empty_true(self):
        self.assertTrue(self.stack.empty(), True)

    def test_empty_false(self):
        self.stack.add(2)
        self.assertFalse(self.stack.empty(), False)

if __name__=='__main__':
    main()
