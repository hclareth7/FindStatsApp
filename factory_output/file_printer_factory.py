from factory_output.printer_factory import PrinterFactory
from factory_output.file_printer import FilePrinter


class FilePrinterFactory(PrinterFactory):
    def __init__(self):
        print()

    def create_printer(self):
        return FilePrinter()
