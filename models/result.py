class Result:
    def __init__(self, x, iterations, log, f_x=None):
        self.x = x
        self.iterations = iterations
        self.log = log
        self.f_x = f_x