import unittest
import os
import pathlib

import psp

class TestGetSerials(unittest.TestCase):

    def get_test_results(self, filename):
        result_file_name = filename.stem
        result_file = filename.parent / (result_file_name + '.txt')
        with open(result_file, 'r') as f:
            result = f.read().strip()
        result = result.replace(' ', '')
        result = result.split(',')
        return result

    def pdf_file_test(self, filename):
        parser = psp.PackSlipParser(str(filename.resolve()))
        serials, unmatched = parser.get_serial_numbers()
        for i in self.get_test_results(filename):
            self.assertIn(i, serials)

    def test_get_serials(self):
        directory = pathlib.Path(__file__).resolve().parent
        data_dir = directory / 'data'
        print('\033[1E')
        for i in os.listdir(data_dir):
            if '.pdf' in i:
                print('\033[1A\033[0GTesting file:', i)
                self.pdf_file_test(data_dir / i)       
