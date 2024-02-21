# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:41:23 2024

@author: yusof
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("Solar Activities Data for SC23.xlsx", parse_dates=['DateTime'], index_col='DateTime')
df2 = pd.read_excel("Solar Activities Data for SC24.xlsx", parse_dates=['DateTime'], index_col='DateTime')
df3 = pd.read_excel("Solar Activities Data for SC25.xlsx", parse_dates=['DateTime'], index_col='DateTime')

numeric_columns = df.select_dtypes(include=['number']).columns
df[numeric_columns] = df[numeric_columns].mask(df[numeric_columns] > 950)

numeric_columns2 = df2.select_dtypes(include=['number']).columns
df2[numeric_columns2] = df2[numeric_columns2].mask(df2[numeric_columns2] > 950)

numeric_columns3 = df3.select_dtypes(include=['number']).columns
df3[numeric_columns3] = df3[numeric_columns3].mask(df3[numeric_columns3] > 950)



column_to_plot=['f10.7 index', 'R(Sunspot Number)']
kindanalysis='M'
df_dmean1=df['f10.7 index'].resample(kindanalysis).mean()
df_dmean2=df['R(Sunspot Number)'].resample(kindanalysis).mean()

df2_dmean1=df2['f10.7 index'].resample(kindanalysis).mean()
df2_dmean2=df2['R(Sunspot Number)'].resample(kindanalysis).mean()

df3_dmean1=df3['f10.7 index'].resample(kindanalysis).mean()
df3_dmean2=df3['R(Sunspot Number)'].resample(kindanalysis).mean()
from sklearn.preprocessing import MinMaxScaler

periodt=[]
if kindanalysis=='D':
    periodt='Daily'
if kindanalysis=='W':
    periodt='Weekly'
if kindanalysis=='M':
    periodt='Monthly'
if kindanalysis=='Y':
    periodt='Yearly'
df['Year']=df.index.year

#df_dmedian1.to_excel("Monthly Median values of f10.7 index on the corresponding phases of the SC23.xlsx")
#df_dmedian2.to_excel("Monthly Median values of Sunspot Number on the corresponding phases of the SC23.xlsx")

#df2_dmedian1.to_excel("Monthly Median values of f10.7 index on the corresponding phases of the SC24.xlsx")
#df2_dmedian2.to_excel("Monthly Median values of Sunspot Number on the corresponding phases of the SC24.xlsx")

#df3_dmedian1.to_excel("Monthly Median values of f10.7 index on the corresponding phases of the SC25.xlsx")
#df3_dmedian2.to_excel("Monthly Median values of Sunspot Number on the corresponding phases of the SC25.xlsx")

#df_dmean1.to_excel("Monthly Mean values of f10.7 index on the corresponding phases of the SC23.xlsx")
#df_dmean2.to_excel("Monthly Mean values of Sunspot Number on the corresponding phases of the SC23.xlsx")

#df2_dmean1.to_excel("Monthly Mean values of f10.7 index on the corresponding phases of the SC24.xlsx")
#df2_dmean2.to_excel("Monthly Mean values of Sunspot Number on the corresponding phases of the SC24.xlsx")

#df3_dmean1.to_excel("Monthly Mean values of f10.7 index on the corresponding phases of the SC25.xlsx")
#df3_dmean2.to_excel("Monthly Mean values of Sunspot Number on the corresponding phases of the SC25.xlsx")

df_dmean = df.resample(kindanalysis).mean()
df2_dmean = df2.resample(kindanalysis).mean()
df3_dmean = df3.resample(kindanalysis).mean()

# Choose columns to normalize
columns_to_normalize = ['f10.7 index']

# Apply Min-Max Scaling to each DataFrame
scaler = MinMaxScaler()
df_dmean[columns_to_normalize] = scaler.fit_transform(df_dmean[columns_to_normalize])
df2_dmean[columns_to_normalize] = scaler.fit_transform(df2_dmean[columns_to_normalize])
df3_dmean[columns_to_normalize] = scaler.fit_transform(df3_dmean[columns_to_normalize])
#df_dmean[columns_to_normalize].to_excel("Normalized Monthly Mean values of f10.7 index on the corresponding phases of the SC23.xlsx")
#df2_dmean[columns_to_normalize].to_excel("Normalized Monthly Mean values of f10.7 index on the corresponding phases of the SC24.xlsx")
#df3_dmean[columns_to_normalize].to_excel("Normalized Monthly Mean values of f10.7 index on the corresponding phases of the SC25.xlsx")


# Assuming df_dmean, df_dmean2, df2_dmean, df2_dmean2, df3_dmean, and df3_dmean2 are already defined

common_time_zone = 'UTC'
columns_to_normalize = ['f10.7 index']  # Adjust the columns as needed
periodt = 'Monthly'  # Adjust as needed

# Convert DataFrame indices to a common time zone
df_dmean[columns_to_normalize].index = df_dmean[columns_to_normalize].index.tz_localize(common_time_zone)
df_dmean2.index = df_dmean2.index.tz_localize(common_time_zone)

df2_dmean[columns_to_normalize].index = df2_dmean[columns_to_normalize].index.tz_localize(common_time_zone)
df2_dmean2.index = df2_dmean2.index.tz_localize(common_time_zone)

df3_dmean[columns_to_normalize].index = df3_dmean[columns_to_normalize].index.tz_localize(common_time_zone)
df3_dmean2.index = df3_dmean2.index.tz_localize(common_time_zone)

# Create a big plot with 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 10), sharex=False)

