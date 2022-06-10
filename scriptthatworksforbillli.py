# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 12:50:02 2022

@author: iavitia

This script was created for Bill Li.
The purpose of this script is to show last date, Voltage, and location of certain 
sites with different parameters.
"""
# first import the functions for downloading data from NWIS

import dataretrieval.nwis as nwis

#List of all the sites to be checked (code is not ready yet but need to link to bottom code)

allSites = ["323313117033901", "323313117033902", "323313117033903"]

all_sites = []

for i in allSites:
    all_sites.append(i)
    



#print(all_sites)

# specify the USGS site code for which we want data.

site = '323932117050801'
# get instantaneous values (iv)

#df = nwis.get_record(sites=site, service='iv', start='2017-12-31', end='2018-01-01')
# get water quality samples (qwdata)

#df2 = nwis.get_record(sites=site, service='qwdata', start='2017-12-31', end='2018-01-01')
# get basic info about the site

df8 = nwis.get_record(sites=site,service='iv', start='2021-12-01', access='3', parameterCd='70969')

#this code will iterate through all the voltages that are 11 or above and also displays the site they belong to
#the code is left as a comment in order to keep it clean. Remove hashtag to run it

#for k in df8["70969"]:
#    if k >= 11:
#        print("This is the voltage: {} this is the site: {}".format(k, site))

#This code grabs the records, organizes them by the parameterCd and displays them based on the site
df4 = nwis.get_record(sites=site, service='iv', start='2017-12-31', parameterCd='70969')

df5 = df4.iloc[-1]

#This code iterates through all the voltage and site number, then displays the last line which shows latest information
df6 = []

for i in df4["70969"]:
    df6.append(i)
  

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
