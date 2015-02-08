import python_vlookup

lookup_value = 'outdoor/accessories'
lookup_list = ['bed-and-bath/accessories','bed-and-bath/storage-and-hampers/storage','decor-and-pillows/rugs/hide']


print python_vlookup.vlookup(lookup_value,'example.csv',2)
print python_vlookup.vlookup(lookup_list,'example.csv',3)