# Plot for SC23
color1 = 'blue'
ax1.plot(df_dmean[columns_to_normalize].index, df_dmean[columns_to_normalize], color=color1, label='SC23 - normalized f10.7 index')
ax1.set_ylabel('f10.7 index (normalized)', color=color1)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.legend(loc='upper left')

color2 = 'green'
ax1_2 = ax1.twinx()
ax1_2.plot(df_dmean2.index, df_dmean2, color=color2, label='SC23 - R(Sunspot Number)')
ax1_2.set_ylabel('R(Sunspot Number)', color=color2)
ax1_2.tick_params(axis='y', labelcolor=color2)
ax1_2.legend(loc='upper right')

# Add shaded regions for different phases for SC23
phases_sc23 = [
    {'start': '1996-08-01', 'end': '1997-10-31', 'color': 'yellow', 'label': 'Minimum 1 Phase'},
    {'start': '1997-11-01', 'end': '1999-10-31', 'color': 'darkorange', 'label': 'Ascending Phase'},
    {'start': '1999-11-01', 'end': '2001-12-31', 'color': 'darkred', 'label': 'Solar Maximum Phase'},
    {'start': '2002-01-01', 'end': '2004-08-31', 'color': 'orange', 'label': 'Descending Phase'},
    {'start': '2004-09-01', 'end': '2008-12-31', 'color': 'cyan', 'label': 'Minimum 2 Phase'}
]

for phase in phases_sc23:
    start_date = pd.to_datetime(phase['start']).tz_localize(common_time_zone)
    end_date = pd.to_datetime(phase['end']).tz_localize(common_time_zone)
    ax1.axvspan(start_date, end_date, alpha=0.3, color=phase['color'], label=phase['label'])

# Plot for SC24
color3 = 'blue'
ax2.plot(df2_dmean[columns_to_normalize].index, df2_dmean[columns_to_normalize], color=color3, label='SC24 - normalized f10.7 index')
ax2.set_ylabel('f10.7 index (normalized)', color=color3)
ax2.tick_params(axis='y', labelcolor=color3)
ax2.legend(loc='upper left')

color4 = 'green'
ax2_2 = ax2.twinx()
ax2_2.plot(df2_dmean2.index, df2_dmean2, color=color4, label='SC24 - R(Sunspot Number)')
ax2_2.set_ylabel('R(Sunspot Number)', color=color4)
ax2_2.tick_params(axis='y', labelcolor=color4)
ax2_2.legend(loc='upper right')

# Add shaded regions for different phases for SC24
phases_sc24 = [
    {'start': '2009-01-01', 'end': '2010-03-31', 'color': 'yellow', 'label': 'Minimum 1 Phase'},
    {'start': '2010-04-01', 'end': '2011-06-30', 'color': 'darkorange', 'label': 'Ascending Phase'},
    {'start': '2011-07-01', 'end': '2014-08-31', 'color': 'darkred', 'label': 'Solar Maximum Phase'},
    {'start': '2014-09-01', 'end': '2016-06-30', 'color': 'orange', 'label': 'Descending Phase'},
    {'start': '2016-07-01', 'end': '2019-12-31', 'color': 'cyan', 'label': 'Minimum 2 Phase'}
]

for phase in phases_sc24:
    start_date = pd.to_datetime(phase['start']).tz_localize(common_time_zone)
    end_date = pd.to_datetime(phase['end']).tz_localize(common_time_zone)
    ax2.axvspan(start_date, end_date, alpha=0.3, color=phase['color'], label=phase['label'])

# Plot for SC25
color5 = 'blue'
ax3.plot(df3_dmean[columns_to_normalize].index, df3_dmean[columns_to_normalize], color=color5, label='SC25 - normalized f10.7 index')
ax3.set_xlabel('Time')
ax3.set_ylabel('f10.7 index (normalized)', color=color5)
ax3.tick_params(axis='y', labelcolor=color5)
ax3.legend(loc='upper left')

color6 = 'green'
ax3_2 = ax3.twinx()
ax3_2.plot(df3_dmean2.index, df3_dmean2, color=color6, label='SC25 - R(Sunspot Number)')
ax3_2.set_ylabel('R(Sunspot Number)', color=color6)
ax3_2.tick_params(axis='y', labelcolor=color6)
ax3_2.legend(loc='upper right')

# Add shaded regions for different phases for SC25
phases_sc25 = [
    {'start': '2020-01-01', 'end': '2021-04-30', 'color': 'yellow', 'label': 'Minimum 1 Phase'},
    {'start': '2021-05-01', 'end': '2022-08-31', 'color': 'darkorange', 'label': 'Ascending Phase'},
    {'start': '2022-09-01', 'end': '2025-03-31', 'color': 'darkred', 'label': 'Solar Maximum Phase'},
    {'start': '2025-04-01', 'end': '2027-12-31', 'color': 'orange', 'label': 'Descending Phase'},
    {'start': '2028-01-01', 'end': '2030-12-31', 'color': 'cyan', 'label': 'Minimum 2 Phase'}
]

for phase in phases_sc25:
    start_date = pd.to_datetime(phase['start']).tz_localize(common_time_zone)
    end_date = pd.to_datetime(phase['end']).tz_localize(common_time_zone)
    ax3.axvspan(start_date, end_date, alpha=0.3, color=phase['color'], label=phase['label'])

# Set the title for the entire big plot
plt.suptitle('Twin Plots for SC23, SC24, and SC25 - Time Periods with Phases', y=1.02)
plt.tight_layout()
# Display the plot
plt.show()
