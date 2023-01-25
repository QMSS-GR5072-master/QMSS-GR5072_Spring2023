# -*- coding: utf-8 -*-
"""
This is file shares useful python functions and other notes for quick reference
"""

# Python: basic operators
a + b      # addition
a - b      # subtraction
a * b      # multiplication
a / b      # division
a ** b     # raise a to b
a // b     # floor division (keep integer part only)
a % b      # keep remainder only
a & b      # for booleans, True if a and b
a | b      # for booleans, True if a or b
a == b     # True if a equals b
a != b     # True if a is not equal to b
a <= b     # True if a is less than or equal to b
a is b     # True if a and b reference the same Python object
a is not b # True if a and b refernce different Python objects

# Get more information about a function with ?, or wrapping it in help()
?pow
help(pow)

# Get help with method
help(np.ndarray.flatten) # must inlcude object type

# Check data type
type(x)

# Convert between types
x = bool(1)
x = float(3.2)
x = str("Test string")
x = int(4.9)  # does not round up!




""" list object methods/functions and attributes """ # =============================================================================

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


""" string object method/functions and attributes """ # =============================================================================


###### Methods / Functions ###### =========================

# Capitalize first word only
x.capitalize()

# Make every letter upper case
x.upper()

# Make every letter lower case
x.lower()

# Replace strings
x.replace("z", "sa") # replace z with sa

# Check index of a particular character/string
x.index("a")

# Coerce numeric type to string to pring
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))





""" numpy objects/methods/functions and attributes  """ # =============================================================================

# A np.array can only contain one type of data, unlike a list which can 
# contain many different data types. This helps increase speen when perofrming
# element wise mathematical operations. np data types include:
# np.int64
# np.int32
# np.int16
# np.int8
# np.float64
# np.float32
# np.bool_
# np.datetime64


###### Creating and Slicing Array ###### =========================

# Create a np.array
x = np.array([1, 2, 3])
x = np.array([1, 2, 3], dtype = np.float32) # you can optionally specify dtype

# Slice 2D array, getting the first row only
array[0, :]

# Slice 2D array, getting only even indexes for indexs 50-100 and the 3rd col
array[50:101:2, 2]

# Slice array based on logical statement (fancy indexing)
bmi[ bmi > 23 ]
bmi[ bmi[:,2] > 23, : ] # Slicing 2D arrays requires to to specify row and col indicies correctly

# Save numpy array
with open("file_name.npy", "wb") as f: # wb stands for "write binary"
    np.save(f, obj_you_are_saving)

# Load numpy array
with open("file.npy", "rb") as f: # rb stands for "read binary"
    array = np.load(f)



###### Attributes ###### =========================

# See data type
array.dtype

# See dimensions of np.array
np_array.shape



###### Methods / Functions ###### =========================

# See data type
array.dtype

# Type conversion (Hierarchy: string > float > integer > boolean)
array.astype(np.int32)

# Create a sequence 1 to 12
np.arange(1,13)

# Sort data
np.sort(array)

# Flattens array to be 1-D only
array.flatten()

# Change dimensions of array
array.reshape()

# Return array of only unique elements
np.unique(array)

# Transpose array
np.transpose(array)

# Bind columns together
np.columnstack((col1, col2))

# Create 3X2 array of all zeros
np.zeros((3,2), dtype = np.int8) # Use smaller bit size for an array of zeros

# Create array of indicies from a 2D array based on logical statement
row_ind, col_ind = np.where(array <= 3)  # 'unpack' the results as a tuple

# Replace values with X if logical statement is True (R's ifelse function)
np.where(array == 0, "", array) # third argument is how to change element if it does not meet condition

# Concatenating rows - stack two arrays (Note: Use .reshape method if dims are not compatible)
np.concatenate((array1, array2))
np.concatenate((array1, array2), axis = 0)

# Concatenating columns - adding extra cols (Note: Use .reshape method if dims are not compatible)
np.concatenate((array1, array2), axis = 1)

# Delete values from object
np.delete(array, slice_index, axis=0)

# Compute descriptive info like the mean, median, sd
array.mean()
np.mean(array)
array.mean()
np.median(array)
array.mode()
array.std()
array.var()
array.sum()         # Sum entire array if no axis is specified
array.sum(axis = 0) # Sum across rows
array.sum(axis = 1) # Sum across cols
array.sum(axis = 1, keepdims=True) # Sum cols, keeping dimensionality the same
array.min()
array.max()
array.cumsum()
array.quantile()

