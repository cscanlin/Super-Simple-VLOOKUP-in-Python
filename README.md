# Super-Simple-VLOOKUP-in-Python


Doesn't get any simpler than this. Pretty much an exact replica of VLOOKUP in Excel, except no fuzzy matching (...yet). I needed this for a project and was surprised I couldn't find any other prebuilt way to do it. I decided to loosely package it up so other can use it, but it's not very sophisticated so I would be careful installing it in any mission critical infrastructure.

Here's the example file from this repository

      import vlookup
      
      lookup_value = 'outdoor/accessories'
      lookup_list = ['bed-and-bath/accessories','bed-and-bath/storage-and-hampers/storage','decor-and-pillows/rugs/hide']
      
      
      print vlookup.vlookup(lookup_value,'example.csv',2)
      print vlookup.list_vlookup(lookup_list,'example.csv',3)
      
There are currently two seperate funtions: vlookup, and list lookup.

vlookup takes a string as the first argument, and list_lookup takes a list (surpised?). They both then take a csv file from the same directory as the table array, and the a column index number to lookup on.

The major difference is that the csv file is opened once each function call so the list_lookup is much more efficient for looking up many things. Keep in mind the csv is opened EVERY time the either funtion is called which could get a bit slow if used in a loop.


