import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm  

dataset1=pd.read_csv('Train.csv')
dataset2=pd.read_csv('Test.csv')
y_train=dataset1.iloc[:,-1].values
X_train=dataset1.iloc[:, :-1].values
X_test=dataset2

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)

y_pred=regressor.predict(X_test)

X_opt=np.array(X_train[:,[0,1,2,3,4]],dtype=float)
regressor_OLS=sm.OLS(endog=y_train,exog=X_opt).fit()
print(regressor_OLS.summary())

** P VALUE FOR ALL THE VARIABLE IS EQUAL TO ZERO
  THEREFORE ALL THE VARIABLES ARE SIGNIFICANT
  SO NO NEED FOR ELIMINATION **
