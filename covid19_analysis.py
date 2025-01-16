import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
df = pd.read_csv('covid_19_data.csv')
# print(df.head(50))
df.drop(['SNo', 'Last Update'], axis=1, inplace=True)
df.rename(columns={'ObservationDate': 'Date', 'Country/Region': 'Country'}, inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
imputer = SimpleImputer(strategy='constant')
df2 = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
df3 = df2.groupby(['Country', 'Date'])[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
#print(df3.head(20))

countries = df3['Country'].unique()
#print(len(countries))

'''for idx in range(0, len(countries)):
    C=df3[df3['Country']==countries[idx]].reset_index()
    plt.scatter(np.arange (0, len(C)), C['Confirmed'], color = 'blue' , label = 'Confirmed')
    plt.scatter(np.arange (0, len(C)), C['Deaths'], color = 'red' , label = 'Deaths')
    plt.scatter(np.arange (0, len(C)), C['Recovered'], color = 'green' , label = 'Recovered')
    plt.title(countries[idx])
    plt.xlabel('Days since the first suspect')
    plt.ylabel('Number of cases')
    plt.legend()
    plt.show()'''
    
df4 = df3.groupby('Date')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

c = df4
plt.scatter(np.arange (0, len(c)), c['Confirmed'], color = 'blue' , label = 'Confirmed')
plt.scatter(np.arange (0, len(c)), c['Deaths'], color = 'red' , label = 'Deaths')
plt.scatter(np.arange (0, len(c)), c['Recovered'], color = 'green' , label = 'Recovered')
plt.title('World')
plt.xlabel('Days since the first suspect')
plt.ylabel('Number of cases')
plt.legend()
plt.show()