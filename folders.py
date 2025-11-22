6import os


def create_folders():
    try:
        # Запрос количества папок
        num_folders = int(input("Введите количество папок для создания: "))

        # Проверка на положительное число
        if num_folders <= 0:
            print("Ошибка: Введите положительное число.")
            return

        # Запрос префикса для имен папок
        prefix = input("Введите префикс для имен папок (или нажмите Enter для 'folder_'): ").strip()
        if prefix == "":
            prefix = "folder"

        # Создание папок
        for i in range(1, num_folders + 1):
            folder_name = f"{prefix}_{i}" if num_folders > 1 else prefix
            try:
                os.makedirs(folder_name)
                print(f"Создана папка: {folder_name}")
            except FileExistsError:
                print(f"Ошибка: Папка '{folder_name}' уже существует.")
            except Exception as e:
                print(f"Ошибка при создании папки '{folder_name}': {str(e)}")

    except ValueError:
        print("Ошибка: Введите корректное число.")


if __name__ == "__main__":
    create_folders()
