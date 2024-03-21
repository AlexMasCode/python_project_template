import pandas as pd
def input_from_console():
    """
    Функція для вводу тексту з консолі.

    Returns:
        str: Введений текст.
    """
    user_input = input("Введіть текст з консолі: ")
    return user_input

def read_from_file():
    """
    Функція для зчитування тексту з файлу за допомогою Python.
    """
    with open("output.txt", "r") as file:
        file_content = file.read()
    return file_content



def read_with_pandas():
    """
    Функція для зчитування тексту з файлу за допомогою бібліотеки pandas.

    Returns:
        pandas.DataFrame: Зміст файлу у вигляді DataFrame.
    """
    file_data = pd.read_csv("output.txt", sep="\n", header=None)
    return file_data
