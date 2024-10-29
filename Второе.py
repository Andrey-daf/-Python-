# TODO Напишите функцию find_common_participants


def find_common_participants(first_group: str, second_group: str, separator: str = ",") -> list:

    # Преобразуем строки в множества
    first_set = set(first_group.split(separator))
    second_set = set(second_group.split(separator))

    # Находим пересечение множеств и преобразуем в отсортированный список
    common_participants = sorted(list(first_set & second_set))

    return common_participants


# Тесты
def test_find_common_participants():
    # Тест 1: Базовый тест с разделителем по умолчанию
    test1_group1 = "Иванов,Петров,Сидоров"
    test1_group2 = "Петров,Сидоров,Смирнов"
    assert find_common_participants(test1_group1, test1_group2) == ["Петров", "Сидоров"]

    # Тест 2: Тест с другим разделителем
    test2_group1 = "Иванов|Петров|Сидоров"
    test2_group2 = "Петров|Сидоров|Смирнов"
    assert find_common_participants(test2_group1, test2_group2, "|") == ["Петров", "Сидоров"]

    # Тест 3: Тест без общих участников
    test3_group1 = "Иванов,Петров"
    test3_group2 = "Сидоров,Смирнов"
    assert find_common_participants(test3_group1, test3_group2) == []

    # Тест 4: Тест с одним общим участником
    test4_group1 = "Иванов,Петров"
    test4_group2 = "Петров,Смирнов"
    assert find_common_participants(test4_group1, test4_group2) == ["Петров"]

    print("Все тесты пройдены успешно!")



# TODO Провеьте работу функции с разделителем отличным от запятой


# Запуск тестов
if __name__ == "__main__":
    test_find_common_participants()

    # Пример использования
    participants_first_group = "Иванов|Петров|Сидоров"
    participants_second_group = "Петров|Сидоров|Смирнов"
    result = find_common_participants(participants_first_group, participants_second_group, "|")
    print(f"Общие участники: {result}")

