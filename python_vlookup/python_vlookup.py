from __future__ import print_function
from builtins import input
from collections import Iterable

import csv

# Returns a list of lists, where each row of the csv is a sublist
def get_csv_data(csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        csv_rows = [row for row in csv.reader(csvfile.read().splitlines())]
    return csv_rows

# Creates a dictionary with the first list item as the key,
# and the value based on the column index input
def create_column_dict(csv_rows, index):
    column_dict = {row[0]: row[index] for row in csv_rows}
    return column_dict

# faster_vlookup allows you to call each function individually.
# You can use the two helper functions to create your array and dictionary only once,
# and then call faster_vlookup which is a much quicker
# Useful for using in loops.
def faster_vlookup(item, column_dict, debug=None, error_value=None):
    try:
        if isinstance(item, Iterable) and not isinstance(item, str):
            return [column_dict[str(entry)] for entry in item]
        else:
            return column_dict[str(item)]
    except KeyError:
        if debug == 'skip':
            if isinstance(item, Iterable) and not isinstance(item, str):
                    return [column_dict[str(entry)] if str(entry) in column_dict else error_value for entry in item]
            else:
                return error_value
        else:
            raise

# Returns the Looked up value as a list or string, uses excel column index numbering (no 0 column).
# If debug is on, the user is prompted to enter values for missing entries
def vlookup(item, csv_file_path, col_index_num, debug=None, error_value=None):
    csv_rows = get_csv_data(csv_file_path)
    column_dict = create_column_dict(csv_rows, col_index_num-1)

    try:
        if isinstance(item, Iterable) and not isinstance(item, str):
            return [column_dict[str(entry)] for entry in item]
        else:
            return column_dict[str(item)]
    except KeyError as e:
        if debug == 'fix':
            entry = str(e)[1:-1]
            debug_lookup(entry, csv_file_path)
            return vlookup(item, csv_file_path, col_index_num, debug='fix')
        if debug == 'skip':
            if isinstance(item, Iterable) and not isinstance(item, str):
                    return [column_dict[str(entry)] if str(entry) in column_dict else error_value for entry in item]
            else:
                return error_value
        else:
            raise

def debug_lookup(entry, csv_file_path):
    print('LOOKUP ENTRY MISSING')
    new_entry = [entry]
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for column_heading in next(reader)[1:]:
            print('Enter {0} for {1}:'.format(column_heading, entry))
            column_entry = input()
            new_entry.append(column_entry)
    with open(csv_file_path, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_entry)
