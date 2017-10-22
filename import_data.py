import numpy as np
import pandas as pd
from sklearn.cross_validation import ShuffleSplit


#import all data sets aka 2016 data set
data = pd.read_csv('data-sets/Parcels_2016_Data_Full.csv',header=0);

#probs the actual price
prices = data["AV_TOTAL"];

#potential features
features = data.drop('AV_TOTAL', axis=1);

print("Boston housing dataset has {0} data points and {1} variables each".format(*data.shape))
