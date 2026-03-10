import os
import numpy as np

from input_output.io_handlers import ConsoleReader, ConsoleWriter, FileReader, FileWriter
from constants.settings import LOG_DECIMALS
from constants.config import EQUATIONS, SYSTEMS, EQ_METHODS, SYS_METHODS
from core.methods_for_systems import newton_method_for_system
from core.methods_for_equations import chord_method, newton_method, simple_iteration_method
from utility.input_parser import InputParser
from utility.drawer import draw_equation, draw_system

def main():
    print("Решение нелинейных уравнений и систем")
    try:
        while True:
            while True:
                print("\nВыберите способ ввода данных:")
                print("1 - консоль, 2 - файл")
                in_type = input("> ").strip()
                if in_type == "1":
                    reader = ConsoleReader()
                    break
                elif in_type == "2":
                    path = input("Введите путь к файлу для ввода: ").strip()
                    if not os.path.exists(path):
                        print(f"Ошибка: файл '{path}' не найден. Повторите ввод")
                        continue
                    reader = FileReader(path)
                    break
                else:
                    print("Ошибка: введите 1 или 2")

            while True:
                print("\nВыберите способ вывода результатов:")
                print("1 - консоль, 2 - файл")
                out_type = input("> ").strip()
                if out_type == "1":
                    writer = ConsoleWriter()
                    break
                elif out_type == "2":
                    path = input("Введите путь к файлу для вывода: ").strip()
                    writer = FileWriter(path)
                    break
                else:
                    print("Ошибка: введите 1 или 2")
            parser = InputParser(reader, writer)

            while True:
                print("\nЧто вы хотели бы решить?")
                print("1 - нелинейное уравнение, 2 - система нелинейных уравнений")
                mode = input("> ").strip()
                if mode in ("1", "2"):
                    break
                print("Ошибка: введите 1 или 2")
            if mode == "1":
                eq_ind = parser.get_choice(EQUATIONS, "Выберите уравнение")
                if eq_ind is None: continue
                equation = EQUATIONS[eq_ind]
                m_ind = parser.get_choice(EQ_METHODS, "Выберите метод решения")
                if m_ind is None: continue
                res = None

                while True:
                    params = parser.get_equation_parameters()
                    if params is None:
                        if isinstance(reader, ConsoleReader):
                            continue
                        break
                    a, b, epsilon = params
                    if not equation.is_single_root_exist(a, b):
                        print(f"Ошибка: на отрезке [{a}, {b}] нет корней или их больше одного")
                        if isinstance(reader, FileReader): break
                        continue
                    try:
                        if m_ind == 0:
                            res = chord_method(equation, a, b, epsilon)
                        elif m_ind == 1:
                            res = newton_method(equation, a, b, epsilon)
                        else:
                            res = simple_iteration_method(equation, a, b, epsilon)
                        break
                    except Exception as e:
                        print(f"Ошибка: {e}")
                        if isinstance(reader, FileReader): break
                        continue
                if res:
                    writer.write(f"Уравнение: {equation.description}")
                    writer.write(f"Метод: {EQ_METHODS[m_ind]}")
                    writer.write(f"Найденный корень: x = {round(res.x, LOG_DECIMALS)}")
                    writer.write(f"Значение функции в корне f(x): {format(res.f_x, f'.{LOG_DECIMALS}f')}")
                    writer.write(f"Число итераций: {res.iterations}")
                    writer.write_table(res.log)
                    draw_equation(res.x, a, b, equation)
            else:
                sys_ind = parser.get_choice(SYSTEMS, "Выберите систему уравнений")
                if sys_ind is None: continue
                system = SYSTEMS[sys_ind]
                print(f"\nИспользуется {SYS_METHODS[0]}")
                res = None

                while True:
                    params = parser.get_system_parameters(system.n)
                    if params is None:
                        if isinstance(reader, ConsoleReader):
                            continue
                        break
                    x_0, epsilon = params
                    try:
                        res = newton_method_for_system(system, x_0, epsilon)
                        break
                    except Exception as e:
                        print(f"Ошибка: {e}")
                        if isinstance(reader, FileReader): break
                        print("Попробуйте другие начальные приближения")
                if res:
                    rounded_x = np.round(res.x, LOG_DECIMALS).tolist()
                    writer.write(f"\nВектор решения: {rounded_x}")
                    writer.write(f"Число итераций: {res.iterations}\n")
                    writer.write_table(res.log)
                    check = system.get_value(res.x)
                    rounded_check = np.round(check, LOG_DECIMALS).tolist()
                    writer.write(f"Вектор невязок: {rounded_check}")
                    if isinstance(writer, FileWriter):
                        writer.close()
                        print(f"\nРезультаты успешно сохранены в файл")
                    draw_system(res.x, x_0, system)
                else:
                    if isinstance(writer, FileWriter):
                        writer.close()

            print("\nХотите ли вы решить ещё один пример?")
            print("1 - да, 0 - выйти")
            if input("> ").strip() != "1":
                break
    except (KeyboardInterrupt, EOFError):
        print("Программа завершена пользователем")

if __name__ == "__main__":
    main()