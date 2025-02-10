class ConiferousTree:
    """
    Базовый класс для представления хвойных деревьев.

    Атрибуты:
        name (str): Название дерева.
        height (float): Высота дерева в метрах.
        age (int): Возраст дерева в годах.
    """

    def __init__(self, name: str, height: float, age: int):
        """
        Инициализация базового класса хвойного дерева.

        """
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        """
        Возвращает строковое представление хвойного дерева.

        Возвращает:
            str: Строковое представление дерева.
        """
        return f"{self.name} высотой {self.height} м и возрастом {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление хвойного дерева.

        Возвращает:
            str: Официальное строковое представление дерева.
        """
        return f"ConiferousTree(name={self.name}, height={self.height}, age={self.age})"

    def grow(self) -> str:
        """
        Метод для роста дерева.

        Возвращает:
            str: Сообщение о росте дерева.
        """
        return f"{self.name} растёт."


class Spruce(ConiferousTree):
    """
    Дочерний класс для представления ели.

    Атрибуты:
        name (str): Название дерева.
        height (float): Высота дерева в метрах.
        age (int): Возраст дерева в годах.
        needle_length (float): Длина хвои в сантиметрах.
    """

    def __init__(self, name: str, height: float, age: int, needle_length: float):
        """
        Инициализация дочернего класса ели.

        Аргументы:
            name (str): Название дерева.
            height (float): Высота дерева в метрах.
            age (int): Возраст дерева в годах.
            needle_length (float): Длина хвои в сантиметрах.
        """
        super().__init__(name, height, age)
        self.needle_length = needle_length

    def __str__(self) -> str:
        """
        Возвращает строковое представление ели.

        Возвращает:
            str: Строковое представление ели.
        """
        return f"{self.name} высотой {self.height} м, возрастом {self.age} лет и длиной хвои {self.needle_length} см"

    def grow(self) -> str:
        """
        Перегруженный метод для роста ели.

        Возвращает:
            str: Сообщение о росте ели.
        """
        return f"{self.name} растёт медленно и имеет длинную хвою."


if __name__ == "__main__":
    tree = ConiferousTree("Сосна", 15.5, 20)
    print(tree)
    print(tree.grow())

    spruce = Spruce("Ель", 12.0, 15, 2.5)
    print(spruce)
    print(spruce.grow())