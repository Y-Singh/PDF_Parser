import psp
import sys

def print_per_line(data, num_per_line):
    """Prints data in columns

        Args:
            data (list): The data to print (usually with __str__ defined)
            num_per_line (int): The number to print per line
    """
    if len(data) < 1:
        return
    data_index = 0
    num_printed = 0
    while data_index < len(data):
        if num_printed == num_per_line - 1 or data_index == len(data) - 1:
            print(data[data_index])
            num_printed = -1
        else:
            print(data[data_index], end=", ")
        data_index += 1
        num_printed += 1

if len(sys.argv) < 2:
    print("Pass the name of the file to parse")
    sys.exit(1)

filename = sys.argv[1]
parser = psp.PackSlipParser(filename)
serials, unmatched = parser.get_serial_numbers()
print()
print("\033[1m\033[94mSerials found:", len(serials), "\033[0m")
print_per_line(serials, 5)
if len(unmatched) > 0:
    print()
    print("\033[1m\033[91mWarning, unmatched serials found:\033[0m")
    print_per_line(unmatched, 5)
