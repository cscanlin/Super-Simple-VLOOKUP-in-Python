import csv

def create_lookup_array(lookup_csv):
    with open(lookup_csv, 'rb') as csvfile:
        lookup_array = []
        lookup_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for lookup_entry in lookup_reader:
            lookup_array.append(lookup_entry)
        return lookup_array

def create_lookup_dict(lookup_array,lookup_index):
    lookup_dict = {}
    for lookup_entry in lookup_array:
        lookup_dict[lookup_entry[0]] = lookup_entry[int(lookup_index)]
    return lookup_dict


def vlookup(lookup_value,lookup_csv,col_index_num):
    lookup_array = create_lookup_array(lookup_csv)
    lookup_dict = create_lookup_dict(lookup_array,col_index_num-1)

    return lookup_dict[lookup_value]

def list_vlookup(lookup_value_list,lookup_csv,col_index_num):
    lookup_array = create_lookup_array(lookup_csv)
    lookup_dict = create_lookup_dict(lookup_array,col_index_num-1)

    looked_up_list = []

    for lookup_value in lookup_value_list:
        looked_up_list.append(lookup_dict[lookup_value])
    return looked_up_list
