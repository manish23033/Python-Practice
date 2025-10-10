print(data)

Print data type of data
print(data.dtypes)  
          
check the data info value are non-null
print(data.info())    

Display the unique value like a 'KM'
print("")
null_values = np.unique(data["KM"])
print(null_values)

replace the value
print("*Before*")
print(np.unique(data["Doors"]))
print("*Before Replace*")

data["Doors"].replace("three", "3", inplace=True)
data["Doors"].replace("four", "4", inplace=True)
data["Doors"].replace("five", "5", inplace=True)

print("*After replace*")
print(np.unique(data["Doors"]))
