'''
Assignment 
Filename: "dspl.py"
Date: 2020
Authors: Fleur Wieland, Nancy Subke, Justus Holman
Group: 1
'''

###########################################################
### Imports
import numpy as np                       # for numerical methods
import matplotlib.pyplot as plt          # for plotting 
import pandas as pd                      # for data input and output
import scipy.stats as st                 # for statistical functions
from numpy.polynomial import Polynomial as P
from scipy.interpolate import interp1d
import matplotlib.dates as mdates
import math 

###########################################################

def parta():
    global df
    
    names= ["salary","pcsalary", "sales", "roe", "pcroe", "ros", "indus",
            "finance", "consprod", "utility", "lsalary", "lsales"]
    
    data = pd.read_csv('data1.csv', delimiter=';', names = names)
    print(data)
    #data = pd.DataFrame(columns=np.arange(0,data.shape[1]))
    
    
    df = pd.DataFrame(columns=names)
    
    
    df.loc[0] = names
    df = df.append([data]*data.shape[1], ignore_index=True)
    
    #print(df)

    #salary in thousands
    #

    print(df.iloc[0, 0])
    
    salary = df["salary"]
    
    
    for i in range(df.shape[1]):
        
        title = df.iloc[0,i]
        print(title)
        vCol = df[title]
        #print(vCol[1:])
        
        createhist(vCol[1:], title)
        summaryStatistics(vCol[1:], len(df), title)
        createscatter(salary[1:], vCol[1:], title, salary.iloc[0])    
    
# =============================================================================
#     plt.subplot(1,3,2)
#     createhist(data2018_T, data1962_T, "temperature", "celcius", "2018", "1962")
#     
#     plt.subplot(1,3,3)
#     createhist(dataRH_sub2018, dataRH_sub1962, "rain", "mm", "2018", "1962")
# =============================================================================
 

def createhist(data, title):
    #Creates a histogram of the given data with its accessory information.    
    
    plt.hist(data, bins=100, color=('red'))
    plt.title(title,fontweight='bold')
    #plt.xlabel(xlabel) 
    #plt.legend([a_label,b_label])  
    plt.show()
    
def summaryStatistics(vX, iN, text):
    print (text)
    dMean = np.mean( vX ) 
    print('mean:', "%.2f" %  dMean )
    dVar = iN/(iN-1) * np.var( vX ) 
    dStdev = np.sqrt( dVar ) 
    print('stdev:', "%.2f" %  dStdev )
    dMax = np.max(vX)
    print('max:',"%.2f" % dMax )
    dMin = np.min(vX)
    print('min:', "%.2f" % dMin)
    
def createscatter(vX, vY, xaxis, yaxis):
    plt.plot( vX , vY , "." )
    plt.ylabel(yaxis)
    plt.xlabel(xaxis)
    #plt.title(title)
    plt.show()

###########################################################
### main
def main():
    parta()
    

###########################################################
### start main
if __name__ == "__main__":
    main()