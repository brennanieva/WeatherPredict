#Author: BrennaNieva
#Date: 10/15/2019
#Description: CSCI 141 [40828] ML Project for Weather Prediction



###############################################################################
# GLOBAL CONSTANT
# For use as dictionary keys
# You can use this list throughout the program without passing it to a function
# DO NOT MODIFY
ATTRS = []
ATTRS.append("Station")
ATTRS.append("Location")
ATTRS.append("Date")
ATTRS.append("Precipitation")
ATTRS.append("TMAX")
ATTRS.append("TMIN")

###############################################################################

def make_training_set(weather2019):
    """ Read training data from the file whose path is weathersmall.
        Return a list of records, where each record is a dictionary
        containing a value for each of the 6 keys in ATTRS.
    """
    # COMPLETE - DO NOT MODIFY
    weather_records = []
    # Read in file
    with open(weather2019) as file:
        #Skip header line in file
        next(file)
        for line in file:
            if '#' in line:
                continue
            line = line.strip('\n')
            line_list = line.split(',')

            # Create a dictionary for the line and map the attributes in
            # ATTRS to the corresponding values in the line of the file
            record = {}

            # Read Station ID as an int:
            record[ATTRS[0]] = str(line_list[0].strip("\""))

            #Read Location as a string:
            record[ATTRS[1]] = str(line_list[1].strip("\""))

            #Read Date as a string:
            record[ATTRS[2]] = str(line_list[6].strip("\""))

            #Read Precipitation as a float:
            record[ATTRS[3]] = str(line_list[9].strip("\""))

            #Checks if TMAX and TMIN are empty, if so, sets their value to 0
            #Avoids list overflow error
            if line_list[12].strip("\"") == '':
                record[ATTRS[4]] = 0;
                record[ATTRS[5]] = 0;
            else:
                #Read TMAX as a string:
                record[ATTRS[4]] = int(line_list[12].strip("\""))

                #Read TMIN as a string:
                record[ATTRS[5]] = int(line_list[13].strip("\""))

            # Add the dictionary to a list
            weather_records.append(record)


    return weather_records

#Executes function and prints the results
print(make_training_set('weather2019.csv'))
