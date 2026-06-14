from calculator import RPNCalculator
from file_manager import FileManager


def print_menu():
    print("\n" + "=" * 45)
    print(" КАЛЬКУЛЯТОР ОБРАТНОЙ ПОЛЬСКОЙ ЗАПИСИ (RPN)")
    print("=" * 45)
    print("1. Ввести выражение вручную")
    print("2. Загрузить и вычислить выражения из файла")
    print("3. Выход")
    print("=" * 45)


def main():
    calc = RPNCalculator()
    file_manager = FileManager()  # Создаем экземпляр класса
    history_file = "history.txt"

    while True:
        print_menu()
        choice = input("Выберите действие (1-3): ").strip()

        if choice == '1':
            expr = input("\nВведите выражение в постфиксной записи (через пробел): ").strip()
            try:
                result = calc.evaluate(expr)
                print(f"\n[УСПЕХ] Результат: {result}")

                # Сохраняем результат через созданный объект
                file_manager.save_result(history_file, expr, result)
                print(f"[ИНФО] Вычисление сохранено в файл '{history_file}'")
            except (ValueError, ZeroDivisionError) as e:
                print(f"\n[ОШИБКА ВВОДА/ВЫЧИСЛЕНИЯ] {e}")
            except Exception as e:
                print(f"\n[СИСТЕМНАЯ ОШИБКА] {e}")

        elif choice == '2':
            print("\n(Для проверки создайте текстовый файл, где каждое выражение на новой строке)")
            filename = input("Введите имя файла (например, input.txt): ").strip()
            try:
                # Читаем файл через созданный объект
                expressions = file_manager.read_expressions(filename)
                print(f"\n[ИНФО] Считано выражений: {len(expressions)}")
                print("-" * 45)

                for expr in expressions:
                    try:
                        result = calc.evaluate(expr)
                        print(f"{expr}  =>  {result}")
                        file_manager.save_result(history_file, expr, result)
                    except Exception as e:
                        print(f"{expr}  =>  [ОШИБКА] {e}")
                print("-" * 45)
            except (FileNotFoundError, IOError) as e:
                print(f"\n[ОШИБКА ФАЙЛОВОЙ СИСТЕМЫ] {e}")

        elif choice == '3':
            print("\nЗавершение работы программы.")
            break

        else:
            print("\n[ОШИБКА] Некорректный пункт меню. Введите 1, 2 или 3.")


if __name__ == "__main__":
    main()