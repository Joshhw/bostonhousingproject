import numpy as np
import pandas as pd
from sklearn.cross_validation import ShuffleSplit


#import all data sets aka 2016 data set
data = pd.read_csv('data-sets/Parcels_2016_Data_Full.csv',header=0);

#columns to keep
keep_col = [
    "PID", "ZIPCODE", "GROSS_AREA", 
    "LIVING_AREA", "GROSS_TAX", "LAND_SF",
    "YR_BUILT", "YR_REMOD", "NUM_FLOORS",
    "U_TOT_RMS", "U_BDRMS", "U_FULL_BTH",
    "U_HALF_BTH", "U_FPLACE", "SHAPESTArea", 
    "SHAPESTLength" 
    ];

#drop anything that isn't a condo
data = data[pd.notnull(data['U_TOT_RMS'])];

#probs the actual price
prices = data["AV_TOTAL"];

#potential features
features = data[keep_col];

print("Boston housing dataset has {0} data points and {1} variables each".format(*features.shape))

minimum_price = np.min(prices);
max_price = np.max(prices);
mean_price = np.mean(prices);
median_price = np.median(prices);
std_price = np.std(prices);


print("various values contained within our Boston data set");
print("minimum price in the data set:${:,.2f}".format(minimum_price));
print("max price in the data set:${:,.2f}".format(max_price));
print("mean price in the data set:${:,.2f}".format(mean_price));
print("median price in the data set:${:,.2f}".format(median_price));
print("standard deviation of the data set:${:,.2f}".format(std_price));

