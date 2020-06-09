import pdfminer.high_level
import re
import csv

part_num_lst = list() # Creates a list var that will hold each part number that matches the format
mp = [
    '(\d{4}-\d{4}-\d{8})',
    '(\d{4}-\d{4}-\d{7})',
    '(\d{4}-\d{4}[*])',
    '(\d{4}-\d{8})'
]

def check_str(line):
    # Checks to see if we can find any matches for any pattern. If a match is found then we'll need to save that part number
    if re.search(mp[0], line) is None and re.search(mp[1], line) is None and re.search(mp[2], line) is None and re.search(mp[3], line) is None:
        return
    else:
        """
            For each pattern, we search to see if we can find a match.
            If a match is found, then that part number is added to the list and removed from the overall text
        """
        while re.search(mp[0], line) is not None:
            part = re.search(mp[0], line)
            part_num = part.group()[0:14]
            line = line.replace(part_num, "")
            part_num_lst.append(part_num)

        while re.search(mp[1], line) is not None:
            part = re.search(mp[1], line)
            part_num = part.group()[0:13]
            line = line.replace(part_num, "")
            part_num_lst.append(part_num)

        while re.search(mp[2], line) is not None:
            part = re.search(mp[2], line)
            part_num = part.group()[0:10]
            line = line.replace(part_num, "")
            part_num_lst.append(part_num)

        while re.search(mp[3], line) is not None:
            part = re.search(mp[3], line)
            part_num = part.group()[0:9]
            line = line.replace(part_num, "")
            part_num_lst.append(part_num)

def generate_csv_file(csv_file_name:str):
    """
    Generates a csv file with a column that has each part number found in the pdf

    Args:
        csv_file_name (str): Name of the file that will be generated
    """
    fields = ['Part Numbers']
    with open(csv_file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields, lineterminator = '\n')
        writer.writeheader()
        for part_num in part_num_lst:
            writer.writerow({fields[0]: part_num})

def main():
    file_name = '702-N Parts Breakdown'
    t = pdfminer.high_level.extract_text(str(file_name + '.pdf')) # Extracts the pdf into a block of text and saves it as a str var
    t=t.split(' ') # Splits the whole block of text into a list of strings by splitting it where a space is
    for i in t:
        check_str(i) # Checks each str to see if it is a part number
    generate_csv_file(file_name + '.csv')
    
main()