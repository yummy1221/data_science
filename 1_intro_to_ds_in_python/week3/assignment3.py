import pandas as pd
import numpy as np

# Assignment 3
# http://pandas.pydata.org/pandas-docs/stable/

# load Energy Indicators.xls
skiprows = list(range(0,16))
skiprows.append(17)
energy = pd.read_excel('Energy Indicators.xls', sheet_name='Energy', 
	skiprows=skiprows, usecols='C:F', skip_footer=38, na_values='...',
	names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'])

energy['Energy Supply'] = energy['Energy Supply'] * 1000000

def rename_country(row):
	country = row['Country']
	if len(country.split('(')) > 1:
		country = country.split('(')[0].strip()
	return country.rstrip('1234567890')

country = energy.apply(rename_country, axis=1)
energy['Country'] = country

energy['Country'].replace('Republic of Korea', 'South Korea', inplace=True)
energy['Country'].replace('United Kingdom of Great Britain and Northern Ireland', 'United Kingdom', inplace=True)
energy['Country'].replace('United States of America', 'United States', inplace=True)
energy['Country'].replace('China, Hong Kong Special Administrative Region', 'Hong Kong', inplace=True)

energy.set_index('Country', inplace=True)

# load GDP
GDP = pd.read_csv('world_bank.csv', skiprows=4)
GDP['Country Name'].replace('Korea, Rep.', 'South Korea', inplace=True)
GDP['Country Name'].replace('Iran, Islamic Rep.', "Iran", inplace=True)
GDP['Country Name'].replace('Hong Kong SAR, China', 'Hong Kong', inplace=True)

GDP.set_index('Country Name', inplace=True)

# load scimagojr-3.xlsx
ScimEn = pd.read_excel('scimagojr-3.xlsx', sheet_name='Sheet1')
ScimEn.set_index('Country', inplace=True)


###### Question 1 (20%) ######
rst1 = pd.merge(ScimEn, energy, 
	how='inner', left_index=True, right_index=True)
recent = ['2006','2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
rst1 = pd.merge(rst1, GDP[recent], how='inner', left_index=True, right_index=True)
rst1.sort_values(by='Rank').iloc[:15]

###### Question 2 (6.6%) ######

outer = pd.merge(ScimEn, energy, 
	how='outer', left_index=True, right_index=True)
outer = pd.merge(outer, GDP[recent], how='outer', left_index=True, right_index=True)

len(outer) - len(rst1) = 318 - 162 = 156


###### Question 3 (6.6%) ######
years = ['2006','2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
q3 = top15.apply(lambda x: np.mean(x[years]), axis=1).sort_values(ascending=False)

###### Question 4 (6.6%) ######
row6 = top15.loc[q3.index[5]]
row6['2015'] - row6['2006']


###### Question 5 (6.6%) ######
np.mean(top15['Energy Supply per Capita'])

Top15 = top15
###### Question 6 (6.6%) ######
Top15['% Renewable'].sort_values(ascending=False).index[0]

###### Question 7 (6.6%) ######
ratio = Top15['Self-citations'] / Top15['Citations']
top = ratio.sort_values(ascending=False)

###### Question 8 (6.6%) ######
###### Question 9 (6.6%) ######
population = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
capital_docs_per_person = Top15['Citable documents'] / population

###### Question 10 (6.6%) ######
median = np.median(Top15['% Renewable'])
cat = [1 if x >= median else 0 for x in Top15['% Renewable']]
Top15['HighRenew'] = cat

###### Question 11 (6.6%) ######
continent = [ContinentDict[x] for x in Top15.index]
Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
Top15['Continent'] = continent
Top15.set_index('Continent').groupby(level=0)['PopEst'].agg(['size', 'sum', 'mean', 'std'])

###### Question 12 (6.6%) ######
Top15['bins for % Renewable'] = pd.cut(Top15['% Renewable'], 5)
continent = [ContinentDict[x] for x in Top15.index]
Top15['Continent'] = continent
Top15.set_index(['Continent', 'bins for % Renewable']).groupby(level=[0,1]).agg('size')

###### Question 13 (6.6%) ######
def numToStr(num):
	num = str(num)
	parts = num.split('.')
	first = parts[0]
	first = ','.join([first[max(0, i-3):i] for i in range(len(first), 0, -3)][::-1])
	return '.'.join([first, parts[1]])

num = 12317615384.61538464
numToStr(num)
population = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
population.apply(numToStr)



