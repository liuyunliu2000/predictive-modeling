import numpy as np 
import pandas as pd 
from datetime import datetime 

#dr= pd.date_range(end = datetime.today(), periods = 100).to_pydatetime().tolist()
#OR
dr=pd.date_range(start="2024-01-01",end="2024-12-31")

N = 10 # simulation for n customer
cid  = range(N) #simulated customerid
region = ['north', 'south', 'central'] #sales region
cage = ['new', 'middle','old'] # customer time on book 
dept = ['hats','cloths','shoes'] # dept of products
D = len(dr) # days of sales for those n customer
P = len(dept) # type of products by dept

# building dataframes
cprofile =pd.DataFrame() # customer profile
pprofile =pd.DataFrame() # product profile
dateprofile= pd.DataFrame() 
saledf = pd.DataFrame() # daily sales
orderdf= pd.DataFrame() # daily order

cprofile['cid'] = cid
dateprofile['date'] = pd.DataFrame(dr)

# add data to df
cprofile['region'] = np.random.choice(region, size=N, p=[0.3, 0.3, 0.4], replace=True)
cprofile['cage'] = np.random.choice(cage, size=N, p=[0.8, 0.1, 0.1], replace=True)
cprofile['abtest'] =np.random.choice([True,False], size=N, p=[0.5,0.5], replace=True )
cus_date = dateprofile.merge(cprofile, how='cross') # cartesian join of customer id and date range

# simulate sales and orders 
saledf = pd.DataFrame(np.random.randint(0,D, size=(D*N, len(dept))), columns=["sales_"+ e for e in dept])
orderdf = pd.DataFrame(np.random.poisson(1, size=D*N*P).reshape(D*N,P), index= range(D*N), columns=["order_"+ e for e in dept])

# final daily summary by customer by date
pmdf = pd.concat([cus_date, saledf, orderdf], axis=1, ignore_index=False )


# %%
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

print(sys.version)

# %% 
import os
import pprint
  
# Get the list of user's
# environment variables
env_var = os.environ
  
# Print the list of user's
# environment variables
print("User's Environment variable:")
pprint.pprint(dict(env_var), width = 1)


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