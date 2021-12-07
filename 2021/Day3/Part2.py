# Get the input data

with open("2021/Day3/input-day-3.txt") as f:
    input_lines = f.readlines()

# Clean the data

diagnostic_report = []
for line in input_lines:
    clean_line = line.replace("\n", "")
    diagnostic_report.append(clean_line)

# Generate gamma & epsilon rates based on the frequency of 1s and 0s in the data

gamma_rate = ''
epsilon_rate = ''
for i in range(0, len(diagnostic_report[0])):
    digit=0
    for binary_num in diagnostic_report:
        digit+=int(binary_num[i])
    if digit > (len(diagnostic_report)/2):
        gamma_rate+="1"
        epsilon_rate+="0"
    else:
        gamma_rate+="0"
        epsilon_rate+="1"


# Convert rates from binary strings to numbers and multiply to obtain the result

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
print(gamma_rate*epsilon_rate)