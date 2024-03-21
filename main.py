from app.io.input import input_from_console, read_from_file, read_with_pandas
from app.io.output import output_to_console, write_to_file


def main():
    # Ввод тексту з консолі
    text_from_console = input_from_console()
    output_to_console(text_from_console)
    write_to_file(text_from_console)

    # Зчитування тексту з файлу
    text_from_file = read_from_file()
    output_to_console(text_from_file)
    write_to_file(text_from_file)

    # Зчитування тексту з файлу за допомогою pandas
    data_frame = read_with_pandas()
    output_to_console("Зчитаний DataFrame з файлу: ")
    output_to_console(data_frame)

main()