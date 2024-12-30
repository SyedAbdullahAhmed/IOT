import pickle

__model=None

def load_model():
    global __model
    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    return model

def predict_data(data):
    global __model
    if __model is None:
        __model = load_model()
    return __model.predict(data)