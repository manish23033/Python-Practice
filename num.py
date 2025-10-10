import pandas as pd
import numpy as np       
# check the data info value are non-null
print(data.info())    

# Display the unique value like a 'KM'
print("")
null_values = np.unique(data["KM"])
print(null_values)

# replace the value
print("*Before*")
print(np.unique(data["Doors"]))
print("*Before Replace*")

data["Doors"].replace("three", "3", inplace=True)
data["Doors"].replace("four", "4", inplace=True)
data["Doors"].replace("five", "5", inplace=True)

print("*After replace*")
print(np.unique(data["Doors"]))

print(data.info())

# Create a data copy
data_copy = data.copy()

data_copy.insert(10, "Price_Class", "0")
print(data_copy)

for i in range(len(data_copy["Price"])):
      if data_copy["Price"][i] <= 8450:
            data_copy["Price_class"][i] = "Low"
      elif data_copy["Price"][i] > 11950:
            data_copy["Price_class"][i] = "High"
      else:
            data_copy["Price_class"][i] = "Medium"

      print(data_copy)