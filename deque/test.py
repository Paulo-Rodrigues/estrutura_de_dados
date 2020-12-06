from deque import Deque
from unittest import main, TestCase

class TestDeque(TestCase):
    def setUp(self):
        self.deque = Deque()

    def test_add_front(self):
        self.deque.add_front(2)
        self.deque.add_front(4)
        self.assertEqual(self.deque.items, [4, 2])

    def test_add_rear(self):
        self.deque.items = [1,2,3]
        self.deque.add_rear(5)
        self.assertEqual(self.deque.items, [1,2,3,5])

    def test_remove_front(self):
        self.deque.items = [1,2,3]
        self.deque.remove_front()
        self.assertEqual(self.deque.items, [2,3])

    def test_remove_rear(self):
        self.deque.items = [1,2,3]
        self.deque.remove_rear()
        self.assertEqual(self.deque.items, [1,2])

    def test_is_empty(self):
        self.assertTrue(self.deque.is_empty(), True)

    def test_size(self):
        self.deque.items = [1,2,3]
        self.assertEqual(self.deque.size(), 3)

if __name__=='__main__':
    main()
