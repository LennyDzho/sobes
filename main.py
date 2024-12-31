class Stack:
    def __init__(self, *args):
        self.items = [item for item in args]

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def is_not_balance(self):
        # Считаем количество открывающих и закрывающих скобок
        items_count = {
            '{': 0,
            '}': 0,
            '(': 0,
            ')': 0,
            '[': 0,
            ']': 0
        }

        for item in self.items:
            if item in '({[)}]':
                items_count[item] += 1

        # Проверяем, равны ли количество открывающих и закрывающих скобок для каждого типа
        return items_count['('] == items_count[')'] and \
               items_count['{'] == items_count['}'] and \
               items_count['['] == items_count[']']


def test_stack_balance():
    # Пример сбалансированных последовательностей
    expression1 = Stack('(', '(', '(', '[', '{', '}', '}', ']', ')', ')', ')')
    expression2 = Stack('[', '(', '[', ']', '(', '(', '[', '[', ']', ']', ')', ')', '{', '}', ')')
    expression3 = Stack('{', '{', '[', '(', ')', ']', '}', '}', ')')

    # Пример несбалансированных последовательностей
    expression4 = Stack('}', '{')
    expression5 = Stack('{', '[', '(', ']', ')', '}')
    expression6 = Stack('[', '[', '{', '(', ')', '}', ')', ')')

    print("Тест 1:", expression1.is_not_balance())  # Сбалансированно
    print("Тест 2:", expression2.is_not_balance())  # Сбалансированно
    print("Тест 3:", expression3.is_not_balance())  # Сбалансированно
    print("Тест 4:", expression4.is_not_balance())  # Несбалансированно
    print("Тест 5:", expression5.is_not_balance())  # Несбалансированно
    print("Тест 6:", expression6.is_not_balance())  # Несбалансированно

# Запуск тестов
if __name__ == '__main__':
    test_stack_balance()
