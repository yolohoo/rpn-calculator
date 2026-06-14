class FileManager:
    """Класс для обработки файловых операций (сохранение истории и загрузка тестов)."""

    def save_result(self, filename: str, expression: str, result: float):
        try:
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(f"{expression} = {result}\n")
        except Exception as e:
            raise IOError(f"Ошибка при сохранении в файл: {e}")

    def read_expressions(self, filename: str) -> list:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                # Читаем непустые строки
                return [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл '{filename}' не найден.")
        except Exception as e:
            raise IOError(f"Ошибка при чтении файла '{filename}': {e}")