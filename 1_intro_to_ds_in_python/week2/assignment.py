import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

###### Part One
def answer_zero():
    return df.iloc[0]
answer_zero()

def answer_one():
    return df[df['Gold']==max(df['Gold'])].index[0]

def answer_two():
	diff = abs(df['Gold'] - df['Gold.1'])
	return diff.sort_values(ascending=False).index[0]

def answer_three():
	tmp = df[['Gold', 'Gold.1', 'Gold.2']].dropna()
	tmp = tmp[(tmp['Gold'] != 0) & (tmp['Gold.1'] != 0)]
	ratio = (tmp['Gold'] - tmp['Gold.1'])/tmp['Gold.2']
	return ratio.sort_values(ascending=False).index[0]

def answer_four():
	points = df['Gold.2'] * 3 + df['Silver.2'] * 2 + df['Bronze.2']
    return points



###### Part Two
import pandas as pd
census_df = pd.read_csv('census.csv')
#census_df.head()
def answer_five():
	st_cty = census_df[['STNAME','CTYNAME']]
	st_cty = st_cty.groupby('STNAME').nunique()
	return st_cty.sort_values(ascending=False, by='CTYNAME').index[0]

# very import: SUMLEV = 40, total of all 50, on state level, 40, on county level
def answer_six():
	pop = census_df[['STNAME','CENSUS2010POP']]
	pop = pop[census_df['SUMLEV']==50]
	pop = pop.set_index('STNAME')
	grouped = pop.groupby(pop.index)
	top3 = grouped.apply(lambda x: x.sort_values('CENSUS2010POP', ascending=False)[:3].sum())
	return list(top3.sort_values('CENSUS2010POP', ascending=False)[:3].index)

def answer_seven():
	pop = census_df[['CTYNAME', 'POPESTIMATE2010', 'POPESTIMATE2011', 
	'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 
	'POPESTIMATE2015']]
	pop = pop[census_df['SUMLEV']==50]
	pop = pop.set_index('CTYNAME')
	pop['diff'] = pop.max(axis = 1) - pop.min(axis=1)
	pop.sort_values('diff', ascending=False, inplace=True)
	return pop.iloc[0].name

def answer_eight():
	rst = census_df[['STNAME', 'CTYNAME']]
	boolean_mask = (census_df['REGION'] == 1) | (census_df['REGION'] == 2)
	boolean_mask = boolean_mask & census_df['CTYNAME'].str.startswith('Washington')
	boolean_mask = boolean_mask & (census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014'])
    return rst[boolean_mask]




