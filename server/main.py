from fastapi import FastAPI, Request
import pickle
import numpy as np
import uvicorn
from mail import sendMail

app = FastAPI()

with open("model_light_status.pkl", "rb") as model_file:
    model_light_status = pickle.load(model_file)
    
with open("model_fan_range.pkl", "rb") as model_file:
    model_fan_range = pickle.load(model_file)


@app.get("/")
async def predict_bulb_state():
    return {"status": "Running"} 
    
@app.post("/predict_bulb_state_using_luminosity")
async def predict_bulb_state(request: Request):
    data = await request.json()
    print(data)
    

    if 'luminosity' not in data:
        return {"error": "Luminosity value is required."}
    
    luminosity_value = np.array([[data['luminosity']]])
    prediction = model_light_status.predict(luminosity_value) 
    
    # Return the prediction as a JSON response (assuming 0 = off, 1 = on)
    return {"bulb_state": int(prediction[0])} 


@app.post("/predict_fan_range_using_temperature")
async def predict_fan_range_using_temperature(request: Request):
    data = await request.json()
    print(data)
    

    if 'temperature' not in data:
        return {"error": "Temperature value is required."}

    if data['temperature'] > 30:
        sendMail()
    
    temperature_value = np.array([[data['temperature']]])
    prediction = model_fan_range.predict(temperature_value) 
    
    return {"fan_range": int(prediction[0])} 


if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=4000, reload=True)

