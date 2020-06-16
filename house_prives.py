### House Prices: Regression Prediction
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from plotnine import *
from scipy import stats
from scipy.stats import norm, skew

# Dataset importation 
train = pd.read_csv('D:/Second Desktop/Data Science/Datasets/Householder/train.csv')
test = pd.read_csv('D:/Second Desktop/Data Science/Datasets/Householder/test.csv')
