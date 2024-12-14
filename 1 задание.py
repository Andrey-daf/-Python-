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

    Примеры:
    >>> table = Table("дерево", 75)
    >>> table.describe()
    'Стол сделан из дерево, высота: 75 см.'
    >>> table.adjust_height(80)
    >>> table.height
    80
    >>> table.adjust_height(-10)
    Traceback (most recent call last):
        ...
    ValueError: Высота должна быть больше 0.
    """

    def __init__(self, material: str, height: float):
        if height <= 0:
            raise ValueError("Высота должна быть больше 0.")
        self.material = material
        self.height = height

    def describe(self) -> str:
        """
        Возвращает описание стола.

        Примеры:
        >>> table = Table("металл", 100)
        >>> table.describe()
        'Стол сделан из металл, высота: 100 см.'
        """
        return f"Стол сделан из {self.material}, высота: {self.height} см."

    def adjust_height(self, new_height: float):
        """
        Изменяет высоту стола.

        Args:
        - new_height (float): Новая высота стола.

        Raises:
        - ValueError: Если высота <= 0.

        Примеры:
        >>> table = Table("стекло", 90)
        >>> table.adjust_height(95)
        >>> table.height
        95
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

    Примеры:
    >>> tree = Tree("дуб", 10)
    >>> tree.describe()
    'дуб возрастом 10 лет.'
    >>> tree.grow(5)
    >>> tree.age
    15
    >>> tree.grow(-3)
    Traceback (most recent call last):
        ...
    ValueError: Количество лет должно быть положительным.
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

        Примеры:
        >>> tree = Tree("берёза", 7)
        >>> tree.grow(3)
        >>> tree.age
        10
        """
        if years < 0:
            raise ValueError("Количество лет должно быть положительным.")
        self.age += years

    def describe(self) -> str:
        """
        Возвращает описание дерева.

        Примеры:
        >>> tree = Tree("сосна", 20)
        >>> tree.describe()
        'сосна возрастом 20 лет.'
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

    Примеры:
    >>> post = FacebookPost("Привет, мир!")
    >>> post.show()
    'Пост: Привет, мир!\\nЛайки: 0'
    >>> post.like()
    >>> post.likes
    1
    >>> post = FacebookPost("Проверка", -1)
    Traceback (most recent call last):
        ...
    ValueError: Количество лайков не может быть отрицательным.
    """

    def __init__(self, content: str, likes: int = 0):
        if likes < 0:
            raise ValueError("Количество лайков не может быть отрицательным.")
        self.content = content
        self.likes = likes

    def like(self):
        """
        Увеличивает количество лайков.

        Примеры:
        >>> post = FacebookPost("Как дела?")
        >>> post.like()
        >>> post.likes
        1
        """
        self.likes += 1

    def show(self) -> str:
        """
        Возвращает содержимое поста и количество лайков.

        Примеры:
        >>> post = FacebookPost("Фото с отпуска")
        >>> post.show()
        'Пост: Фото с отпуска\\nЛайки: 0'
        """
        return f"Пост: {self.content}\nЛайки: {self.likes}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
