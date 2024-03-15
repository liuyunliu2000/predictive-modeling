Skip to content
 Enterprise
Search or jump to…
Pull requests
Issues
Explore
 
@yuliu 
This repository is currently being migrated. It's locked while the migration is in progress.
emarketing-science
/
adhoc_analysis
Public
Cannot fork because repository is locked.
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
adhoc_analysis/lab/yuliu/python/temp.py
@yuliu
yuliu some random python stuff
Latest commit defd466 on May 17, 2023
 History
 1 contributor
102 lines (85 sloc)  2.39 KB
 

# %%-*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""


import sys, os
import numpy as np
import pandas as pd
from datetime import timedelta, date, datetime
import pandas.io.sql as psql
import dask
import dask.dataframe as dd
import sqlalchemy as sq

from labutil import abtest, create_sqlengine, read_parquet
print(sys.version)

# %% redshift tester after !fanauth 
import os
import pprint
  
# Get the list of user's
# environment variables
env_var = os.environ
  
# Print the list of user's
# environment variables
print("User's Environment variable:")
pprint.pprint(dict(env_var), width = 1)

#%% create engine
engine = create_sqlengine()



# %% cell separtor
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

s1 = Series(range(0,4))
s1
s2= Series(range(1,5))
s2
s3= s2+s1 
print(s3)
print(dir(5))
s4=s3.T
print(s3.T)
#%%
df = DataFrame()
type(df)

df = pd.read_csv('file.csv')
df
df = pd.read_csv('file.csv', header=0, index_col=0, quotechar='"', sep=',', 
                 na_values=['na', '-','.', ''])
df 
#%%
#test sample
adf = pd.DataFrame(np.random.randint(0,100,size=(10,4))*1.001,columns=list('ABCD'))
adf.head()
bdf = pd.DataFrame(np.random.randint(0,100,size=(10,5)),columns=list('ABCDE'))
pd.merge(adf, bdf, how="outer", indicator=True) #.query('_merge == "left_only"')

bdf["X"]= bdf[['A','B']].apply(lambda row: "=>".join(row.values.astype(str)),axis=1)

adf.style.format(precision=5)
bdf.head()
# %%
train = bdf.sample(frac=0.5, replace=False, random_state=1)
test = bdf.drop(train.index)
print(train.index)
print(test.index)
# %%
# check pandas dataframe query 
adf = pd.DataFrame(np.random.randint(0,200,size=(50,4))*1.001,
                    columns=list('ABCD'),
                    index=pd.date_range(start='1/1/2023', periods=50)
                    )
adf["dt"]=adf.index
adf["id"]=np.random.choice([1,2,3,4], size=50)
refdt=adf['dt'].max() +timedelta(days=-1)
refdt
#adf.reset_index()
#bdf=adf.query('dt')
#bdf.head()
#print(adf)
# %% 
ref_date = '2023-03-24'
week_ref_day= 'Mon' 
DATE_FORMAT = '%Y-%m-%d'
def get_date(dt: str, minus_days=1):
    return (datetime.strptime(dt, DATE_FORMAT).date() - timedelta(days=minus_days)).strftime(DATE_FORMAT)

week_ref_day_map = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
week_ref_date = get_date(ref_date, minus_days=pd.to_datetime(ref_date).weekday() - week_ref_day_map[week_ref_day])

week_ref_date
# %%
FooterFanatics, Inc.
Fanatics, Inc.
Fanatics, Inc.
© 2024 GitHub, Inc.
Footer navigation
Help
Support
API
Training
Blog
About
GitHub Enterprise Server 3.9.4
adhoc_analysis/temp.py at 1d92d5a3c2567c104577e2acff6d33bfce5b4598 · emarketing-science/adhoc_analysis