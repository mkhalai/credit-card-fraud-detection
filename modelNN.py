from keras.layers import Dense 
from keras.models import Sequential 
from keras.activations import tanh

from sklearn.preprocessing import StandardScaler
from sklean.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

def buildModel(data):
    pass



def tsne(data):
    predictors = data.iloc[:,0:-1].values
    target = data.iloc[:,-1].values
    x = StandardScaler().fit_transform(predictors)

    tsne = TSNE()


data = pd.read_csv('creditcard.csv')
data.drop(['Time'],axis=1,inplace=True)
data = data.sample(frac=1)
variances = princomp(data)
plt.plot(np.arange(1,data.shape[1],1), variances)
plt.show()




