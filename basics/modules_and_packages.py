import re

# Your code goes here
find_members = [f for f in dir(re) if 'find' in f]

print(find_members)
