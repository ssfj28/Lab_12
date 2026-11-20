"""Автоматические тесты основных операций очереди."""

import unittest

from queue_operations import Queue


class TestQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.queue: Queue[int] = Queue()

    def test_new_queue_is_empty(self) -> None:
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)

    def test_enqueue_and_size(self) -> None:
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.size(), 2)
        self.assertFalse(self.queue.is_empty())

    def test_fifo_order(self) -> None:
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.dequeue(), 20)
        self.assertEqual(self.queue.dequeue(), 30)
        self.assertTrue(self.queue.is_empty())

    def test_peek_does_not_remove_item(self) -> None:
        self.queue.enqueue(42)
        self.assertEqual(self.queue.peek(), 42)
        self.assertEqual(self.queue.size(), 1)

    def test_contains(self) -> None:
        self.queue.enqueue(5)
        self.assertTrue(self.queue.contains(5))
        self.assertFalse(self.queue.contains(7))

    def test_clear(self) -> None:
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.clear()
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)

    def test_get_items_returns_copy_in_queue_order(self) -> None:
        self.queue.enqueue(3)
        self.queue.enqueue(1)
        items = self.queue.get_items()
        self.assertEqual(items, [3, 1])
        items.append(99)
        self.assertEqual(self.queue.get_items(), [3, 1])

    def test_dequeue_empty_queue_raises_error(self) -> None:
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_peek_empty_queue_raises_error(self) -> None:
        with self.assertRaises(IndexError):
            self.queue.peek()


if __name__ == "__main__":
    unittest.main()
