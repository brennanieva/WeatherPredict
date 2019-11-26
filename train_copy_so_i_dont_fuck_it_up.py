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
ATTRS.append("TOBS")
#Time of Observation Bias
#  different times of day exert different temperatures,  TOBS used to caluc


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



#Executes function and prints the results
training_data = (make_training_set('TrainingSets/Jan2019.csv'))
# print(training_data)


def compute_mean(list):
    average = sum(list) / len(list)
    return average

def compare_predictions(predictions,today):

    for i in predictions:
        comparision =  i - int(today)
        return comparision

def predict_equal(yesterday):
    for i in range(len(training_data)):


        today_tmax = int(training_data[i].get('TMAX'))
        today_tmin = int(training_data[i].get('TMIN'))

        TomorrowTempPredict = int(training_data[i].get('TMAX'))

        return TomorrowTempPredict

        
def predict_linear(yesterday):
    for i in range(len(training_data)):
 

        
        yesterday_tmax = int(training_data[i-1].get('TMAX'))

        today_tmax = int(training_data[i].get('TMAX'))

        TomorrowTempPredict = today_tmax + (today_tmax - yesterday_tmax)
        return TomorrowTempPredict


    


#Calculates single date's temp difference

lin_predictions = []
eq_predictions = []

lin_errors = []
eq_errors = []

for i in range(len(training_data)):

    today = training_data[i]

    yesterday = training_data[i-1]

    today_tmax = int(training_data[i].get('TMAX'))
    today_tmin = int(training_data[i].get('TMIN'))


    lin_predictions.append(predict_linear(yesterday))

    eq_predictions.append(predict_equal(yesterday))




    lin_errors.append(compare_predictions(lin_predictions, today_tmax))

    eq_errors.append(compare_predictions(eq_predictions, today_tmax))



avg_error = compute_mean(lin_errors)

print("linear predictions: ")
print(lin_predictions)
print("equal predictions: ")
print(eq_predictions)

print("linear errors: ")
print(lin_errors)

print("equal errors: ")
print(eq_errors)

print("Average error: ")
print(avg_error)


