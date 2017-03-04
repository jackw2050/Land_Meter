


# For calibration file read entire file parsing each line using delimitor
# Store data in list
# Search list for parameter in list[0].  Read or replace List[1]

import csv, sys
filename = 'names.csv'


class file_op(object):
    def read_cal_data(self, name):
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    if row[0] == name:
                        print(row)
                        return name

            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

    def write_new_file(self, row_data):
        with open('names.csv', 'w') as csvfile:
            fieldnames = ['field', 'value', 'comment']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.write





# Text file operations


# file = open( "testfile.txt", "w")
# file.write("Hello World!")
# file = open( "testfile.txt", "r")
# print file.readline()
# print file.readline()
# print file.readline()
# print file.readline()
# print file.readline()


# # CSV file operations

# # https://docs.python.org/2/library/csv.html



# import csv, sys

# with open('names.csv', 'w') as csvfile:
#     fieldnames = ['field', 'value', 'comment']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'field': 'Meter', 'value': 'Land'})
#     writer.writerow({'field': 'Revision', 'value': '5.6'})
#     writer.writerow({'field': 'Calibration_version', 'value': 'calibrated'})
#     writer.writerow({'field': 'Customer', 'value': 'Orangelamp'})

#     writer.writerow({'field': 'pwm_freq', 'value': '125', 'comment': 'Hz'})
#     writer.writerow({'field': 'sense_freq', 'value': '10000', 'comment': 'Hz'})
#     writer.writerow({'field': 'adc_ain_0_offset', 'value': '0.0044678'})
#     writer.writerow({'field': 'sense_pot_setting', 'value': '645'})

# # with open('names.csv', newline='') as f:
# #     reader = csv.reader(f)
# #     for row in reader:
# #         print(row)
# #


# filename = 'names.csv'
# with open(filename, newline='') as f:
#     reader = csv.reader(f)
#     try:
#         for row in reader:
#             if row[0] == 'sense_freq':
#                 print(row)
#                 print(float(row[1]))

#             elif row[0] == 'pwm_freq':
#                 pwm_freq = float(row[1])
#                 print(pwm_freq)
#     except csv.Error as e:
#         sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

