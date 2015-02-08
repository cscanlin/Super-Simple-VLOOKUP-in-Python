import vlookup

lookup_value = 'outdoor/accessories'
lookup_list = ['bed-and-bath/accessories','bed-and-bath/storage-and-hampers/storage','decor-and-pillows/rugs/hide']


print vlookup.vlookup(lookup_value,'example.csv',2)
print vlookup.vlookup(lookup_list,'example.csv',3)
