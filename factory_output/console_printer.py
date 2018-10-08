from factory_output.printer import Printer


class ConsolePrinter(Printer):
    def __init__(self):
        pass

    def print(self, data):
        print(data)
