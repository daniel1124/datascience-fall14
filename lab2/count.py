
# coding: utf-8

# In[36]:

import avro.schema
from avro.datafile import DataFileReader
from avro.io import DatumReader

import pandas as pd
import numpy as np

reader = DataFileReader(open("countries.avro", "r"), DatumReader())
countries = pd.DataFrame(columns=["name", "country_id", "area_sqkm", "population"])

for item in reader:
    countries = countries.append(item, ignore_index=True)

len(countries[countries.population > 10000000])

