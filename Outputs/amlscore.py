import json
import numpy as np
import os
import pickle
import joblib
import pandas as pd
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path("automl")
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)['data']
        data = pd.DataFrame.from_dict(data)
        # make prediction
        result = model.predict(data)
        return result.tolist()
    except Exception as ex:
        error = str(ex)
        return error
