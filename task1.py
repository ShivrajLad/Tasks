
import pandas as pd
from faker import Faker
from datetime import datetime
import random

fake = Faker()

lst_id = []
lst_name = []
lst_add = []
lst_dt = []
lst_bol = []
lst_flt = []
lst_pvd = []
lst_sc = []
lst_ph = []
lst_job = []

num_rows = 1000
num_cols = 1000

for i in range(1, 1001):
    p = "CASP" + "0" * (16 - len(str(i))) + str(i)
    lst_id.append(p)

for _ in range(1000):
    a=fake.name()
    lst_name.append(a)
    b=fake.address()
    lst_add.append(b)
    c=fake.date_between_dates(date_start=datetime(1950,1,1),date_end=datetime(1996,12,31))
    lst_dt.append(c)
    d=fake.pybool()
    lst_bol.append(d)
    e=fake.pyfloat(min_value=0,max_value=1000000)
    lst_flt.append(e)
    f=fake.credit_card_provider()
    lst_pvd.append(f)
    g=fake.credit_card_security_code()
    lst_sc.append(g)
    h=fake.phone_number()
    lst_ph.append(h)
    j=fake.job()
    lst_job.append(j)

dict = {'Customer_ID': lst_id, 'Name': lst_name, 'Date of Birth': lst_dt, 'Address': lst_add, 'Job Profile': lst_job,
        'Phone Number': lst_ph, 'Credit Card Provider': lst_pvd, 'Credit Amount': lst_flt, 'credit card security code': lst_sc,
        'Credit Defaulter Status': lst_bol}

# Generate the header row with column names
header_row = ['col' + str(i+1) for i in range(num_cols)]

# Generate the data rows with random values
data_rows = [[random.randint(1, 1000) for j in range(num_cols)] for i in range(num_rows)]

# Convert dictionary to dataframe
df = pd.DataFrame(dict)
df2 = pd.DataFrame(data_rows, columns=header_row)

# List of two dataframes
frames=[df,df2]

# Concatenated the two dataframes.
res = pd.concat(frames, axis=1)

# Save Dataframe in csv format.
res.to_csv('EmployeeData.csv', index=False)
