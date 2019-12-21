#%%
import pandas as pd
import datetime as dt
from datetime import date, timedelta, datetime
from mpg_refresh import mpg_data_creator
from mpg_insights import mpg_insights

#%%
df = pd.read_csv('moped_mpg_data.csv')
df = mpg_data_creator(df)
df.name = 'Moped Data'

mpg_insights(df)

# %%
