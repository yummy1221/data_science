# pandas package

import pandas as pd
animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)

numbers = [1, 2, 3]
pd.Series(numbers)

# dealing with missing numbers
# underlying uses numpy
animals = ['Tiger', 'Bear', None]
pd.Series(animals)

numbers = [1, 2, None]
pd.Series(numbers)

import numpy as np
np.nan == None # False
np.nan == np.nan # False
np.isnan(np.nan) # True

###### ###### ######
###### pandas.Series - between list and dictionary
###### ###### ######

# How to initialize from dictionary
sports = {
	'Archery' : 'Bhutan',
	'Golf' : 'Scotland',
	'Sumo' : 'Japan',
	'Taekwondo' : 'South Korea'
}
s = pd.Series(sports)
s
s.index
s2 = pd.Series(['Bhutan', 'Scotland', 'Japan', 'South Korea'], 
	index = ['Archery', 'Golf', 'Sumo', 'Taekwondo'])
s3 = pd.Series(['Archery', 'Golf', 'Sumo', 'Taekwondo'], 
	index = ['a', 'b'])

# indexing data
# better use iloc/loc if index label is integer
s.iloc[3] == s[3]
s.loc['Golf'] == s['Golf']

sports = {
	99 : 'Bhutan',
	100 : 'Scotland',
	101 : 'Japan',
	102 : 'South Korea'
}
s3 = pd.Series(sports)

# pandas underlying is numpy library, vectorization, most numpy functioins
s = pd.Series([100.00, 120.00, 101.00, 3.00])
total = np.sum(s)
print(total)

s = pd.Series(np.random.randint(0, 1000, 10000))
s.head()
len(s)

# broadcasting
s += 2
for label, value in s.iteritems():
	s.set_value(label, value+2)
	s.loc[label] = value + 2

# duplicate label index
sports = {
	'Archery' : 'Bhutan',
	'Golf' : 'Scotland',
	'Sumo' : 'Japan',
	'Taekwondo' : 'South Korea'
}

original_sports = pd.Series(sports)
cricket_loving_countries = pd.Series(
	['Australia', 'Barbados', 'Pakistan', 'England'], 
	index = ['Cricket', 'Cricket', 'Cricket', 'Cricket'])
# will not modify original Series, will create a new one
all_countries = original_sports.append(cricket_loving_countries)


###### ###### ######
###### pandas.DataFrame - between list and dictionary
###### ###### ######



