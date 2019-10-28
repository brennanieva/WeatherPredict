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



def make_training_set(Jan2019):
""" Weather_records creates a dictionary with attributes labeled Station, Location, Date, Precipitation, Max Temperature (TMAX) and Minimum Temperature(TMIN)"""
    weather_records = []
    # Read in file
    with open(Jan2019) as file:
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

            # Read Station ID as an string:
            record[ATTRS[0]] = str(line_list[0].strip("\""))

            #Read Location as a string:
            record[ATTRS[1]] = str(line_list[1].strip("\""))

            #Read Date as a string:
            record[ATTRS[2]] = str(line_list[3].strip("\""))

            #Read Precipitation as a float:
            record[ATTRS[3]] = str(line_list[4].strip("\""))

            #Checks if TMAX and TMIN are empty, if so, sets their value to 0
            #Avoids list overflow error
            if line_list[5].strip("\"") == '':
                record[ATTRS[4]] = 0
                record[ATTRS[5]] = 0
            else:
                #Read TMAX as a int:
                record[ATTRS[4]] = int(line_list[5].strip("\""))

                #Read TMIN as a int:
                record[ATTRS[5]] = int(line_list[6].strip("\""))

            # Add the dictionary to a list
            weather_records.append(record)


    return weather_records

#Ignore
#euclidean_distance = math.sqrt((feature[0]-p[0])**2 +(feature[1]-p[1])**2
#Ignore

#Executes function and prints the results
training_data = (make_training_set('TrainingSets/Jan2019.csv'))
print(training_data)



    # today = "2019-01-04"
    # for i in range(len(training_data)):
    #     if training_data[i].get('Date')[8:] == today[8:]:
    #         print("Does This Work???? bc idk man")
    #         print(training_data[i].get("TMAX"))

currentDate = "2019-01-02"
ed = 0.0 #Ignore

for i in range(len(training_data)):
    if training_data[i].get('Date')[8:] == currentDate[8:]:
       
        TodayTempDifference = (training_data[i].get('TMAX')) - (training_data[i].get('TMIN'))
        print("TMAX", training_data[i].get('TMAX'))
        print("TMIN", training_data[i].get('TMIN'))
        print (TodayTempDifference)
#Sample calculations
# training_data = "TrainingSets/Jan2019.csv"
# train_set = make_training_set(Jan2019)

