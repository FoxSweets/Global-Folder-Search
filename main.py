from pathlib import Path
from configparser import ConfigParser
import collections
import os
import time


def record_server(key: str, value: str) -> None:
    config = ConfigParser()
    config.read("example.ini")
    config["DEFAULT"][key] = value
    with open("example.ini", "w") as configfile:
        config.write(configfile)
    print("Файл успешно записан")


def search_server(search):
    config = ConfigParser()
    config.read("example.ini")
    try:
        path_file = config["DEFAULT"][search]
    except KeyError:
        path_file = 'None'
    if not os.path.exists(path_file):
        disk_file = ["C:/", "D:/"]
        for disk in disk_file:
            disk = Path(disk)
            for file in disk.rglob("*"):
                print(file)
                if str(file).endswith(search):
                    record_server(search, str(file))
                    break
        else:
            print("Такой файл не найден")
    else:
        print("Такой файл уже есть")


def main():
    temp_time = time.perf_counter()
    print('Начало')
    search_server("Discord.exe")  # Название файла или программы
    print('Конец')
    print(f"{(time.perf_counter() - temp_time):.02f}")


if __name__ == "__main__":
    main()
