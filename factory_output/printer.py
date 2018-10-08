from abc import ABCMeta, abstractmethod


class Printer(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def print(self, data):
        pass
