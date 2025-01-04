from fastapi import FastAPI, Request
import pickle
import numpy as np
import uvicorn

app = FastAPI()

with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)


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
    prediction = model.predict(luminosity_value) 
    
    # Return the prediction as a JSON response (assuming 0 = off, 1 = on)
    return {"bulb_state": int(prediction[0])} 


if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=4000, reload=True)

