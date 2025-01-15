import pickle

__model_light_status=None
__model_fan_range=None

def load_model_light_status():
    global __model_light_status
    with open("model_light_status.pkl", "rb") as model_file:
        __model_light_status = pickle.load(model_file)
        
    return __model_light_status

def load_model_fan_range():
    global __model_fan_range
    with open("model_pkl.pkl", "rb") as model_file:
        __model_fan_range = pickle.load(model_file)
    return __model_fan_range

def predict_data(data):
    global __model_fan_range, __model_light_status
    if __model_fan_range is None:
        __model_fan_range = load_model_light_status()
    return __model.predict(data)