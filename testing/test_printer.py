from unittest import TestCase
from printer import Printer, PrinterError

class TestPrinter(TestCase):
    def setUp(self) -> None:
        self.printer = Printer(pages_per_s=2.0, capacity=300)

    def test_print_within_capacity(self):
        message = self.printer.print(25)
        self.assertEqual(f"Printed 25 pages in 12.50 seconds.", message)

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)
        