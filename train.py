from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core import Dataset

ds= TabularDatasetFactory.from_delimited_files(path="https://raw.githubusercontent.com/Aishwaryasasanapuri/Heart-Failure-prediction-project/main/heart_failure_clinical_records_dataset.csv")
def clean_data(data):
   
    x_df = data.to_pandas_dataframe().dropna()
    y_df = x_df.pop("DEATH_EVENT")
    return x_df, y_df

x, y = clean_data(ds)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

run = Run.get_context()

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

   

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))
    os.makedirs('outputs', exist_ok=True)
    # note file saved in the outputs folder is automatically uploaded into experiment record
    joblib.dump(value=model, filename='outputs/hypermodel.pkl')

if __name__ == '__main__':
    main()
