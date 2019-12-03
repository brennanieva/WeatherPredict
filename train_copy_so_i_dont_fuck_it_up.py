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
    ''' Computes the average of the list'''
    average = sum(list) / len(list)
    return average

def compare_predictions(predictions,today):
    '''Compares the difference between the prediction and "todays" actual temperature'''
    for i in predictions:
        
        comparision =  i - int(today)
        return comparision

def predict_equal(yesterday):
    '''Takes yesterday's temperature and calculates that tomorrows temperature will be the same as yesterday'''
    

    

    TomorrowTempPredict = int(training_data[i-1].get('TMAX'))

    return TomorrowTempPredict

        
def predict_linear(yesterday):
    '''Calculates tomorrow's temperature as a linear relationship by using yesterday's temperature and the day before yesterday'''

    yesterday = int(training_data[i-1].get('TMAX'))
   
    today_tmax = int(training_data[i].get('TMAX'))

    
    two_days_tmax = int(training_data[i-2].get('TMAX'))


    TomorrowTempPredict = today_tmax + (yesterday - two_days_tmax)
    return TomorrowTempPredict


    
    


#Calculates single date's temp difference

if __name__ == "__main__":

    data_viewed = input("To view all weather data from Jan2019, type 'view_all' \n otherwise, please specifiy a date to forecast the following day's temperature (YYYY-MM-DD):  ")

    if data_viewed == "view_all":
        lin_predictions = []
        eq_predictions = []
        lin_errors = []
        eq_errors = []
        

        for i in range(len(training_data)):
            today = training_data[i]
            yesterday = training_data[i-1]

            today_tmax = int(training_data[i].get('TMAX'))
            today_tmin = int(training_data[i].get('TMIN'))


            lin_predictions.append(predict_linear(today))
            eq_predictions.append(predict_equal(today))

            lin_errors.append(compare_predictions(lin_predictions, today_tmax))
            eq_errors.append(compare_predictions(eq_predictions, today_tmax))



        lin_avg_error = compute_mean(lin_errors)
        eq_avg_error = compute_mean(eq_errors)

        print("linear predictions: ")
        print(lin_predictions)
        print("equal predictions: ")
        print(eq_predictions)

        print("linear errors: ")
        print(lin_errors)

        print("equal errors: ")
        print(eq_errors)

        print("Average error [linear]: ")
        print(lin_avg_error)

        print("Average error [equal]: ")
        print(eq_avg_error)

    else:

        print("linear prediction: ", predict_linear((data_viewed)))
        print("equal prediction: ", predict_equal((data_viewed)))







    

    






#To DO

#Take average error for equal
#Fix Equal Temperature
#finish CSV parse
#csv docs




#prediction mech to all take the same arguments so that we can easily swap them in and out
#given all days at the index of the one you want to predict,  here are the different prediction methods and their output




