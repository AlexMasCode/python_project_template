def output_to_console(text):
    """
    Функція для виводу тексту у консоль.

    Args:
        text (str): Текст для виводу.
    """
    print(text)

def write_to_file(text):
    """
    Функція для запису до файлу за допомогою вбудованих можливостей Python.

    Args:
        text (str): Текст для запису.
    """
    with open("output.txt", "w") as file:
        file.write(text)
