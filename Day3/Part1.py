# Get the input data

with open("2021/Day3/input-day-3.txt") as f:
    input_lines = f.readlines()

# Clean the data

diagnostic_report = []
for line in input_lines:
    clean_line = line.replace("\n", "")
    diagnostic_report.append(clean_line)