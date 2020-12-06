from queue import Queue
from unittest import main, TestCase

class TestQueue(TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_items(self):
        self.assertEqual(self.queue.items, [])

    def test_add(self):
        self.queue.add(2)
        self.queue.add(4)
        self.assertEqual(self.queue.items, [2, 4])

    def test_remove(self):
        self.queue.add(2)
        self.queue.add(4)
        self.queue.remove()
        self.assertEqual(self.queue.items, [4])

    def test_peek(self):
        self.queue.add(2)
        self.queue.add(4)
        self.assertEqual(self.queue.peek(), 4)

    def test_peek_none(self):
        self.assertEqual(self.queue.peek(), None)

    def test_items(self):
        self.queue.add(2)
        self.queue.add(5)
        self.assertEqual(self.queue.items, [2, 5])

    def test_size(self):
        self.queue.add(2)
        self.assertEqual(self.queue.size(), 1)

    def test_empty_true(self):
        self.assertTrue(self.queue.empty(), True)

    def test_empty_false(self):
        self.queue.add(2)
        self.assertFalse(self.queue.empty(), False)


if __name__=='__main__':
    main()
