# Super-Simple-VLOOKUP-in-Python


Doesn't get any simpler than this. Pretty much an exact replica of VLOOKUP in Excel, except no fuzzy matching (...yet). I needed this for a project and was surprised I couldn't find any other prebuilt way to do it. I decided to loosely package it up so other can use it, but it's not very sophisticated so I would be careful installing it in any mission critical infrastructure.

Install with pip

      pip install python_vlookup

Here's the example file from this repository

      from python_vlookup import python_vlookup

      lookup_value = 'outdoor/accessories'
      lookup_list = ['bed-and-bath/accessories','bed-and-bath/storage-and-hampers/storage','decor-and-pillows/rugs/hide']

      print python_vlookup.vlookup(lookup_value,'example.csv',2)
      print python_vlookup.vlookup(lookup_list,'example.csv',3)

vlookup takes either a string or a list as the first argument. It then takes a csv file from the same directory as the table array, and then a column index number to lookup on.

The csv file is opened once each function call so the list lookup is much more efficient for looking up many things. Keep in mind the csv is opened EVERY time the function is called which could make things a bit slow if used in a loop.

It works by creating a list of lists from the csv where each row is it's own list. It then creates a dictionary with the first list item as the key, and the value based on the column index input. Finally, it returns the value as a list or string.

faster_vlookup allows you to call each function individually. You can use the two helper functions to create your array and dictionary only once, and then call faster_vlookup which is a much quicker as it's just a dictionary search. Useful for using in loops.
