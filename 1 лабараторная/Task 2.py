# TODO Найдите количество книг, которое можно разместить на дискете
# Данные задачи
disk_size_mb = 1.44  # Объём дискеты в мегабайтах
pages_per_book = 100  # Количество страниц в книге
lines_per_page = 50  # Число строк на странице
chars_per_line = 25  # Количество символов в строке
bytes_per_char = 4  # Количество байт на символ

# Переводим объём дискеты в байты
disk_size_bytes = disk_size_mb * 1024 * 1024

# Вычисляем объём одной книги в байтах
book_size_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char

# Вычисляем, сколько книг помещается на дискету
books_on_disk = disk_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(books_on_disk))

