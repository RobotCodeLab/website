#!/usr/bin/env python3

import os
import sys


# given the name of a file, call remove_first_column on the file
def remove_first_column(file_name):
    # open the file
    with open(file_name, 'r') as f:
        # read the file
        lines = f.readlines()
        # open the file again for writing
        with open(file_name, 'w') as f:
            # write the file without the first column
            for line in lines:
                f.write(line.split('\t')[1] + '\n')



# a function that takes a csv as input and return a csv with the same columns but with the first column removed the last item
function remove_first_column(csv_file) {
    # read the csv file
    csv_file_content = read_csv(csv_file)
    # get the first column
    first_column = csv_file_content[0]





# a list of students and grades for a class
students = [
    ['John', 'A', 'B', 'C'],
    ['Mary', 'B', 'C', 'A'],
    ['Peter', 'A', 'B', 'C'],
    ['Sally', 'A', 'B', 'C'],
    ['George', 'A', 'B', 'C'],
    ['Mike', 'A', 'B', 'C'],
    ['Sarah', 'A', 'B', 'C'],
    ['Samantha', 'A', 'B', 'C'],
    ['William', 'A', 'B', 'C'],
    ['Jennifer', 'A', 'B', 'C'],
    ['James', 'A', 'B', 'C'],
    ['Robert', 'A', 'B', 'C'],
    ['Michael', 'A', 'B', 'C'],
    ['William', 'A', 'B', 'C'],
    ['Elizabeth', 'A', 'B', 'C'],
    ['Richard', 'A', 'B', 'C'],
    ['Joseph', 'A', 'B', 'C'],
}











