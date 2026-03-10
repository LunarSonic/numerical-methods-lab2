import numpy as np

from abc import ABC, abstractmethod
from constants.settings import LOG_DECIMALS

class BaseReader(ABC):
    @abstractmethod
    def read_line(self, text=None):
        pass

    def read_floats(self, text=None):
        line = self.read_line(text)
        if not line:
            return None
        clean_line = line.replace(",", " ")
        try:
            return [float(x) for x in clean_line.split()]
        except ValueError:
            raise ValueError("Необходимо вводить только числа")

class BaseWriter(ABC):
    @abstractmethod
    def write(self, message):
        pass

    def write_table(self, log):
        if not log:
            return
        headers = log[0].keys()
        fmt_header = " | ".join([f"{h:^12}" for h in headers])
        separator = "-" * len(fmt_header)
        self.write(separator)
        self.write(fmt_header)
        self.write(separator)
        for row in log:
            formatted = []
            for v in row.values():
                if isinstance(v, float):
                    value = f"{v:.{LOG_DECIMALS}f}"
                elif isinstance(v, (list, tuple, np.ndarray)):
                    arr = np.array(v)
                    value = "[" + ", ".join(f"{x:.{LOG_DECIMALS}f}" for x in arr) + "]"
                else:
                    value = str(v)
                formatted.append(f"{value:^12}")
            self.write(" | ".join(formatted))
        self.write(separator)

