# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 12:50:02 2022

@author: iavitia

This script was created for Bill Li.
The purpose of this script is to show last date, Voltage, and location of certain 
sites with different parameters. It will now also display Ground Water and Surface Water parameters.
"""
# first import the functions for downloading data from NWIS

import dataretrieval.nwis as nwis
import pandas as pd

#INPUT PROPER SITES HERE:

surfacesite = '11042000'
groundsite = '323932117050801'

#SURFACE WATER CODE

site = surfacesite

df = nwis.get_record(sites=site, service='measurements')

#GROUND WATER CODE

site2 = groundsite

#df4 must have it's parameters checked against what keys are availabe

df4 = nwis.get_record(sites=site2, service='iv', start='2017-12-31', parameterCd='70969')
df5 = df4.iloc[-1]

#Program iterates through voltage, then appends them to df6
df6 = []

for i in df4["70969"]:
    df6.append(i)
  
#Program iterates through all the site numbers, then appends them to df7 
df7 = []

for j in df4["site_no"]:
    df7.append(j)


#PRINTING ALL INFORMATION
print('********************************************************************')
print("SURFACE WATER SITE INFORMATION")
print(site, df.measurement_dt.iat[-1])
print('********************************************************************')
#The following code is just to organize the data into something legible
print("THE LAST VOLTAGE FOR SITE # {} IS: {}".format(df7[-1], df6[-1]))

#print("BELOW IS THE BASIC SITE INFORMATION")
print("___________________________________________________________________")
print("GROUND WATER LAST LOCATION WITH SITE NUMBER, DATE, AND VOLTAGE")
print("********************************************************************")
print(df5)

print("********************************************************************")
print("IF ANY DATA IS DISPLAYED BELOW THIS STATEMENT, IT IS BECAUSE VOLTAGE IS BELOW 11")
print("********************************************************************")

#Program iterates through all voltage, then displays anything which is 11 or below.
for k in df4["70969"]:
    if k <= 11:
        df = pd.DataFrame([k, j], ['Voltage', 'Site No.'])
        print(df)
print("********************************************************************")
  

df7 = []

for j in df4["site_no"]:
    df7.append(j)

#The following code is just to organize the data into something legible
print("THE LAST VOLTAGE FOR SITE # {} IS: {}".format(df7[-1], df6[-1]))

#print("BELOW IS THE BASIC SITE INFORMATION")
print("___________________________________________________________________")
print("BELOW IS THE LAST LOCATION WITH SITE NUMBER, DATE, AND VOLTAGE")
print("___________________________________________________________________")
print(df5)
