#Author: BrennaNieva
#Date: 10/15/2019
#Description: CSCI 141 [40828] ML Project for Weather Prediction



###############################################################################

ATTRS = []
ATTRS.append("Station")
ATTRS.append("Location")
ATTRS.append("Date")
ATTRS.append("Precipitation")
ATTRS.append("TMAX")
ATTRS.append("TMIN")

###############################################################################

def make_training_set(weather2019):
   
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




#Sample calculations
training_data = "weather2019.csv"
train_set = make_training_set('weather2019.csv')

#DateTime
#Take yesterday's temperature - todays
# for key, value in train_set.make_training_set():
#     if key is 'Date': #'name' is the key we wish to get the value from
#         print(value) # print its value

# today = train_set["Date"] == "2019-08-31" and train_set["Station"] == "USC00450587"
# print (today)
