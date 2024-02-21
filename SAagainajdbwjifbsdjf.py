# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 18:35:40 2024

@author: yusof
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_excel("SAvsGCR phases stats for pp.xlsx", sheet_name="Sheet1")
plt.figure(figsize=(10,13))
plt.subplot(5,1,1)
sns.barplot(x='Phases', y='Mean R',hue='Solar Cycle',data=df,color='blue')

plt.title('Comparison of averaged value between solar activities and particle fluxes in first 4 years of all SCs ')
plt.subplot(5,1,2)
sns.barplot(x='Phases', y='Mean F10.7 index', hue='Solar Cycle', data=df,color='green')

plt.subplot(5,1,3)
sns.barplot(x='Phases', y='Mean Neutron Count',hue='Solar Cycle', data=df,color='purple')

plt.subplot(5,1,4)
sns.barplot(x='Phases', y='Mean PF',hue='Solar Cycle',data=df,color='darkorange')

plt.subplot(5,1,5)
sns.barplot(x='Phases', y='Mean HF',hue='Solar Cycle', data=df,color='darkred')

plt.tight_layout()
plt.savefig('Comparison of averaged value between solar activities and particle fluxes in first 4 years of all SCs.png')
plt.show()
plt.figure(figsize=(10,13))
plt.subplot(5,1,1)
sns.lineplot(x='Phases', y='Mean R',data=df,color='blue',linewidth=2,marker='o',markerfacecolor='black', markersize=7)

plt.title('Comparison of averaged value between solar activities and particle fluxes across in first 4 years of all SCs (combined)')
plt.subplot(5,1,2)
sns.lineplot(x='Phases', y='Mean F10.7 index', data=df,color='green',linewidth=2,marker='o',markerfacecolor='black', markersize=7)

plt.subplot(5,1,3)
sns.lineplot(x='Phases', y='Mean Neutron Count',data=df,color='purple',linewidth=2,marker='o',markerfacecolor='black', markersize=7)

plt.subplot(5,1,4)
sns.lineplot(x='Phases', y='Mean PF',data=df,color='darkorange',linewidth=2,marker='o',markerfacecolor='black', markersize=7)

plt.subplot(5,1,5)
sns.lineplot(x='Phases', y='Mean HF', data=df,color='darkred',linewidth=2,marker='o',markerfacecolor='black', markersize=7)

plt.tight_layout()
plt.savefig('Comparison of averaged value between solar activities and particle fluxes in first 4 years of all SCs (combined).png')
plt.show()

plt.figure(figsize=(10,13))
plt.subplot(4,1,1)
sns.barplot(x='Phases', y='Mean R',hue='Solar Cycle', data=df,color='blue',)

plt.title(f'Comparison of averaged value between solar activities and space weather events in first 4 years of all SCs')
plt.subplot(4,1,2)
sns.barplot(x='Phases', y='Mean F10.7 index',hue='Solar Cycle', data=df,color='green')

plt.subplot(4,1,3)
sns.barplot(x='Phases', y='Average SF',hue='Solar Cycle', data=df,color='purple')
plt.subplot(4,1,4)
sns.barplot(x='Phases', y='Average GS',hue='Solar Cycle',data=df,color='darkorange')
plt.tight_layout()
plt.savefig('Comparison of maximum value between solar activities space weather events in first 4 years of all SCs.png')
plt.show()

plt.figure(figsize=(10,13))
plt.subplot(4,1,1)
sns.lineplot(x='Phases', y='Mean R',data=df,color='blue',linewidth=2,marker='o',markerfacecolor='black', markersize=7)

plt.title(f'Comparison of averaged value between solar activities and space weather events in first 4 years of all SCs (combined)')
plt.subplot(4,1,2)
sns.lineplot(x='Phases', y='Mean F10.7 index', data=df,color='green',linewidth=2,marker='o',markerfacecolor='black', markersize=7)

plt.subplot(4,1,3)
sns.lineplot(x='Phases', y='Average SF', data=df,color='purple',linewidth=2,marker='o',markerfacecolor='black', markersize=7)
plt.subplot(4,1,4)
sns.lineplot(x='Phases', y='Average GS',data=df,color='darkorange',linewidth=2,marker='o',markerfacecolor='black', markersize=7)
plt.tight_layout()
plt.savefig('Comparison of maximum value between solar activities space weather events in first 4 years of all SCs (combined).png')
plt.show()