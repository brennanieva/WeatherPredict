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
    """ Compiles a training set from JAN2019 (CSV file) and creates dictionary (weather_records) with attributes labeled Station, Location, Date, Precipitation, Max Temperature (TMAX) and Minimum Temperature(TMIN)
    
    """
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
# print(training_data)


today = "2019-01-16"
yesterday = "2019-01-15" 
tomorrow = "2019-01-17"


#def calculations(Date)
#Assumes that weather is linear


#Calculates single date's temp difference

for i in range(len(training_data)):
    #Yesterday's data
    if training_data[i].get('Date')[8:]  == yesterday[8:]:
        YesterdayTempDifference = (training_data[i].get('TMAX')) - (training_data[i].get('TMIN'))

        print("Yesterday: ", yesterday)
        print("TMAX: ", training_data[i].get('TMAX'))
        print("TMIN: ", training_data[i].get('TMIN'))
        yesterday_tmax = int(training_data[i].get('TMAX'))
        yesterday_tmin = int(training_data[i].get('TMIN'))
        print ("Yesterday's Temp Difference: ", YesterdayTempDifference)


    #Today's data
    if training_data[i].get('Date')[8:] == today[8:]:
        TodayTempDifference = (training_data[i].get('TMAX')) - (training_data[i].get('TMIN'))

        print("Today: ", today)
        print("TMAX: ", training_data[i].get('TMAX'))
        print("TMIN: ", training_data[i].get('TMIN'))
        
        today_tmax = int(training_data[i].get('TMAX'))
        today_tmin = int(training_data[i].get('TMIN'))
        print ("Today's Temp Difference: ", TodayTempDifference)




        TomorrowMax = today_tmax + (today_tmax - yesterday_tmax )
        print("Tomorrows Max Temp?: ", TomorrowMax)



        





