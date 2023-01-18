# -*- coding: utf-8 -*-
"""
This is file shares useful python functions and other notes for quick reference
"""

# Get more information about a function with ?, or wrapping it in help()
?pow
help(pow)

# Check data type
type(x)

# Convert between types
x = bool(1)
x = float(3.2)
x = str("Test string")
x = int(4.9)  # does not round up!

# Install package - using pip (you might have to first install pip yo install other libraries)
pip3 install numpy


""" Method/Functions for list types  """ # =============================================================================

# Concatenate two lists (can be strings, or numbers)
list3 = list1 + list2

# Append new element to list
x.append("hello")

# Check list object for the index of a number or string
x.index("hello") 

# Count number of times a value appears in a list
x.count(1.73)

# Remove the first element of a list that matches the input
x.remove("hello")

# Reverse order of the list
x.reverse()


""" Method/Functions for string types  """ # =============================================================================

# Capitalize first word only
x.capitalize()

# Replace strings
x.replace("z", "sa") # replace z with sa

# Check index of a particular character/string
x.index("a")


""" Importing Python Libraries or functions from libraries """ # =============================================================================

# Import radians function of math package
from math import radians



""" numpy objects/methods/functions  """ # =============================================================================

# Create a np.array
x = np.array([1, 2, 3])


""" pandas objects/methods/functions  """ # =============================================================================

# Write csv. This only works if your writing a pd.DataFrame object!
df.to_csv("filename.csv")

# Select only numeric columbns
df1 = df.select_dtypes(include=np.number)
df1 = df.select_dtypes(include=np.'int64')
df1 = df.select_dtypes(include=np.'datetime64[ns]')

# Look at columns
df1.columns

# More neatly view of col names
for col in df1.columns:
    print(col)

# =============================================================================

""" Useful shortcuts """
#
# Single line comment:        ctrl + 1    
# Multi-line comment:         ctrl + 4
# Unblock multi-line comment: ctrl + 5
# 
# =============================================================================


# =============================================================================

""" Other Random Notes to remember! """

# # Methods: Functions that belong to objects
# # Modules: Python scripts which are read in from various Python libraries
# # 
# # 
# # 
# =============================================================================

