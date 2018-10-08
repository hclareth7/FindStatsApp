import datetime
import errno
import os
from pathlib import Path

from factory_output.printer import Printer


class FilePrinter(Printer):
    def __init__(self):
        pass

    def print(self, data):
        path = f"{str(Path.home())}/Desktop/FindStatsApp"
        FilePrinter._mkdir_p(path)
        now = datetime.datetime.now()
        file_name = f"{path}/{str(now.strftime('%Y_%m_%d_%HH_%MM_%SS'))}.txt"
        with open(file_name, "w") as file:
            file.write(f"{str(data)}")
            file.close()

    @staticmethod
    def _mkdir_p(path):
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise
