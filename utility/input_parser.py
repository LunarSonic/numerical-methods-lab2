class InputParser:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def get_choice(self, items, text):
        print(f"\n{text}:")
        for i, item in enumerate(items):
            print(f"{i + 1}. {item}")
        while True:
            try:
                line = input(f"Выберите вариант (1-{len(items)}): ").strip()
                if not line: continue
                choice = int(line)
                if 1 <= choice <= len(items):
                    return choice - 1
                else:
                    print(f"Ошибка: введите число от 1 до {len(items)}")
            except ValueError:
                print("Ошибка: введите 1 целое число")
            except EOFError:
                return None

    def get_equation_parameters(self):
        try:
            params = self.reader.read_floats("Введите начало интервала, конец и точность через пробел: ")
            if params is None:
                print("Ошибка: файл пуст или данные не найдены")
                return None
            if len(params) < 3:
                print(f"Ошибка: в первой строке нужно 3 числа, в файле только {len(params)}")
                return None
            a, b, epsilon = params[0], params[1], params[2]
            if a >= b:
                print("Ошибка: левая граница a должна быть меньше правой границы b")
                return None
            if epsilon <= 0:
                print("Ошибка: точность должна быть положительной")
                return None
            return a, b, epsilon
        except ValueError:
            print("Ошибка: в параметрах должны быть только числа")
            return None
        except Exception as e:
            print(f"Ошибка при чтении параметров: {e}")
            return None

    def get_system_parameters(self, n):
        try:
            params = self.reader.read_floats(f"Введите {n} приближений и точность через пробел: ")
            if params is None:
                print("Ошибка: файл пуст или данные системы не найдены")
                return None
            if len(params) < n + 1:
                print(f"Ошибка: нужно {n + 1} чисел, получено {len(params)}")
                return None
            x_0 = params[:n]
            epsilon = params[-1]
            if epsilon <= 0:
                print("Ошибка: точность должна быть положительной")
                return None
            return x_0, epsilon
        except ValueError:
            print("Ошибка: в параметрах системы должны быть только числа")
            return None
        except Exception as e:
            print(f"Ошибка при чтении параметров системы: {e}")
            return None