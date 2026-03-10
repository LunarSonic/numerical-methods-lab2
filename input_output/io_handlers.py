from input_output.interfaces import BaseReader, BaseWriter

class ConsoleReader(BaseReader):
    def read_line(self, text=""):
        return input(text).strip()

    def read_floats(self, text):
        line = self.read_line(text)
        if not line:
            return None
        clean_line = line.replace(',', ' ')
        try:
            return [float(x) for x in clean_line.split()]
        except ValueError:
            raise ValueError("Необходимо вводить только числа")

class FileReader(BaseReader):
    def __init__(self, path):
        self.file = open(path, "r", encoding="utf-8")

    def read_line(self, text=""):
        line = self.file.readline()
        if line:
            return line.strip()
        else:
            return None

    def read_floats(self, text=""):
        line = self.read_line()
        if line:
            try:
                return list(map(float, line.replace(",", ".").split()))
            except ValueError:
                raise ValueError("Ошибка чтения чисел из файла")
        else:
            return None

class ConsoleWriter(BaseWriter):
    def write(self, message):
        print(message)

class FileWriter(BaseWriter):
    def __init__(self, path):
        self.path = path
        self.file = open(path, "w", encoding="utf-8")

    def write(self, message):
        self.file.write(str(message) + "\n")

    def close(self):
        if not self.file.closed:
            self.file.close()