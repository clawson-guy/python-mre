#List needed packages
import time
import yaml
import os
from pathlib import Path
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import warnings
import functools as ft
from yaml import safe_load
#credentials stored here (keep secure by placing them locally)
creds = yaml.safe_load(open(r"C:\Users\clawson\Python_Projects\Initial\credentials.yml"))

# grab credentials

##zeus connection string
z_user = creds['ZEUS_1']['username']
z_password = creds['ZEUS_1']['password']
z_host = creds['ZEUS_1']['hostname']
z_port = creds['ZEUS_1']['port']
z_database = 'mail_report'

##sugar connection string
s_user = creds['Sugar']['user']
s_password = creds['Sugar']['password']
s_host = creds['Sugar']['host']
s_port = creds['Sugar']['port']
s_database = creds['Sugar']['database']

# create connection engine, then test connection
def zeus_cnx():
    '''
    connect to mysql db and return an engine object
    '''
    return create_engine(
        url= f'mysql://{z_user}:{z_password}@{z_host}:{z_port}/{z_database}'
        ).raw_connection()
def sugar_cnx():
    '''
    connect to mysql db and return an engine object
    '''
    return create_engine(
        url= f'mysql://{s_user}:{s_password}@{s_host}:{s_port}/{s_database}'
        ).raw_connection()
 
# connection error handling

if __name__ == '__main__':
 
    try:
        z_engine = zeus_cnx()
        print(f"Connection to {z_host} for user: {z_user} created successfully.\n")
        s_engine = sugar_cnx()
        print(f"Connection to {s_host} for user: {s_user} created successfully.\n")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)


zeus_query = """
select *
from sugar_dms2
#where category = 'TRSP'
#limit 100
;
"""

# Implementation of matplotlib function
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
   
np.random.seed(10**7)
n_bins = 20
x = np.random.randn(10000, 3)
   
colors = ['green', 'blue', 'lime']
 
plt.hist(x, n_bins, density = True, 
         histtype ='bar',
         color = colors,
         label = colors)
 
plt.legend(prop ={'size': 10})
 
plt.title('matplotlib.pyplot.hist() function Example\n\n',
          fontweight = "bold")
 
plt.show()

pd.read_sql_query('show databases', zeus_cnx(), index_col=None)