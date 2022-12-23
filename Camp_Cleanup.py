import os.path
import sys
import numpy as np

current_directory = os.path.dirname(os.path.realpath(__file__))

# Setup variables for future computation.
filepath = current_directory + '\\Resources\\Camp_Cleanup_Input.txt'
expanded_assignment = []
assignment_list = []
pair = []
counter = 0
boolean_sum = 0

# Check that file exists, if not exit with error message.
if not os.path.isfile(filepath):
    sys.exit("Error - File not found.")

# Open file and read it in line by line.
file = open(filepath, "r")
lines = file.readlines()

# Read through each line and expand out the assignments into "full assignment" strings.
for line in lines:
    assignments = line.strip().split(',')
    for assignment in assignments:
        assignment = assignment.split('-')
        for i in range(int(assignment[0]), int(assignment[1]) + 1):
            expanded_assignment.append(str(i))
        counter += 1
        pair.append(expanded_assignment)
        expanded_assignment = []
        # If the counter hits 2 then we have 2 expanded assignments grouped as a pair.  Add this pair to the list and move on.
        if counter == 2:
            assignment_list.append(pair)
            pair = []
            counter = 0

# PART 1
# Go through each pair in the list and compare them to see if the first assignment contains the second or vice versa.
# Note that counter will always be zero when we get to this point as the assignments are divided into groups of two.
for pair in assignment_list:
    if pair[0] != pair[1]:
        # Check if list one is in list two.
        for boolean in np.isin(pair[0], pair[1], invert=True):
            boolean_sum += boolean
        # All the values in list one are in list two, increment counter.
        if boolean_sum == 0:
            counter += 1
        boolean_sum = 0
        # Check if list two is in list one.
        for boolean in np.isin(pair[1], pair[0], invert=True):
            boolean_sum += boolean
        # All the values in list two are in list one, increment counter.
        if boolean_sum == 0:
            counter += 1
        boolean_sum = 0
    # They are the same, increment counter.
    else:
        counter += 1

print(f'Number of assignments contained in other assignments: {counter}')

# PART 2
counter = 0
boolean_sum = 0

for pair in assignment_list:
    if pair[0] != pair[1]:
        # There is some overlap. increment counter.
        if np.isin(pair[0], pair[1]).__contains__(True):
            counter += 1
    # They are the same, increment counter.
    else:
        counter += 1

print(f'Number of assignments with any overlap: {counter}')

file.close()