# Compute custom fuction and call it as a method using .agg
def pct30(column):
    return column.quantile(0.3)
df["col"].agg(pct30)

# Pass multiple functions as methods
df["col"].agg([pct30, pct40])

# Compute correlation between two columns
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])

# simulate data from a normal distribution
array1 = np.random.normal(1.75, 0.20, 500)  #(mean, sd, n)

# Vectorize a base Python function to apply to a np.array object
upper_funct = np.vectorize(str.upper)
upper_case = upper_funct()



""" pandas objects/methods/functions and attributes  """ # =============================================================================

# =============================================================================
# pandas has two essential data types: 
#   (1) pd.Series which is like a 1-D numpy array
#   (2) pd.DataFrame which is essentially a 2-D numpy array for working with tabular data
# 
# =============================================================================

# Write csv. This only works if your writing a pd.DataFrame object!
df.to_csv("filename.csv")

# Look at first 5 rows of data
df.head()

# Look at index (row) names
df.index

# Change a column in your dataset to be the index
df1 = df.set_index("name")
df1 = df.set_index(["first_name", "last_name"])

# Reset the indexes that you created - so they become a column
df.reset_index()
df.reset_index(drop=True) # Just to drop the index and not make it a column

# Look at column names
df.columns

# Look at single column
df["col_name"]

# Look at multiple columns
df[["col_name", "col_names"]]
cols = ["col_name", "col_names"]
df[cols]

# More neatly view of col names
for col in df1.columns:
    print(col)

# Look at columns and their data types
df.info()

# Generate basic descriptive statistics
df.describe()

# Look at data values, which are stored as a 2-D
df.values

# Look at dimensions of DF
df.shape

# Sort data  
df.sort_values("col_name", ascending = False)

# Sort data by index value
df.sort_index(level = ["name1", "name2"], ascending=[True, False])

# Sort data by multiple valoues 
df.sort_values(["col_name", "col_name2"], ascending = [True, False])

# Add new column
df["new_col"] = x * y

# Slice DF based on logical conditions
df[df["col_name"] > 50]

# Slice DF based on index values (index must be sorted!)
df.sort_index().loc[["name1", "name2"]]
df.loc["2014-08-25":"2016-09-16"]  # Slice date range
df.loc["2014":"2016"]  # Slice by partial date range
df.loc[[("name1", "Group1"), ("name2", "Group2") ]]  # Subset based on intersection of two vars

# Slice DF based on range of index values
df.loc[("Labrador", "Brown"):("Schnauzer", "Grey")]

# Slice columns (keep all rows)
df.loc[:, "name":"height"]

# Slide DF using integers
df.iloc[1:3, 3:6]

# Slice DF based on logical conditions - AND logic
df[ (df["col_name"] == "value1") & (df["col_name2"] == "value2") ]

# Slice DF based on logical conditions - AND logic
colors = ["brown", "black", "tan"]
condition = dogs["color"].isin(colors)
dogs[condition]

# Drop duplicates
df.drop_duplicates(subset=["name", "breed"])

# Select only numeric columbns
df = df.select_dtypes(include=np.number)
df = df.select_dtypes(include=np.'int64')
df = df.select_dtypes(include=np.'datetime64[ns]')

# Check freq table, placing largest groups at top
df["breed"].value_counts(sort=True)

# Check proportion table, placing largest groups at top
df["breed"].value_counts(normalize=True)

# Grouped summaries
df.groupby("grouping_var")["var"].mean()
df.groupby("grouping_var")["var"].agg([min, np.mean, max, sum])
df.groupby("grouping_var")[["var1", "var2"]].agg([min, np.mean, max, sum])
df.groupby(["grouping_var1", "grouping_var2"])["var"].mean()

# Pivot table
df.pivot_table(values="var", index="groupping_var")
df.pivot_table(values="var", index="groupping_var", aggfunc=[np.mean, np.median])
df.pivot_table(values="var", index="groupping_var1", columns="groupping_var2")
df.pivot_table(values="var", index="groupping_var1", columns="groupping_var2", fill_value=0)
df.pivot_table(values="var", index="groupping_var1", columns="groupping_var2", fill_value=0, margins=True)


""" Interacting with other Python libraries """ # =============================================================================

# Install package - using pip (you might have to first install pip yo install other libraries)
pip3 install numpy

# Import radians function of math package
from math import radians



""" Useful shortcuts """ # =============================================================================

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

