from abc import ABCMeta, abstractmethod


class PrinterFactory(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def create_printer(self):
        pass
