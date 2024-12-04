from typing import Any

class Table:
    """
    Класс, представляющий стол.

    Атрибуты:
    - material (str): Материал стола.
    - height (float): Высота стола в сантиметрах.

    Методы:
    - describe(): Описание стола.
    - adjust_height(new_height: float): Изменяет высоту стола.
    """

    def __init__(self, material: str, height: float):
        if height <= 0:
            raise ValueError("Высота должна быть больше 0.")
        self.material = material
        self.height = height

    def describe(self) -> str:
        """
        Возвращает описание стола.
        """
        return f"Стол сделан из {self.material}, высота: {self.height} см."

    def adjust_height(self, new_height: float):
        """
        Изменяет высоту стола.

        Args:
        - new_height (float): Новая высота стола.

        Raises:
        - ValueError: Если высота <= 0.
        """
        if new_height <= 0:
            raise ValueError("Высота должна быть больше 0.")
        self.height = new_height


class Tree:
    """
    Класс, представляющий дерево.

    Атрибуты:
    - species (str): Вид дерева.
    - age (int): Возраст дерева в годах.

    Методы:
    - grow(years: int): Увеличивает возраст дерева.
    - describe(): Описание дерева.
    """

    def __init__(self, species: str, age: int):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.species = species
        self.age = age

    def grow(self, years: int):
        """
        Увеличивает возраст дерева.

        Args:
        - years (int): Количество лет, на которое увеличивается возраст.

        Raises:
        - ValueError: Если years < 0.
        """
        if years < 0:
            raise ValueError("Количество лет должно быть положительным.")
        self.age += years

    def describe(self) -> str:
        """
        Возвращает описание дерева.
        """
        return f"{self.species} возрастом {self.age} лет."


class FacebookPost:
    """
    Класс, представляющий пост на Facebook.

    Атрибуты:
    - content (str): Содержимое поста.
    - likes (int): Количество лайков.

    Методы:
    - like(): Увеличивает количество лайков.
    - show(): Возвращает содержимое поста.
    """

    def __init__(self, content: str, likes: int = 0):
        if likes < 0:
            raise ValueError("Количество лайков не может быть отрицательным.")
        self.content = content
        self.likes = likes

    def like(self):
        """
        Увеличивает количество лайков.
        """
        self.likes += 1

    def show(self) -> str:
        """
        Возвращает содержимое поста и количество лайков.
        """
        return f"Пост: {self.content}\nЛайки: {self.likes}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
