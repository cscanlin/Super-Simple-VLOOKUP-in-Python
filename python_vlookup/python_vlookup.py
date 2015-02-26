import csv

# Returns a list of lists, where each row is a sublist
def get_csv_data(csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        csv_rows = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
    return csv_rows

# Creates a dictionary with the first list item as the key,
# and the value based on the column index input
def create_column_dict(csv_rows, index):
    column_dict = {row[0]: row[index] for row in csv_rows}
    return column_dict

# Returns the Looked up value as a list or string
def vlookup(item,csv_file_path,col_index_num):
    csv_rows = get_csv_data(csv_file_path)
    column_dict = create_column_dict(csv_rows,col_index_num-1)

    if isinstance(item, list):
        return [column_dict[str(key)] for key in item]

    return column_dict[str(item)]

# faster_vlookup allows you to call each function individually.
# You can use the two helper functions to create your array and dictionary only once,
# and then call faster_vlookup which is a much quicker
# Useful for using in loops.
def faster_vlookup(item,column_dict):
    if isinstance(item, list):
        return [column_dict[str(key)] for key in item]
    return column_dict[str(item)]
