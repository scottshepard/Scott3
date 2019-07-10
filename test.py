import pdb
import pandas as pd
from Scott3.Scott3 import Scott3
import yaml
    
with open('config.yml', 'r') as stream:
    creds = yaml.safe_load(stream)

s = Scott3(
    creds['aws_access_key_id'], 
    creds['aws_secret_access_key'], 
    creds['default_bucket'])

d = {'a': 1, 'b': 2, 'c': {'d': 3}}
df = pd.DataFrame({'id': [1, 2, 3], 'value': [2, 4, 6]})

s.write_json(d, 'test_json.json')
s.write_csv(df, 'test_df.csv')

d2  = s.read_json('test_json.json')
df2 = s.read_csv('test_df.csv')

print('JSON functions work: ', d == d2)
print('CSV functions work: ', df.equals(df2))
