from stack import Stack


class RPNCalculator:
    """Класс для вычисления арифметических выражений в обратной польской записи."""

    def __init__(self):
        self.valid_operators = {'+', '-', '*', '/'}

    def evaluate(self, expression: str) -> float:
        if not expression.strip():
            raise ValueError("Выражение не может быть пустым.")

        stack = Stack()
        tokens = expression.split()

        for token in tokens:
            if self._is_valid_operand(token):
                stack.push(float(token))
            elif token in self.valid_operators:
                if len(stack) < 2:
                    raise ValueError("Недостаточно операндов для выполнения операции.")

                # Порядок извлечения важен для деления и вычитания
                b = stack.pop()
                a = stack.pop()
                result = self._apply_operator(a, b, token)
                stack.push(result)
            else:
                raise ValueError(
                    f"Некорректный токен: '{token}'. Разрешены только положительные вещественные числа и знаки операций.")

        # В конце в стеке должен остаться ровно один элемент — результат
        if len(stack) != 1:
            raise ValueError(
                "Некорректное выражение: после вычисления остались лишние операнды или не хватает операторов.")

        return stack.pop()

    def _is_valid_operand(self, token: str) -> bool:
        try:
            val = float(token)
            return val > 0
        except ValueError:
            return False

    def _apply_operator(self, a: float, b: float, operator: str) -> float:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Ошибка: Деление на ноль.")
            return a / b
        raise ValueError(f"Неизвестный оператор: {operator}")