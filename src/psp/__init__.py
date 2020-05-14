import re

import pdfminer.high_level

class PackSlipParser:
    matching_patterns = [
            '\d{1,5}[A-Z]\d{1,5}',
            '\w+MD\d{4}-\d{4}?(?!\/)(-\d{2})?(?!\/)\w+',
        ]
    def __init__(self, filename):
        self.filename = filename
        self.matching_re = list()
        for i in self.matching_patterns:
            compiled_re = re.compile(i)
            self.matching_re.append(compiled_re)

    def get_file_text(self):
        """Gets the text from the pdf file"""
        return pdfminer.high_level.extract_text(self.filename)

    def get_pdf_paragraphs(self):
        """In pdfminer paragraphs are separated by \n\n characters"""
        text = self.get_file_text()
        text = text.split("\n\n")
        return text

    def string_is_serial_number(self, string):
        """Determines if a given string is a serial number"""
        for i in self.matching_re:
            if i.match(string):
                return True
        return False

    def is_serial_numbers_paragraph(self, paragraph):
        """Determines if a paragraph contains serial numbers"""
        for i in self.matching_re:
            if i.search(paragraph):
                return True
        return False

    def find_possible_serial_number_paragraphs(self, paragraphs):
        """Finds any paragraphs that may have serial numbers"""
        possible = list()
        for paragraph in paragraphs:
            if self.is_serial_numbers_paragraph(paragraph):
                possible.append(paragraph)
        return possible

    def extract_serial_numbers(self, paragraph):
        """Extracts serial numbers from a string

        Returns:
            tuple: (matched serial numbers, unmatched values)
        """
        serial_numbers = list()
        unmatched = list()
        split_re = re.compile('[,\n ]')
        sn_string = split_re.split(paragraph)

        sn_string = [i for i in sn_string if i != '']

        for i in sn_string:
            if self.string_is_serial_number(i):
                serial_numbers.append(i)
            else:
                unmatched.append(i)
        return serial_numbers, unmatched

    def get_serial_numbers(self):
        """Gets serial numbers from the pdf file

        Returns:
            tuple: (matched serial numbers, unmatched values)
                unmatched values were in the serial num paragraph but did
                not match the regex to make them a valid serial number
        """
        paragraphs = self.get_pdf_paragraphs()
        possible = self.find_possible_serial_number_paragraphs(paragraphs)

        if len(possible) == 0:
            raise Exception("Failed to parse serial numbers")
        serial_numbers, unmatched = list(), list()
        for i in possible:
            tmp_serial_numbers, tmp_unmatched = self.extract_serial_numbers(i)
            serial_numbers += tmp_serial_numbers
            unmatched += tmp_unmatched
        return serial_numbers, unmatched
