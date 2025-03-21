import json
import pickle
import numpy as np

__city = None
__data_columns = None
__model = None
def load_saved_artifacts():
    print('loading saved artifacts..start')
    global __data_columns
    global __city

    with open('./artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __city = __data_columns[3:]
    global __model
    with open('./artifacts/American_home_prices_model.pickle','rb') as f:
        __model = pickle.load(f)
    print('loading saved artifacts..done')




def get_estimated_price(City, sqft, bath, beds):
    try:
        loc_index = __data_columns.index(City.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))

    x[0] = beds
    x[1] = bath
    x[2] = sqft
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def get_city_names():
    return __city

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_city_names())
    print(get_estimated_price("New York",2000,2,1))
