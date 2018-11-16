from datetime import datetime # time
import json # json

# API call to prepare multiple points
def prepare_points(points, latitude, longitude, value, layer, timestamp = None):
    # check if we have a valid timestamp (use prepare_time to get a formatted value)
    if timestamp == None:
        timestamp = str(datetime.today()).split('.')[0] 
    # create the dict
    data = {
        'timestamp': timestamp,
        'location': {
            'lat': latitude,
            'long': longitude
        },
        'value': value,
        'layer': layer
    }
    # append the dict to all the values
    points.append(data)
    # return all the values + this new one
    return points

def prepare_time(year, month, day, hour=None, minute=None, second=None):
    # get all args in an array for pre-processing
    times = [year,month,day,hour,minute,second]
    # pre-processing phase
    new_times = []
    # see what arg is none
    for elem in times:
        if elem != None:
            # only use args that have a value
            new_times.append(elem)
    # create a datetime corresponding to the args
    time = datetime(*new_times)
    # return the time
    return str(time)