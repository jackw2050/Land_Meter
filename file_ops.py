# Files - cal file,  log file,  data files (TBD)
# Cal file: 1)  Create new file
#           2)  Read data from file
#           3)  Store data in list
#           4)  Retrieve requested data
#           5)  Later - Replace specific data in file
# Log file: 1)  Create new file
#           2)  Append to file

# Data file 1)  Check for existing file - return bool
#           2)  Create new file
#           3)  Append data to new file
#               Two versions.  One that takes one line of data.  One that takes list and iterates through
#               Note:  May need multiple version for each test or just for different number of columns.  Pass files name on call



# For calibration file read entire file parsing each line using delimitor
# Store data in list
# Search list for parameter in list[0].  Read or replace List[1]

import csv, sys
from datetime import datetime




filename = 'names.csv'
#class file_op(object):
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


#   Calibration file section
def create_basic_cal_file():
    with open('zls_cal.csv', 'w') as csvfile:
        fieldnames = ['field', 'value', 'comment']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'field': 'Meter',                              'value': 'Land',        'comment': ''})
        writer.writerow({'field': 'Hardware_revision',                  'value': '1.0',         'comment': 'Initial release'})
        writer.writerow({'field': 'Software_revision',                  'value': '1.5',         'comment': ''})
        writer.writerow({'field': 'Calibration_version',                'value': 'calibrated',  'comment': ''})
        writer.writerow({'field': 'Customer',                           'value': 'Orangelamp',  'comment': ''})
    
        writer.writerow({'field': 'pwm_freq',                           'value': '125',         'comment': 'Hz'})
        writer.writerow({'field': 'sense_freq',                         'value': '10000',       'comment': 'Hz'})
        writer.writerow({'field': 'adc_offset',                         'value': '0.0044678',   'comment': 'V'})
        writer.writerow({'field': 'zh_offset',                          'value': '0.0',         'comment': 'V'})
        writer.writerow({'field': 'lid_thermistor_offset',              'value': '0.0',         'comment': 'V'})
        writer.writerow({'field': 'p12v_offset',                        'value': '0.0',         'comment': 'V'})
        writer.writerow({'field': 'p5v_offset',                         'value': '0.0',         'comment': 'V'})
        writer.writerow({'field': 'p3p3v_offset',                       'value': '0.0',         'comment': 'V'})
        writer.writerow({'field': 'battery_thermistor_offset',          'value': '0.0',         'comment': 'V'})
        writer.writerow({'field': 'batt_v_offset',                      'value': '0.0',         'comment': 'V'})

        writer.writerow({'field': 'beam_offset',                        'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'm5v_offset',                         'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'zp_offset',                          'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'gearbox_thermistor_offset',          'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'conning_tower_thermistor_offset',    'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'arrestment_thermistor_offset',       'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'meter_thermistor_1_offset',          'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'meter_thermistor_2_offset',          'value': '0.0',         'comment': ''})
            
        writer.writerow({'field': 'adc_divider',                        'value': '0.0044678',   'comment': ''})
        writer.writerow({'field': 'zh_divider',                         'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'lid_thermistor_divider',             'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'p12v_divider',                       'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'p5v_divider',                        'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'p3p3v_divider',                      'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'battery_thermistor_divider',         'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'batt_v_divider',                     'value': '0.0',         'comment': ''})

        writer.writerow({'field': 'beam_divider',                       'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'm5v_divider',                        'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'zp_divider',                         'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'gearbox_thermistor_divider',         'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'conning_tower_thermistor_divider',   'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'arrestment_thermistor_divider',      'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'meter_thermistor_1_divider',         'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'meter_thermistor_2_divider',         'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'beam10',                             'value': '0.0',         'comment': ''})
        writer.writerow({'field': 'beam50',                             'value': '2.5',         'comment': ''})
        writer.writerow({'field': 'beam90',                             'value': '5.0',         'comment': ''})

        writer.writerow({'field': 'p5vTarget',                          'value': '5.0',         'comment': 'V'})
        writer.writerow({'field': 'p5vError',                           'value': '0.2',         'comment': 'V'})

        writer.writerow({'field': 'p3p3vTarget',                        'value': '3.3',         'comment': 'V'})
        writer.writerow({'field': 'p3p3vError',                         'value': '0.2',         'comment': 'V'})

        writer.writerow({'field': 'p12vTarget',                         'value': '12.0',        'comment': 'V'})
        writer.writerow({'field': 'p12vError',                          'value': '0.2',         'comment': 'V'})

        writer.writerow({'field': 'batteryTarget',                      'value': '12.0',        'comment': 'V'})
        writer.writerow({'field': 'batteryError',                       'value': '2.0',         'comment': 'V'})

        writer.writerow({'field': 'zh_dividerTarget',                   'value': '12.0',        'comment': 'V'})
        writer.writerow({'field': 'zh_dividerError',                    'value': '2.0',         'comment': 'V'})
        
        writer.writerow({'field': 'zpTarget',                           'value': '12.0',        'comment': 'V'})
        writer.writerow({'field': 'zpError',                            'value': '2.0',         'comment': 'V'})        



# CSV file open flags  a - append, w - write, rb




def readFile(fileName):
   with open(fileName, 'rb') as csvfile:
    cal_file_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    your_list = list(cal_file_reader)
   return your_list


def read_cal_file():
    with open('zls_cal.csv', 'rb') as csvfile:
        cal_file_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        your_list = list(cal_file_reader)
        
        return your_list
        
        #for row in cal_file_reader:
            #col_width = max(len(word) for row in cal_file_reader for word in row) + 2  # padding
            #print '\t '.join(row)

            #print row[0], '\t', row[1], row[2]
            #print "".join(word.ljust(col_width) for word in row)
            #'{0:30}  {10}  {10}'.format(row[0], row[1], row[2])


def update_cal_file(field, value, comment):
    with open('zls_cal.csv', 'w') as csvfile:
        fieldnames = ['field', 'value', 'comment']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)



# Log file section
def create_basic_log_file():
    print "Creating initial log file"
    with open('log.csv', 'w') as csvfile:
        fieldnames = ['Date', 'Comment']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        log_time = str(datetime.now())
        #writer.writeheader()
        writer.writerow({'Date': log_time, 'Comment': 'Initial entry'})

    print "Log file successfully created"
    
def create_log_entry(issue):   
     with open('log.csv', 'a') as csvfile:
        fieldnames = ['Date', 'Comment']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        log_time = str(datetime.now())
        #writer.writeheader()
        writer.writerow({'Date': log_time, 'Comment': issue})

