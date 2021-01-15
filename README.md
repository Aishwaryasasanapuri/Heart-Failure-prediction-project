*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# Heart Failure Prediction

This project is part of Udacity Capstone Project.  It is performed using two models:

1. Automated ML and
2. Hyperparameters are tuned using HyperDrive.

## Project Set Up and Installation

The project is carried out using below steps

- Import the External dataset
- Train Auto ML model
- Train Hyperdrive model
- Compare model performance
- Deploy best model
- Test model endpoint

## Dataset

### Overview

Dataset is downloaded from Kaggle repository and used through Github.

Kaggle link : https://www.kaggle.com/andrewmvd/heart-failure-clinical-data

**Citation**: Davide Chicco, Giuseppe Jurman: Machine learning can predict survival of patients with heart failure from serum creatinine and ejection fraction alone. BMC Medical Informatics and Decision Making 20, 16 (2020)

12 clinical features:

- age: age of the patient (years)
- anaemia: decrease of red blood cells or hemoglobin (boolean)
- high blood pressure: if the patient has hypertension (boolean)
- creatinine phosphokinase (CPK): level of the CPK enzyme in the blood (mcg/L)
- diabetes: if the patient has diabetes (boolean)
- ejection fraction: percentage of blood leaving the heart at each contraction (percentage)
- platelets: platelets in the blood (kiloplatelets/mL)
- sex: woman or man (binary)
- serum creatinine: level of serum creatinine in the blood (mg/dL)
- serum sodium: level of serum sodium in the blood (mEq/L)
- smoking: if the patient smokes or not (boolean)
- time: follow-up period (days)

### Task

In this project, we will predict the death prediction or Heart failure rate with the help of 12 attributes provided in the dataset. The target ("DEATH_EVENT") column with values of 1 means person will suffer from heart failure and 0 means no heart failure.


### Access
 Explain how you are accessing the data in your workspace.

We download the heart failure dataset from kaggle as a csv file and upload the same to github and access the using rawcontent process from github.

Below is the screenshot after the dataset is registered

![](https://github.com/Aishwaryasasanapuri/Heart-Failure-prediction-project/blob/main/Screenshots/Dataset.JPG)

Before we proceed with the project , firstly we will create a compute instance to run our jupyter files. 

![](https://github.com/Aishwaryasasanapuri/Udacity---AzureML-Capstone-project/blob/main/Screenshots/Capture.JPG)

## Automated ML
 Give an overview of the `automl` settings and configuration you used for this experiment

Automl is also known as Automated ML which helps in rapidly performing multiple iteration on different algorithms. It also supports Ensemble methods. Here we get voting ensemble as our best run.

Automl Configuaration

![](https://github.com/Aishwaryasasanapuri/Heart-Failure-prediction-project/blob/main/Screenshots/Automl_config.JPG)

### Results
 What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

We got Voting Ensembler as best model with an accuracy of 

Screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

Here is the Automl run details

![](https://github.com/Aishwaryasasanapuri/Udacity---AzureML-Capstone-project/blob/main/Screenshots/Automl_runs.JPG)

Best Auto Ml model

![](https://github.com/Aishwaryasasanapuri/Udacity---AzureML-Capstone-project/blob/main/Screenshots/Aml_bestmodel.JPG)

![](https://github.com/Aishwaryasasanapuri/Heart-Failure-prediction-project/blob/main/Screenshots/voting%20ensembler.JPG)

Best run id

![](https://github.com/Aishwaryasasanapuri/Heart-Failure-prediction-project/blob/main/Screenshots/Aml_bestrunid.JPG)


## Hyperparameter Tuning
 What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search

We choose a hyperdrive model with Randomparameter sampling , Early termination policy we used is Banditpolicy with a sloack facotr of 0.1 and we have used Accuracy as our primary metric.

![](https://github.com/Aishwaryasasanapuri/Heart-Failure-prediction-project/blob/main/Screenshots/hd_config.JPG)

### Results
What are the results you got with your model? What were the parameters of the model? How could you have improved it?

Screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

![](https://github.com/Aishwaryasasanapuri/Udacity---AzureML-Capstone-project/blob/main/Screenshots/hyperparameter_run.JPG)

![](https://github.com/Aishwaryasasanapuri/Heart-Failure-prediction-project/blob/main/Screenshots/hyperdrive_run_page.JPG)

Best hyperdrive model

![](https://github.com/Aishwaryasasanapuri/Heart-Failure-prediction-project/blob/main/Screenshots/hd_bestmodel.JPG)

Logs files of the services

![](https://github.com/Aishwaryasasanapuri/Heart-Failure-prediction-project/blob/main/Screenshots/enablelogs.JPG)

## Model Deployment
 Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.
 
![](https://github.com/Aishwaryasasanapuri/Udacity---AzureML-Capstone-project/blob/main/Screenshots/Screenshots/hd_endpoint.JPG)
 
![](https://github.com/Aishwaryasasanapuri/Udacity---AzureML-Capstone-project/blob/main/Screenshots/hd_endpoint2.JPG)

Application insights of Hyperdrive service

![](https://github.com/Aishwaryasasanapuri/Heart-Failure-prediction-project/blob/main/Screenshots/hd_appinsights.JPG)

Application insights of Automl service 
![](https://github.com/Aishwaryasasanapuri/Heart-Failure-prediction-project/blob/main/Screenshots/automl_appinsights.JPG)

## Deleting Compute

Since we completed all the related works , we will be deleting the Endpoint services and Compute clusters and instances

![](https://github.com/Aishwaryasasanapuri/Udacity---AzureML-Capstone-project/blob/main/Screenshots/deleting_compute.JPG)

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. [Link](https://youtu.be/vzmJMp8j4Xo)

- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*(Optional):* This is where you can provide information about any standout suggestions that you have attempted.

- We have enabled Application insights



## Future Improvements

- More data would help in getting more insights from the Automl and hyperdrive methods
- Feature engineering can be performed
- Different feature reduction techniques could be used like PCA, RFE 
- Using Cross validation techniques would help in cribbing problems like overfitting
- Th model can be converted to ONXX format and be deployed on Edge services.
