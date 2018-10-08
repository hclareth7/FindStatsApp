from factory_output.printer_factory import PrinterFactory
from factory_output.console_printer import ConsolePrinter


class ConsolePrinterFactory(PrinterFactory):
    def __init__(self):
        pass

    def create_printer(self):
        return ConsolePrinter()
