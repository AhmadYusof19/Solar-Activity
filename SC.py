# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:12:46 2024

@author: yusof
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel('Wind Helium Data 1996-2023.xlsx')
#df2= pd.read_excel("Solar Activities Data for SC23.xlsx")
df3= pd.read_excel("Wind Satellite Protnn Data.xlsx")
df4= pd.read_excel("Cosmic Ray Flux Data Oulu.xlsx")
df.index=(df['DateTime'])
#df2.index=(df2['DateTime'])
df3.index=(df3['DateTime'])
df4.index=(df4['DateTime'])

numeric_columns = df.select_dtypes(include=['number']).columns
df[numeric_columns] = df[numeric_columns].mask((df[numeric_columns] <= 5e-5) | (df[numeric_columns] > 1.2))

#numeric_columns2 = df2.select_dtypes(include=['number']).columns
#df2[numeric_columns2] = df2[numeric_columns2].mask(df2[numeric_columns2] > 950)

numeric_columns3 = df3.select_dtypes(include=['number']).columns
df3[numeric_columns3] = df3[numeric_columns3].mask((df3[numeric_columns3] <= 2)| (df3[numeric_columns3] >200)) 

numeric_columns4 = df4.select_dtypes(include=['number']).columns
df4[numeric_columns4] = df4[numeric_columns4].mask(df4[numeric_columns4] > 10000)
start_datetime = pd.to_datetime('2020-09-01 00:00:00')
end_datetime = pd.to_datetime('2023-12-31 23:59:00')
df = df[(df['DateTime'] >= start_datetime) & (df['DateTime'] <= end_datetime)]
df3 = df3[(df3['DateTime'] >= start_datetime) & (df3['DateTime'] <= end_datetime)]
df4 = df4[(df4['DateTime'] >= start_datetime) & (df4['DateTime'] <= end_datetime)]
df['solar_cycle_phase'] = ''
phases = {
    'Minimum 1': (pd.to_datetime('2020-01-01'), pd.to_datetime('2021-05-01')),
    'Ascending': (pd.to_datetime('2021-05-01'), pd.to_datetime('2022-09-01')),
    'Maximum (So far)': (pd.to_datetime('2022-09-01'), pd.to_datetime('2024-01-01'))
}
# Classify each year into the corresponding phase
for phase, (start_date, end_date) in phases.items():
    df.loc[(df.index >= start_date) & (df.index <= end_date), 'solar_cycle_phase'] = phase

# Print the resulting DataFrame
#df.to_excel("test.xlsx")
phases2 = {
    'Minimum 1': (pd.to_datetime('2020-01-01'), pd.to_datetime('2021-05-01')),
    'Ascending': (pd.to_datetime('2021-05-01'), pd.to_datetime('2022-09-01')),
    'Maximum (So far)': (pd.to_datetime('2022-09-01'), pd.to_datetime('2024-01-01'))
}
df3['solar_cycle_phase'] = ''
for phase, (start_date, end_date) in phases2.items():
    df3.loc[(df3.index >= start_date) & (df3.index <= end_date), 'solar_cycle_phase'] = phase
    


phases3 = {
    'Minimum 1': (pd.to_datetime('2020-01-01'), pd.to_datetime('2021-05-01')),
    'Ascending': (pd.to_datetime('2021-05-01'), pd.to_datetime('2022-09-01')),
    'Maximum (So far)': (pd.to_datetime('2022-09-01'), pd.to_datetime('2024-01-01'))
}
df4['solar_cycle_phase'] = ''
for phase, (start_date, end_date) in phases3.items():
    df3.loc[(df3.index >= start_date) & (df3.index <= end_date), 'solar_cycle_phase'] = phase

stats_by_phaseSC25He=df.groupby('solar_cycle_phase')['Helium Flux(4.53-6.00 MeV)'].describe()
stats_by_phaseSC25H=df3.groupby('solar_cycle_phase')['Proton Flux (0.88-1.27) MeV'].describe()  
stats_by_phaseSC25N=df4.groupby('solar_cycle_phase')['CorrectedCountRate[cts/min]'].describe()


stats_by_phaseSC25He.to_excel("Statistics of Helium Flux in phases (SC25).xlsx")
stats_by_phaseSC25H.to_excel("Statistics of Proton Flux Number in phases (SC25).xlsx")
stats_by_phaseSC25N.to_excel("Statistics of Neutron Count in phases (SC25).xlsx")
  