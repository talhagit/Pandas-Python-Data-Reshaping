# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 19:30:48 2018

@author: Talha.Iftikhar
"""
import pandas as pd
import calendar
import numpy as np
import matplotlib.pyplot as plt
##Pandas : Reshaping Data

#Lets attach a csv sample file#C:\Users\Talha.Iftikhar\Desktop
ss_data=pd.read_excel("C:\\Users\\Talha.Iftikhar\\Desktop\\SuperStoreOrders.xls",sep=",")# Change to where your file is

ss_data.head # To see few rows.

n=5
ss_data_sample=ss_data[:int(len(ss_data)*(n/100))] # Sample the data by percentage

len(ss_data_sample)
ss_data_sample.head

##Pivoting data##
# Lets Slice and get needed columns
ss_data_final=ss_data_sample.loc[:,['Order Date','Ship Mode','Profit']]
#Extract Month from Order Date
ss_data_final['Month'] = ss_data_final['Order Date'].dt.month
#Change Month number to name
ss_data_final['Month'] = ss_data_final['Month'].apply(lambda x: calendar.month_abbr[x])
#Pivot Table
ss_data_piv=ss_data_final.pivot_table(index="Ship Mode", columns="Month", values="Profit")
#DIfferent Aggregation level
ss_data_piv=ss_data_final.pivot_table(index="Ship Mode", columns="Month", values="Profit",aggfunc='count')
##Grand Total for each month##
ss_data_piv.sum(axis=0)
##Grand Total for each Ship Mode##
ss_data_piv.sum(axis=1)


##Lets Plot  some thing to see visual Appearance
fig, ax1 = plt.subplots()
ss_data_final.pivot_table(index="Ship Mode", columns="Month", values="Profit",aggfunc='count').plot(kind='bar', 
                                                       rot=0, 
                                                       ax=ax1)
ax1.set_ylabel('Survival ratio')
ax1.set_xlabel('Ship Mode')


ss_data_final['Profit<5000'] = ss_data_final['Profit'] <= 5000

ss_data_final.pivot_table(index="Profit<5000", columns="Month", values="Profit",aggfunc='count')

##Melt Data##
pivoted = ss_data_final.pivot_table(index="Profit<5000", columns="Month", values="Profit").reset_index()
pd.melt(pivoted)
pd.melt(pivoted, id_vars=['Profit<5000'])

##Group by and Unstack##
group=ss_data_final.groupby(['Month','Ship Mode']).size()
tbl=group.unstack('Ship Mode')

tbl.plot()

##Plot a Crosstab##
pd.crosstab(index=ss_data_final['Month'],columns=ss_data_final['Ship Mode']).plot(kind='Area')







