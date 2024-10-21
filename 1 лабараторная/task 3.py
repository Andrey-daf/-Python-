list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Определение общего количества игроков
total_players = len(list_players)

# Разделение игроков на две равные команды
middle_index = total_players // 2
first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

# Корректная форма вывода
print("['" + "', '".join(first_team) + "']")
print("['" + "', '".join(second_team) + "']")
