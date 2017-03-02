


# For calibration file read entire file parsing each line using delimitor
# Store data in list
# Search list for parameter in list[0].  Read or replace List[1]







# Text file operations


# file = open( "testfile.txt", "w")
# file.write("Hello World!")
file = open( "testfile.txt", "r")
print file.readline()
print file.readline()
print file.readline()
print file.readline()
print file.readline()


# CSV file operations

# https://docs.python.org/2/library/csv.html
import csv

# csv.reader(csvfile, dialect='excel', **fmtparams)


import csv
with open('some.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

# or 

import csv
with open('passwd', 'rb') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print row


# or
# A slightly more advanced use of the reader — catching and reporting errors:

import csv, sys
filename = 'some.csv'
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print row
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


# csv.writer(csvfile, dialect='excel', **fmtparams)

import csv
with open('some.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)






# Binary file operations




