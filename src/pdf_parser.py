import pdfminer.high_level
import re
import csv

# mp = [
#     '(\d{4}-\d{4}-\d{8})',
#     '(\d{4}-\d{4}-\d{7})',
#     '(\d{4}-\d{4}[*])',
#     '(\d{4}-\d{8})'
# ]


class Pattern:
    def __init__(self, regex, length):
        self.regex = regex
        self.length = length
    
class PDF_Parser:
    def __init__(self):
        self.part_num_lst = list()
        self.mp = list()
        self.text = None
    
    def extract_text(self, file_name:str):
        t = pdfminer.high_level.extract_text(str('src/' + file_name + '.pdf')) # Extracts the pdf into a block of text and saves it as a str var
        t = t.split(' ') # Splits the whole block of text into a list of strings by splitting it where a space is
        self.text = t

    def check_str(self, line):
        # Checks to see if we can find any matches for any pattern. If a match is found then we'll need to save that part number
        matches = False
        for pattern in self.mp:
            if re.search(pattern.regex, line) is not None:
                matches = True
        if matches is False:
            return
        for pattern in self.mp:
            while re.search(pattern.regex, line) is not None:
                print(pattern.length)
                part = re.search(pattern.regex, line)
                part_num = part.group()[0:pattern.length]
                line = line.replace(part_num, "")
                self.part_num_lst.append(part_num)

    def generate_csv_file(self, csv_file_name:str):
        """
        Generates a csv file with a column that has each part number found in the pdf

        Args:
            csv_file_name (str): Name of the file that will be generated
        """
        fields = ['Part Numbers']
        with open(csv_file_name, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fields, lineterminator = '\n')
            writer.writeheader()
            for part_num in self.part_num_lst:
                writer.writerow({fields[0]: part_num})

    def parse_input(self, string:str):
        pattern = ''
        length = 0
        for index, letter in enumerate(string):
            if letter.isdigit():
                pattern += '\d'
            elif letter.isalpha():
                if letter.isupper():
                    pattern += '[A-Z]'
                else:
                    pattern += '[a-z]'
            else:
                pattern += f'[{letter}]'
            length += 1
        if len(self.text) > 50 and string[index].isdigit():
            pattern += '\d\d\d\d'
        print(pattern)
        self.mp.append(Pattern(pattern, length))
        

if __name__ == "__main__":
    parser = PDF_Parser()
    file_name = '702-N Parts Breakdown' #TODO make this an input
    parser.extract_text(file_name)
    while True:
        example_ptn = input("Please enter the pattern you would like to search for. (0 - Quit) : ")
        if example_ptn == '0':
            break
        else:
            parser.parse_input(example_ptn)
    for i in parser.text:
        parser.check_str(i) # Checks each str to see if it is a part number
    parser.generate_csv_file(file_name + '.csv')