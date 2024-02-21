# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:49:09 2024

@author: yusof
"""

import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
import seaborn as sns
df=pd.read_excel("Solar Activities Data for SC23.xlsx", parse_dates=['DateTime'],index_col='DateTime')
df2= pd.read_excel("Solar Activities Data for SC24.xlsx", parse_dates=['DateTime'],index_col='DateTime')
df3= pd.read_excel("Solar Activities Data for SC25.xlsx", parse_dates=['DateTime'],index_col='DateTime')


df.index = pd.to_datetime(df.index)
df2.index = pd.to_datetime(df2.index)
df3.index = pd.to_datetime(df3.index)
phases = {
    'Minimum 1': (pd.to_datetime('1996-08-01'), pd.to_datetime('1997-11-01')),
    'Ascending': (pd.to_datetime('1997-11-01'), pd.to_datetime('1999-11-01')),
    'Maximum': (pd.to_datetime('1999-11-01'), pd.to_datetime('2002-01-01')),
    'Declining': (pd.to_datetime('2002-01-01'), pd.to_datetime('2004-09-01')),
    'Minimum 2':(pd.to_datetime('2004-09-01'), pd.to_datetime('2009-01-01'))
}
df['solar_cycle_phase'] = ''

# Classify each year into the corresponding phase
for phase, (start_date, end_date) in phases.items():
    df.loc[(df.index >= start_date) & (df.index <= end_date), 'solar_cycle_phase'] = phase

# Print the resulting DataFrame
#df.to_excel("test.xlsx")
phases2 = {
    'Minimum 1': (pd.to_datetime('2009-01-01'), pd.to_datetime('2010-04-01')),
    'Ascending': (pd.to_datetime('2010-04-01'), pd.to_datetime('2011-07-01')),
    'Maximum': (pd.to_datetime('2011-07-01'), pd.to_datetime('2014-09-01')),
    'Declining': (pd.to_datetime('2014-09-01'), pd.to_datetime('2016-07-01')),
    'Minimum 2':(pd.to_datetime('2016-07-01'), pd.to_datetime('2020-01-01'))
}
df2['solar_cycle_phase'] = ''
for phase, (start_date, end_date) in phases2.items():
    df2.loc[(df2.index >= start_date) & (df2.index <= end_date), 'solar_cycle_phase'] = phase
    
stats_by_phaseSC23R=df.groupby('solar_cycle_phase')['R(Sunspot Number)'].describe()
stats_by_phaseSC23f=df.groupby('solar_cycle_phase')['f10.7 index'].describe()  
    
stats_by_phaseSC24R=df2.groupby('solar_cycle_phase')['R(Sunspot Number)'].describe()
stats_by_phaseSC24f=df2.groupby('solar_cycle_phase')['f10.7 index'].describe()  

phases3 = {
    'Minimum 1': (pd.to_datetime('2020-01-01'), pd.to_datetime('2021-05-01')),
    'Ascending': (pd.to_datetime('2021-05-01'), pd.to_datetime('2022-09-01')),
    'Maximum (So far)': (pd.to_datetime('2022-09-01'), pd.to_datetime('2024-01-01'))
}
df3['solar_cycle_phase'] = ''
for phase, (start_date, end_date) in phases3.items():
    df3.loc[(df3.index >= start_date) & (df3.index <= end_date), 'solar_cycle_phase'] = phase
stats_by_phaseSC25R=df3.groupby('solar_cycle_phase')['R(Sunspot Number)'].describe()
stats_by_phaseSC25f=df3.groupby('solar_cycle_phase')['f10.7 index'].describe()


stats_by_phaseSC23R.to_excel("Statistics of Sunspot Number in phases (SC23).xlsx")
stats_by_phaseSC24R.to_excel("Statistics of Sunspot Number in phases (SC24).xlsx")
stats_by_phaseSC25R.to_excel("Statistics of Sunspot Number in phases (SC25).xlsx")

stats_by_phaseSC23f.to_excel("Statistics of f10.7 index in phases (SC23).xlsx")
stats_by_phaseSC24f.to_excel("Statistics of f10.7 index in phases (SC24).xlsx")
stats_by_phaseSC25f.to_excel("Statistics of f10.7 index in phases (SC25).xlsx")