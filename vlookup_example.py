import python_vlookup

###for faster_vlookup
csv_rows = python_vlookup.get_csv_data('example.csv')
column_dict = python_vlookup.create_column_dict(csv_rows,1)
###

lookup_value = 'outdoor/accessories'
lookup_list = ['bed-and-bath/accessories','bed-and-bath/storage-and-hampers/storage','decor-and-pillows/rugs/hide']


print python_vlookup.vlookup(lookup_value,'example.csv',2)
print python_vlookup.vlookup(lookup_list,'example.csv',3)

print python_vlookup.faster_vlookup(lookup_list,column_dict)
