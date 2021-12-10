# Get the input data

with open("2021/Day3/input-day-3.txt") as f:
    input_lines = f.readlines()

# Clean the data

diagnostic_report = []
for line in input_lines:
    clean_line = line.replace("\n", "")
    diagnostic_report.append(clean_line)

# Get the oxygen rating

def filterArrayOxygenGenerator(num, arr):
    new_arr = []
    digit = 0
    for i in range(0, len(arr)):
        digit+=int(arr[i][num])
    if digit >= (len(arr)/2):
        digit = 1
    else:
        digit = 0
    for i in range(0, len(arr)):
        if int(arr[i][num]) == digit:
            new_arr.append(arr[i])
    return new_arr
        

def getOxygenGenerator():
    index = 0
    array = diagnostic_report
    while len(array) >1:
        array = filterArrayOxygenGenerator(index, array)
        index+=1
    return int(array[0], 2)


# Get CO2 Scrubber

def filterArrayCO2Scrubber(num, arr):
    new_arr = []
    digit = 0
    for i in range(0, len(arr)):
        digit+=int(arr[i][num])
    if digit < (len(arr)/2):
        digit = 1
    else:
        digit = 0
    for i in range(0, len(arr)):
        if int(arr[i][num]) == digit:
            new_arr.append(arr[i])
    return new_arr
        

def getCO2Scrubber():
    index = 0
    array = diagnostic_report
    while len(array) >1:
        array = filterArrayCO2Scrubber(index, array)
        index+=1
    return int(array[0],2)



# Get result
            
print(getOxygenGenerator()*getCO2Scrubber())

