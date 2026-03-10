from input_output.interfaces import BaseReader, BaseWriter

class ConsoleReader(BaseReader):
    def read_line(self, text=""):
        return input(text).strip()

class FileReader(BaseReader):
    def __init__(self, path):
        self.file = open(path, "r", encoding="utf-8")

    def read_line(self, text=""):
        line = self.file.readline()
        if line:
            return line.strip()
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