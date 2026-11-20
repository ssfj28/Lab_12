"""Интерактивная демонстрация работы очереди (FIFO) на collections.deque."""

from collections import deque
from typing import Deque, Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    """Простая очередь: добавление в конец, извлечение из начала."""

    def __init__(self) -> None:
        self._items: Deque[T] = deque()

    def enqueue(self, item: T) -> None:
        """Добавить элемент в конец очереди."""
        self._items.append(item)

    def dequeue(self) -> T:
        """Извлечь и вернуть первый элемент очереди."""
        if self.is_empty():
            raise IndexError("Невозможно извлечь элемент: очередь пуста.")
        return self._items.popleft()

    def peek(self) -> T:
        """Вернуть первый элемент без его удаления."""
        if self.is_empty():
            raise IndexError("Невозможно просмотреть элемент: очередь пуста.")
        return self._items[0]

    def is_empty(self) -> bool:
        """Проверить, пуста ли очередь."""
        return len(self._items) == 0

    def size(self) -> int:
        """Вернуть количество элементов в очереди."""
        return len(self._items)

    def contains(self, item: T) -> bool:
        """Проверить, содержится ли значение в очереди."""
        return item in self._items

    def clear(self) -> None:
        """Удалить все элементы из очереди."""
        self._items.clear()

    def get_items(self) -> list[T]:
        """Вернуть копию элементов в порядке извлечения."""
        return list(self._items)


def show_menu() -> None:
    print("\n========== РАБОТА С ОЧЕРЕДЬЮ ==========")
    print("1. Добавить элемент в очередь")
    print("2. Извлечь первый элемент")
    print("3. Посмотреть первый элемент")
    print("4. Проверить, пуста ли очередь")
    print("5. Узнать количество элементов")
    print("6. Проверить наличие элемента")
    print("7. Очистить очередь")
    print("8. Показать все элементы")
    print("0. Выход")
    print("=======================================")


def main() -> None:
    queue: Queue[str] = Queue()

    while True:
        show_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            item = input("Введите значение: ")
            queue.enqueue(item)
            print(f"Элемент «{item}» добавлен в конец очереди.")

        elif choice == "2":
            try:
                item = queue.dequeue()
                print(f"Из очереди извлечён элемент: «{item}».")
            except IndexError as error:
                print(error)

        elif choice == "3":
            try:
                print(f"Первый элемент очереди: «{queue.peek()}».")
            except IndexError as error:
                print(error)

        elif choice == "4":
            if queue.is_empty():
                print("Очередь пуста.")
            else:
                print("Очередь содержит элементы.")

        elif choice == "5":
            print(f"Количество элементов в очереди: {queue.size()}.")

        elif choice == "6":
            item = input("Введите значение для поиска: ")
            if queue.contains(item):
                print(f"Элемент «{item}» присутствует в очереди.")
            else:
                print(f"Элемент «{item}» не найден в очереди.")

        elif choice == "7":
            queue.clear()
            print("Очередь очищена.")

        elif choice == "8":
            items = queue.get_items()
            if items:
                print("Элементы очереди (от первого к последнему):")
                print(" -> ".join(items))
            else:
                print("Очередь пуста.")

        elif choice == "0":
            print("Работа программы завершена.")
            break

        else:
            print("Неизвестная команда. Выберите пункт от 0 до 8.")


if __name__ == "__main__":
    main()
