import numpy as np
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator

mydata=pd.read_csv("heart_disease_data.csv")
np.set_printoptions(threshold=np.nan)
names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'heartdisease']
heartDisease = pd.read_csv( "heart_disease_data.csv")
display(heartDisease.head())
del heartDisease['ca']
del heartDisease['slope']
del heartDisease['thal']
del heartDisease['oldpeak']
heartDisease = heartDisease.replace('?', np.nan)

model = BayesianModel([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'), ('sex', 'trestbps')
,('exang', 'trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),('heartdisease','restecg')
,('heartdisease','thalach'),('heartdisease','chol')])
model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)
from pgmpy.inference import VariableElimination
HeartDisease_infer = VariableElimination(model)
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': 32})
print(q['heartdisease'])
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'chol': 100})
print(q['heartdisease'])
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'trestbps': 10})
print(q['heartdisease'])
