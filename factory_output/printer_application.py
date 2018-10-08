from factory_output.printer_factory import PrinterFactory


class PrinterApplication:
    def __init__(self, printer_factory: PrinterFactory):
        self.printer = printer_factory.create_printer()

    def print(self, data):
        self.printer.print(data)
